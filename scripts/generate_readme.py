#!/usr/bin/env python3
"""
Generate README.md with live SRS progress tracking
"""

import json
import sys
from pathlib import Path
from datetime import datetime
from collections import defaultdict
from typing import Dict, List, Optional


def load_srs_data() -> Dict:
    """Load SRS data from .srs-data.json"""
    data_file = Path('.srs-data.json')
    if not data_file.exists():
        return {'items': {}, 'stats': {}}

    with open(data_file, 'r') as f:
        return json.load(f)


def get_card_status(card_data: Optional[Dict]) -> tuple:
    """
    Returns (status_emoji, status_text, tier)
    Tier 0: New (never reviewed)
    Tier 1: Seen (1+ reviews, avg < 3)
    Tier 2: Learning (avg >= 3, not mastered)
    Tier 3: Mastered
    """
    if not card_data:
        return '⭐', 'New', 0

    if card_data.get('mastered', False):
        return '🏆', 'Mastered', 3

    reviews = card_data.get('reviews', [])
    if not reviews:
        return '⭐', 'New', 0

    avg_score = sum(r['score'] for r in reviews) / len(reviews)

    if avg_score >= 4.0:
        return '💪', 'Strong', 2
    elif avg_score >= 3.0:
        return '👍', 'Learning', 2
    else:
        return '📖', 'Practicing', 1


def generate_progress_bar(current: int, total: int, width: int = 40) -> str:
    """Generate a text-based progress bar"""
    if total == 0:
        filled = 0
    else:
        filled = int(width * current / total)

    bar = '█' * filled + '░' * (width - filled)
    percentage = (current / total * 100) if total > 0 else 0
    return f"[{bar}] {percentage:.1f}% ({current}/{total})"


def parse_topic_structure() -> Dict[str, Dict[str, List[Dict]]]:
    """
    Scan content directories and organize topics by section and category
    Returns: {section_name: {category_name: [list of topic files]}}
    """
    sections = {
        'ML Workflows': 'ml-workflows',
        'ML Rapid Fire': 'ml-rapid-fire',
        'Math & Quant Foundations': 'math-quant-foundations'
    }

    result = {}

    for section_name, base_dir in sections.items():
        base_path = Path(base_dir)
        topics_by_category = defaultdict(list)

        if not base_path.exists():
            continue

        # Check if directory has subdirectories or just files
        subdirs = [d for d in base_path.iterdir() if d.is_dir()]

        if subdirs:
            # Scan subdirectories (like ml-workflows/01-basics)
            for category_dir in sorted(subdirs):
                category_name = category_dir.name
                for md_file in sorted(category_dir.glob('*.md')):
                    topics_by_category[category_name].append(
                        _parse_md_file(md_file)
                    )
        else:
            # Scan files directly (like math-quant-foundations/*.md)
            category_name = base_dir  # Use dir name as category
            for md_file in sorted(base_path.glob('*.md')):
                topics_by_category[category_name].append(
                    _parse_md_file(md_file)
                )

        if topics_by_category:
            result[section_name] = dict(topics_by_category)

    return result


def _parse_md_file(md_file: Path) -> Dict:
    """Parse a markdown file and extract question info"""
    try:
        with open(md_file, 'r') as f:
            content = f.read()
            if '# Question' in content:
                question = content.split('# Question')[1].split('# Answer')[0].strip()
            else:
                question = md_file.stem.replace('-', ' ').title()
    except:
        question = md_file.stem.replace('-', ' ').title()

    return {
        'file': str(md_file),
        'name': md_file.stem,
        'question': question,
        'number': md_file.stem.split('-')[0] if '-' in md_file.stem else ''
    }


def generate_category_section(category: str, topics: List[Dict], srs_data: Dict) -> str:
    """Generate markdown for a category section"""
    # Clean up category name
    category_display = category.replace('-', ' ').title()

    # Calculate category stats
    total = len(topics)
    mastered = 0
    learning = 0
    new = 0

    lines = [f"\n### {category_display}\n"]

    # Add topics table
    for topic in topics:
        filepath = topic['file']
        card_data = srs_data['items'].get(filepath)

        emoji, status, tier = get_card_status(card_data)

        # Count for stats
        if tier == 3:
            mastered += 1
        elif tier == 2:
            learning += 1
        elif tier == 0:
            new += 1
        else:
            learning += 1  # tier 1 counts as learning

        # Format the topic line
        question_preview = topic['question'][:80] + '...' if len(topic['question']) > 80 else topic['question']

        # Show review count if any
        review_info = ""
        if card_data and card_data.get('reviews'):
            num_reviews = len(card_data['reviews'])
            avg_score = sum(r['score'] for r in card_data['reviews']) / num_reviews
            review_info = f" `{num_reviews} reviews, avg {avg_score:.1f}/5`"

        topic_link = f"[{topic['name']}]({filepath})"
        lines.append(f"- {emoji} {topic_link}: {question_preview}{review_info}")

    # Add category progress bar at top
    progress_line = generate_progress_bar(mastered, total, width=30)
    lines.insert(1, f"**Progress:** {progress_line} | 🏆 {mastered} | 💪 {learning} | ⭐ {new}\n")

    return '\n'.join(lines)


