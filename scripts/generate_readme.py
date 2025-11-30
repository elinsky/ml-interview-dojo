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
    # Support both old format (recall_quality) and new format (recall)
    recall = attempt.get('recall', attempt.get('recall_quality', 'none'))

    # Map old 'partial' to 'partial-' for backwards compatibility
    if recall == 'partial':
        recall = 'partial-'

    tier_map = {
        'none': 0,
        'partial-': 1,
        'partial+': 2,
        'full': 3,
    }
    return tier_map.get(recall, 0)


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
        return '⚫', 'New', -1
    tier_info = {
        0: ('🟠', 'None'),
        1: ('🟡', 'Partial-'),
        2: ('🔵', 'Partial+'),
        3: ('🟢', 'Full'),
    }
    emoji, text = tier_info.get(tier, ('⚫', 'New'))
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
    lines.append("## Recall Levels\n")
    lines.append("| Level | Criteria |")
    lines.append("|-------|----------|")
    lines.append("| 🟢 Full | Got everything |")
    lines.append("| 🔵 Partial+ | More than half of checklist |")
    lines.append("| 🟡 Partial- | Less than half of checklist |")
    lines.append("| 🟠 None | Didn't know it |")
    lines.append("| ⚫ New | Not yet attempted |")
    lines.append("")

    # Overall stats
    total = 0
    by_tier = {-1: 0, 0: 0, 1: 0, 2: 0, 3: 0}

    for category, cards in flashcards_by_category.items():
        for card in cards:
            total += 1
            tier = get_best_tier(card['data'])
            by_tier[tier if tier is not None else -1] += 1

    full = by_tier[3]
    partial_plus = by_tier[2]
    partial_minus = by_tier[1]
    none_recall = by_tier[0]
    new = by_tier[-1]

    coverage = full + partial_plus + partial_minus + none_recall  # anything attempted
    ready = full + partial_plus  # interview ready

    lines.append("## Progress Summary\n")
    lines.append(f"**Coverage:** {generate_progress_bar(coverage, total)} ({coverage}/{total})\n")
    lines.append(f"**Ready:** {generate_progress_bar(ready, total)} ({ready}/{total})\n")
    lines.append("| Status | Count |")
    lines.append("|--------|-------|")
    lines.append(f"| 🟢 Full | {full} |")
    lines.append(f"| 🔵 Partial+ | {partial_plus} |")
    lines.append(f"| 🟡 Partial- | {partial_minus} |")
    lines.append(f"| 🟠 None | {none_recall} |")
    lines.append(f"| ⚫ New | {new} |")
    lines.append(f"| **Total** | **{total}** |")
    lines.append("")

    # Quick start
    lines.append("## Quick Start\n")
    lines.append("```bash")
    lines.append("# Log an attempt (recall: none, partial-, partial+, full)")
    lines.append('python3 scripts/log_attempt.py --file "ml-rapid-fire/path/to/card.md" --recall full')
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
        section_ready = 0
        section_coverage = 0
        for category in section_categories:
            cards = flashcards_by_category[category]
            section_total += len(cards)
            section_ready += sum(1 for card in cards if get_best_tier(card['data']) is not None and get_best_tier(card['data']) >= 2)
            section_coverage += sum(1 for card in cards if get_best_tier(card['data']) is not None)

        lines.append(f"### {section}\n")
        lines.append(f"**Coverage:** {generate_progress_bar(section_coverage, section_total)} ({section_coverage}/{section_total})\n")
        lines.append(f"**Ready:** {generate_progress_bar(section_ready, section_total)} ({section_ready}/{section_total})\n")

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
            cat_ready = sum(1 for card in cards if get_best_tier(card['data']) is not None and get_best_tier(card['data']) >= 2)
            cat_coverage = sum(1 for card in cards if get_best_tier(card['data']) is not None)

            lines.append(f"#### {category_display}\n")
            lines.append(f"**Coverage:** {generate_progress_bar(cat_coverage, cat_total)} ({cat_coverage}/{cat_total})\n")
            lines.append(f"**Ready:** {generate_progress_bar(cat_ready, cat_total)} ({cat_ready}/{cat_total})\n")

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
            cat_ready = sum(1 for card in cards if get_best_tier(card['data']) is not None and get_best_tier(card['data']) >= 2)
            cat_coverage = sum(1 for card in cards if get_best_tier(card['data']) is not None)

            lines.append(f"#### {category_display}\n")
            lines.append(f"**Coverage:** {generate_progress_bar(cat_coverage, cat_total)} ({cat_coverage}/{cat_total})\n")
            lines.append(f"**Ready:** {generate_progress_bar(cat_ready, cat_total)} ({cat_ready}/{cat_total})\n")

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
