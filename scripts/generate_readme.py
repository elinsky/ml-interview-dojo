#!/usr/bin/env python3
"""
Generate README.md with progress tracking from progress.yaml
"""

import yaml
from pathlib import Path
from datetime import datetime
from collections import defaultdict

PROGRESS_FILE = Path(__file__).parent.parent / "progress.yaml"
README_FILE = Path(__file__).parent.parent / "README.md"

# Content directories to scan
CONTENT_DIRS = ['ml-rapid-fire']


def load_progress():
    if PROGRESS_FILE.exists():
        with open(PROGRESS_FILE, 'r') as f:
            return yaml.safe_load(f) or {'flashcards': {}}
    return {'flashcards': {}}


def get_tier(attempt):
    """Calculate tier from attempt data"""
    recall = attempt.get('recall_quality', 'none')
    used_hints = attempt.get('used_hints', False)
    looked = attempt.get('looked_at_answer', False)
    time_min = attempt.get('time_minutes', 999)

    if recall == 'none':
        return 0
    elif recall == 'partial' or used_hints or looked:
        return 1
    elif recall == 'full' and not used_hints and not looked:
        if time_min <= 2:
            return 3
        else:
            return 2
    return 0


def get_best_tier(flashcard_data):
    """Get the best tier achieved across all attempts"""
    attempts = flashcard_data.get('attempts', [])
    if not attempts:
        return None
    return max(get_tier(a) for a in attempts)


def get_status(flashcard_data):
    """Returns (emoji, status_text, tier)"""
    tier = get_best_tier(flashcard_data)
    if tier is None:
        return '⭐', 'New', -1
    tier_info = {
        0: ('☑️', 'Attempted'),
        1: ('👍', 'Recalled'),
        2: ('💪', 'Independent'),
        3: ('🏆', 'Mastered'),
    }
    emoji, text = tier_info.get(tier, ('⭐', 'New'))
    return emoji, text, tier


def scan_flashcards():
    """Scan ml-rapid-fire for all PDF and markdown flashcards"""
    flashcards_by_category = defaultdict(list)

    for base_dir in CONTENT_DIRS:
        base_path = Path(base_dir)
        if not base_path.exists():
            continue

        for category_dir in sorted(base_path.iterdir()):
            if not category_dir.is_dir():
                continue

            category = category_dir.name

            # Scan PDFs directly in category
            for pdf_file in sorted(category_dir.glob('*.pdf')):
                flashcards_by_category[category].append({
                    'file': str(pdf_file),
                    'name': pdf_file.stem.replace('_', ' '),
                })

            # Scan subdirectories for markdown files (e.g., logistic-regression/*.md)
            for subdir in sorted(category_dir.iterdir()):
                if subdir.is_dir():
                    for md_file in sorted(subdir.glob('*.md')):
                        flashcards_by_category[category].append({
                            'file': str(md_file),
                            'name': md_file.stem.replace('-', ' ').replace('_', ' '),
                            'topic': subdir.name,
                        })

    return flashcards_by_category


def generate_progress_bar(current, total, width=30):
    if total == 0:
        filled = 0
    else:
        filled = int(width * current / total)
    bar = '█' * filled + '░' * (width - filled)
    pct = (current / total * 100) if total > 0 else 0
    return f"[{bar}] {pct:.1f}%"


def generate_readme():
    progress = load_progress()
    flashcards_by_category = scan_flashcards()

    lines = []

    # Header
    lines.append("# ML Interview Dojo\n")
    lines.append("Personal repository for ML interview prep flashcards.\n")

    # Tier legend
    lines.append("## Tier System\n")
    lines.append("| Tier | Name | Criteria |")
    lines.append("|------|------|----------|")
    lines.append("| 0 | ☑️ Attempted | Tried but couldn't recall |")
    lines.append("| 1 | 👍 Recalled | Partial recall, or used hints/peeked |")
    lines.append("| 2 | 💪 Independent | Full recall, no hints, no peeking |")
    lines.append("| 3 | 🏆 Mastered | Independent + answered in ≤2 min |")
    lines.append("| - | ⭐ New | Not yet attempted |")
    lines.append("")

    # Overall stats
    total = 0
    by_tier = {-1: 0, 0: 0, 1: 0, 2: 0, 3: 0}

    for category, cards in flashcards_by_category.items():
        for card in cards:
            total += 1
            card_data = progress['flashcards'].get(card['file'])
            if card_data:
                tier = get_best_tier(card_data)
                by_tier[tier if tier is not None else -1] += 1
            else:
                by_tier[-1] += 1

    mastered = by_tier[3]
    independent = by_tier[2]
    recalled = by_tier[1]
    attempted = by_tier[0]
    new = by_tier[-1]

    lines.append("## Progress Summary\n")
    lines.append(f"**Mastery Progress:** {generate_progress_bar(mastered, total)} ({mastered}/{total})\n")
    lines.append("| Status | Count |")
    lines.append("|--------|-------|")
    lines.append(f"| 🏆 Mastered | {mastered} |")
    lines.append(f"| 💪 Independent | {independent} |")
    lines.append(f"| 👍 Recalled | {recalled} |")
    lines.append(f"| ☑️ Attempted | {attempted} |")
    lines.append(f"| ⭐ New | {new} |")
    lines.append(f"| **Total** | **{total}** |")
    lines.append("")

    # Quick start
    lines.append("## Quick Start\n")
    lines.append("```bash")
    lines.append("# Log an attempt")
    lines.append('python3 scripts/log_attempt.py --file "ml-rapid-fire/classical-ml/logistic-regression/01-what-is-logistic-regression.md" --time 2 --hints false --looked false --recall full')
    lines.append("")
    lines.append("# Update this README")
    lines.append("python3 scripts/generate_readme.py")
    lines.append("```\n")

    # Flashcards by category
    lines.append("## ML Rapid Fire\n")

    for category in sorted(flashcards_by_category.keys()):
        cards = flashcards_by_category[category]
        category_display = category.replace('-', ' ').title()

        # Category stats
        cat_total = len(cards)
        cat_mastered = 0
        for card in cards:
            card_data = progress['flashcards'].get(card['file'])
            if card_data and get_best_tier(card_data) == 3:
                cat_mastered += 1

        lines.append(f"### {category_display}\n")
        lines.append(f"**Progress:** {generate_progress_bar(cat_mastered, cat_total)} ({cat_mastered}/{cat_total})\n")

        for card in cards:
            card_data = progress['flashcards'].get(card['file'])
            if card_data:
                emoji, status, tier = get_status(card_data)
                attempts = len(card_data.get('attempts', []))
                lines.append(f"- {emoji} [{card['name']}]({card['file']}) `{attempts} attempts`")
            else:
                lines.append(f"- ⭐ [{card['name']}]({card['file']})")

        lines.append("")

    # Footer
    lines.append("---")
    lines.append(f"\n*Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")

    return '\n'.join(lines)


def main():
    readme = generate_readme()
    with open(README_FILE, 'w') as f:
        f.write(readme)
    print("✅ README.md updated!")


if __name__ == '__main__':
    main()