def generate_overall_stats(srs_data: Dict, sections: Dict) -> str:
    """Generate overall statistics section"""
    stats = srs_data.get('stats', {})

    # Count all cards by status
    total_cards = 0
    mastered = 0
    learning = 0
    new = 0

    for section_name, topics_by_category in sections.items():
        for topics in topics_by_category.values():
            total_cards += len(topics)
            for topic in topics:
                filepath = topic['file']
                card_data = srs_data['items'].get(filepath)
                _, _, tier = get_card_status(card_data)

                if tier == 3:
                    mastered += 1
                elif tier == 2:
                    learning += 1
                elif tier == 0:
                    new += 1
                else:
                    learning += 1

    lines = []
    lines.append("## Progress Scorecard\n")

    # Overall mastery progress
    progress_bar = generate_progress_bar(mastered, total_cards, width=40)
    lines.append(f"### Overall Mastery\n")
    lines.append(f"```")
    lines.append(f"{progress_bar}")
    lines.append(f"```\n")

    # Breakdown
    lines.append(f"### Card Status\n")
    lines.append(f"| Status | Count | Percentage |")
    lines.append(f"|--------|-------|------------|")

    def pct(count):
        return f"{(count/total_cards*100):.1f}%" if total_cards > 0 else "0%"

    lines.append(f"| 🏆 Mastered | {mastered} | {pct(mastered)} |")
    lines.append(f"| 💪 Learning | {learning} | {pct(learning)} |")
    lines.append(f"| ⭐ New | {new} | {pct(new)} |")
    lines.append(f"| **Total** | **{total_cards}** | **100%** |\n")

    # Review stats
    if stats:
        lines.append(f"### Study Statistics\n")
        lines.append(f"- Total Reviews: **{stats.get('total_reviews', 0)}**")
        lines.append(f"- Current Streak: **{stats.get('current_streak', 0)} days**")
        lines.append(f"- Best Streak: **{stats.get('best_streak', 0)} days**")
        lines.append(f"- Total XP: **{stats.get('xp', 0)}**")

        # Calculate level
        xp = stats.get('xp', 0)
        level = xp // 1000 + 1
        xp_to_next = 1000 - (xp % 1000)
        lines.append(f"- Level: **{level}** ({xp_to_next} XP to next level)")

        # Last reviewed
        if stats.get('last_review_date'):
            lines.append(f"- Last Review: **{stats.get('last_review_date')}**")

    lines.append("")

    return '\n'.join(lines)


def generate_readme():
    """Generate the complete README"""
    srs_data = load_srs_data()
    sections = parse_topic_structure()

    lines = []

    # Header
    lines.append("# ML Interview Dojo\n")
    lines.append("Personal repository for preparing for machine learning interviews.\n")

    # Source material
    lines.append("## Source Material\n")
    lines.append("ML questions are from [Machine Learning Interviews Book](https://huyenchip.com/ml-interviews-book/) by Chip Huyen.")
    lines.append("Math & Quant questions are curated for market-making and quant-adjacent roles.\n")

    # Overall stats
    lines.append(generate_overall_stats(srs_data, sections))

    # Quick start
    lines.append("## Quick Start\n")
    lines.append("```bash")
    lines.append("# Start a review session")
    lines.append("python3 srs.py review")
    lines.append("")
    lines.append("# View your stats")
    lines.append("python3 srs.py stats")
    lines.append("")
    lines.append("# Update this README")
    lines.append("python3 scripts/generate_readme.py")
    lines.append("```\n")

    # How it works
    lines.append("## How the SRS Works\n")
    lines.append("This uses a **queue-based spaced repetition system** (not date-based like Anki):\n")
    lines.append("- **No due dates**: Cards are prioritized in a smart queue based on performance")
    lines.append("- **No pile-up**: Come back after months and continue right where you left off")
    lines.append("- **Adaptive**: Struggles with a card? It gets higher priority automatically")
    lines.append("- **Mastery tracking**: Cards graduate from New → Learning → Mastered\n")
    lines.append("**Mastery Criteria**: 3+ consecutive reviews with score ≥4, spaced at least 1 hour apart\n")

    # Status legend
    lines.append("## Status Legend\n")
    lines.append("- 🏆 **Mastered**: Consistently perfect recall")
    lines.append("- 💪 **Strong**: Average score ≥4.0, still in practice")
    lines.append("- 👍 **Learning**: Average score ≥3.0, making progress")
    lines.append("- 📖 **Practicing**: Reviewed but needs more work")
    lines.append("- ⭐ **New**: Not yet reviewed\n")

    # Generate each section
    for section_name in sorted(sections.keys()):
        topics_by_category = sections[section_name]
        lines.append(f"## {section_name}\n")

        for category in sorted(topics_by_category.keys()):
            topics = topics_by_category[category]
            lines.append(generate_category_section(category, topics, srs_data))

    # Footer
    lines.append("\n---")
    lines.append(f"\n*Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")
    lines.append(f"\n*Generated by [scripts/generate_readme.py](scripts/generate_readme.py)*")

    return '\n'.join(lines)


def main():
    readme_content = generate_readme()

    # Write to README.md
    with open('README.md', 'w') as f:
        f.write(readme_content)

    print("✅ README.md generated successfully!")
    print("📝 Run 'python3 srs.py stats' to see your live progress")


if __name__ == '__main__':
    main()
