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

# Display names for categories (when different from kebab-case title)
CATEGORY_DISPLAY_NAMES = {
    "ml-basics": "ML Basics",
    "cnns": "CNNs",
    "rnns": "RNNs",
    "svm": "SVM",
    "knn": "KNN",
}

# Define major sections and their subsections (in display order)
# Maps category names to their parent section
SECTION_STRUCTURE = {
    "Core ML": [
        "ml-basics",
        "linear-regression",
        "logistic-regression",
        "cross-entropy",
        "regularization",
    ],
    "Classical ML": [
        "decision-trees",
        "svm",
        "knn",
        "naive-bayes",
        "clustering",
        "dimensionality-reduction",
    ],
    "Deep Learning": [
        "neural-network-basics",
        "optimizers",
        "cnns",
        "rnns",
        "transformers",
    ],
    "Model Evaluation": [
        "classification-metrics",
        "regression-metrics",
        "validation",
        "model-selection",
        "loss-functions",
    ],
    "Probability & Statistics": [
        "probability-basics",
        "distributions",
        "descriptive-stats",
        "statistical-inference",
        "mle-estimators",
    ],
    "Linear Algebra": [
        "vectors-matrices",
        "eigenvalues-eigenvectors",
        "svd-decomposition",
    ],
    "Calculus & Optimization": [
        "derivatives-gradients",
        "convex-optimization",
        "gradient-descent-variants",
    ],
    "Data Engineering": [
        "feature-engineering",
        "missing-data",
        "imbalanced-data",
        "text-processing",
    ],
    "Reinforcement Learning": [
        "rl-core-concepts",
        "rl-algorithms",
        "exploration-exploitation",
    ],
    "Systems & Production": [
        "ml-ops",
        "scalability",
    ],
    "Information Theory": [
        "entropy",
        "kl-divergence",
    ],
}


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


def get_flashcards_by_category(progress):
    """Group flashcards from progress.yaml by category"""
    flashcards_by_category = defaultdict(list)

    for file_path, data in progress.get('flashcards', {}).items():
        category = data.get('category', 'uncategorized')
        flashcards_by_category[category].append({
            'file': file_path,
            'name': data.get('name', Path(file_path).stem),
            'topic': data.get('topic'),
            'data': data,
        })

    # Sort cards within each category by file path
    for category in flashcards_by_category:
        flashcards_by_category[category].sort(key=lambda x: x['file'])

    return flashcards_by_category


def get_section_for_category(category):
    """Find which major section a category belongs to"""
    for section, categories in SECTION_STRUCTURE.items():
        if category in categories:
            return section
    return None


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
    flashcards_by_category = get_flashcards_by_category(progress)

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
            tier = get_best_tier(card['data'])
            by_tier[tier if tier is not None else -1] += 1

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

    # Group categories by section
    categories_by_section = defaultdict(list)
    uncategorized = []

    for category in flashcards_by_category.keys():
        section = get_section_for_category(category)
        if section:
            categories_by_section[section].append(category)
        else:
            uncategorized.append(category)

    # Flashcards by section
    lines.append("## Flashcards\n")

    first_section = True
    for section in SECTION_STRUCTURE.keys():
        section_categories = categories_by_section.get(section, [])
        if not section_categories:
            continue

        # Add divider between sections (not before first)
        if not first_section:
            lines.append("---\n")
        first_section = False

        # Section header with aggregate stats
        section_total = 0
        section_mastered = 0
        for category in section_categories:
            cards = flashcards_by_category[category]
            section_total += len(cards)
            section_mastered += sum(1 for card in cards if get_best_tier(card['data']) == 3)

        lines.append(f"### {section}\n")
        lines.append(f"**Section Progress:** {generate_progress_bar(section_mastered, section_total)} ({section_mastered}/{section_total})\n")

        # Sort categories by their order in SECTION_STRUCTURE
        section_order = SECTION_STRUCTURE[section]
        sorted_categories = sorted(
            section_categories,
            key=lambda c: section_order.index(c) if c in section_order else 999
        )

        for category in sorted_categories:
            cards = flashcards_by_category[category]
            category_display = CATEGORY_DISPLAY_NAMES.get(category, category.replace('-', ' ').title())

            # Category stats
            cat_total = len(cards)
            cat_mastered = sum(1 for card in cards if get_best_tier(card['data']) == 3)

            lines.append(f"#### {category_display}\n")
            lines.append(f"**Progress:** {generate_progress_bar(cat_mastered, cat_total)} ({cat_mastered}/{cat_total})\n")

            for card in cards:
                emoji, status, tier = get_status(card['data'])
                attempts = len(card['data'].get('attempts', []))
                if attempts > 0:
                    lines.append(f"- {emoji} [{card['name']}]({card['file']}) `{attempts} attempts`")
                else:
                    lines.append(f"- {emoji} [{card['name']}]({card['file']})")

            lines.append("")

    # Handle uncategorized if any
    if uncategorized:
        lines.append("---\n")
        lines.append("### Other\n")
        for category in sorted(uncategorized):
            cards = flashcards_by_category[category]
            category_display = CATEGORY_DISPLAY_NAMES.get(category, category.replace('-', ' ').title())

            cat_total = len(cards)
            cat_mastered = sum(1 for card in cards if get_best_tier(card['data']) == 3)

            lines.append(f"#### {category_display}\n")
            lines.append(f"**Progress:** {generate_progress_bar(cat_mastered, cat_total)} ({cat_mastered}/{cat_total})\n")

            for card in cards:
                emoji, status, tier = get_status(card['data'])
                attempts = len(card['data'].get('attempts', []))
                if attempts > 0:
                    lines.append(f"- {emoji} [{card['name']}]({card['file']}) `{attempts} attempts`")
                else:
                    lines.append(f"- {emoji} [{card['name']}]({card['file']})")

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
