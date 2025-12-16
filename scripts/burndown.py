#!/usr/bin/env python3
"""Generate burndown charts for ML Interview Dojo progress tracking.

Two burndowns:
1. Stability: Subsections remaining to stabilize -> target 0 by Jan 15
2. Mastery: Cards in stable subsections needing mastery -> target 0 by Jan 31
"""

from datetime import date, datetime, timedelta
from pathlib import Path
import yaml
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


# Configuration
START_DATE = date(2025, 12, 16)
STABILITY_TARGET_DATE = date(2026, 1, 15)
MASTERY_TARGET_DATE = date(2026, 1, 31)

# All 36 subsections
ALL_SUBSECTIONS = [
    "01-core-ml/01-ml-basics",
    "01-core-ml/02-linear-regression",
    "01-core-ml/03-logistic-regression",
    "01-core-ml/04-cross-entropy",
    "01-core-ml/05-regularization",
    "02-model-evaluation/01-classification-metrics",
    "02-model-evaluation/02-regression-metrics",
    "02-model-evaluation/03-validation",
    "02-model-evaluation/04-model-selection",
    "02-model-evaluation/05-loss-functions",
    "03-deep-learning/01-neural-network-basics",
    "03-deep-learning/02-optimizers",
    "03-deep-learning/03-regularization",
    "03-deep-learning/04-cnns",
    "03-deep-learning/05-rnns",
    "03-deep-learning/06-transformers",
    "04-statistics/01-probability-basics",
    "04-statistics/02-distributions",
    "04-statistics/03-descriptive-stats",
    "04-statistics/04-statistical-inference",
    "04-statistics/05-mle-estimators",
    "05-reinforcement-learning/01-core-concepts",
    "05-reinforcement-learning/02-algorithms",
    "05-reinforcement-learning/03-exploration-exploitation",
    "06-classical-ml/01-decision-trees",
    "06-classical-ml/02-svm",
    "06-classical-ml/03-knn",
    "06-classical-ml/04-naive-bayes",
    "06-classical-ml/05-clustering",
    "06-classical-ml/06-dimensionality-reduction",
    "07-mathematics/01-linear-algebra",
    "07-mathematics/02-calculus-optimization",
    "08-data-engineering/01-feature-engineering",
    "08-data-engineering/02-missing-data",
    "08-data-engineering/03-imbalanced-data",
    "08-data-engineering/04-text-processing",
]

TOTAL_SUBSECTIONS = len(ALL_SUBSECTIONS)


def get_tier(attempt):
    """Calculate tier from attempt data."""
    recall = attempt.get('recall', attempt.get('recall_quality', 'none'))
    if recall == 'partial':
        recall = 'partial-'
    tier_map = {
        'none': 0,
        'partial-': 1,
        'partial+': 2,
        'full': 3,
    }
    return tier_map.get(recall, 0)


def get_current_tier(flashcard_data):
    """Get tier from most recent attempt (not best)."""
    attempts = flashcard_data.get('attempts', [])
    if not attempts:
        return None
    return get_tier(attempts[0])


def is_mastered(flashcard_data):
    """Check if card is mastered (most recent attempt is partial+ or full)."""
    tier = get_current_tier(flashcard_data)
    return tier is not None and tier >= 2


def get_subsection_from_path(file_path):
    """Extract subsection identifier from file path.

    e.g., 'ml-rapid-fire/01-core-ml/01-ml-basics/01-what-is-ml.md'
          -> '01-core-ml/01-ml-basics'
    """
    parts = file_path.split('/')
    if len(parts) >= 3 and parts[0] == 'ml-rapid-fire':
        return f"{parts[1]}/{parts[2]}"
    return None


def calculate_burndown_stats(data, as_of_date=None):
    """Calculate burndown statistics.

    Returns dict with:
    - subsections_remaining: count of unstable subsections
    - cards_needing_mastery: cards in stable subsections not yet mastered
    - cards_in_stable: total cards in stable subsections
    - stable_subsections: list of stable subsection names
    """
    stability = data.get('stability', {})
    flashcards = data.get('flashcards', {})

    # Count stable subsections
    stable_subsections = []
    for subsection in ALL_SUBSECTIONS:
        sub_data = stability.get(subsection, {})
        if sub_data.get('stable', False):
            # Check if it was stable as of as_of_date
            stable_date_str = sub_data.get('stable_date')
            if stable_date_str and as_of_date:
                stable_date = datetime.fromisoformat(stable_date_str).date()
                if stable_date <= as_of_date:
                    stable_subsections.append(subsection)
            elif not as_of_date:
                stable_subsections.append(subsection)

    subsections_remaining = TOTAL_SUBSECTIONS - len(stable_subsections)

    # Count cards in stable subsections needing mastery
    cards_in_stable = 0
    cards_needing_mastery = 0

    for file_path, card_data in flashcards.items():
        subsection = get_subsection_from_path(file_path)
        if subsection in stable_subsections:
            cards_in_stable += 1
            if not is_mastered(card_data):
                cards_needing_mastery += 1

    return {
        'subsections_remaining': subsections_remaining,
        'cards_needing_mastery': cards_needing_mastery,
        'cards_in_stable': cards_in_stable,
        'stable_subsections': stable_subsections,
    }


def calculate_historical_stats(data, start_date, end_date):
    """Calculate burndown stats for each day from start_date to end_date.

    Returns list of (date, subsections_remaining, cards_needing_mastery) tuples.
    """
    burndown_data = data.get('burndown', {})
    history = burndown_data.get('history', [])

    # Build lookup from history
    history_lookup = {}
    for entry in history:
        entry_date = datetime.fromisoformat(entry['date']).date()
        history_lookup[entry_date] = entry

    result = []
    current_date = start_date
    while current_date <= end_date:
        if current_date in history_lookup:
            entry = history_lookup[current_date]
            result.append((
                current_date,
                entry.get('subsections_remaining', TOTAL_SUBSECTIONS),
                entry.get('cards_needing_mastery', 0),
            ))
        else:
            # No data for this date, use current stats
            stats = calculate_burndown_stats(data, as_of_date=current_date)
            result.append((
                current_date,
                stats['subsections_remaining'],
                stats['cards_needing_mastery'],
            ))
        current_date += timedelta(days=1)

    return result


def calculate_ahead_behind(current_remaining, start_remaining, start_date, target_date):
    """Calculate how many items ahead/behind schedule.

    Positive = ahead, negative = behind.
    """
    today = date.today()

    if today >= target_date:
        return -current_remaining if current_remaining > 0 else 0

    total_days = (target_date - start_date).days
    days_elapsed = (today - start_date).days

    if total_days <= 0:
        return 0

    # Expected remaining by END of today
    daily_rate = start_remaining / total_days
    expected_remaining = start_remaining - (daily_rate * (days_elapsed + 1))

    return expected_remaining - current_remaining


def generate_staircase_target(start_remaining, start_date, target_date):
    """Generate staircase target line coordinates."""
    total_days = (target_date - start_date).days
    if total_days <= 0:
        return [start_date], [start_remaining]

    daily_rate = start_remaining / total_days

    dates = []
    values = []

    # First point
    dates.append(start_date)
    values.append(start_remaining)

    for day_offset in range(total_days):
        current_date = start_date + timedelta(days=day_offset)
        next_date = current_date + timedelta(days=1)

        target_value = start_remaining - (daily_rate * (day_offset + 1))
        target_value = max(0, target_value)

        dates.append(current_date)
        values.append(target_value)

        dates.append(next_date)
        values.append(target_value)

    return dates, values


def generate_burndown_chart(stats, output_path, data=None):
    """Generate matplotlib burndown chart with two subplots."""
    today = date.today()

    # Get historical data
    history = []
    if data is not None:
        history = calculate_historical_stats(data, START_DATE, today)

    # Get burndown config for starting values
    burndown_config = data.get('burndown', {}) if data else {}

    # Starting values
    start_subsections = burndown_config.get('start_subsections_remaining', TOTAL_SUBSECTIONS)
    start_mastery = burndown_config.get('start_cards_needing_mastery', 0)

    # Create figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    fig.suptitle('ML Interview Dojo - Burndown Progress', fontsize=14, fontweight='bold')

    # --- Stability Burndown ---
    stab_current = stats['subsections_remaining']

    stab_target_dates, stab_target_values = generate_staircase_target(
        start_subsections, START_DATE, STABILITY_TARGET_DATE
    )

    ax1.plot(stab_target_dates, stab_target_values, 'b--', linewidth=2, label='Target', alpha=0.7)

    if history:
        hist_dates = [h[0] for h in history]
        hist_stability = [h[1] for h in history]
        ax1.plot(hist_dates, hist_stability, 'g-', linewidth=2, alpha=0.7)
        ax1.scatter(hist_dates, hist_stability, color='green', s=100, zorder=5,
                    edgecolors='darkgreen', linewidths=2, label='Actual')
    else:
        ax1.scatter([today], [stab_current], color='green', s=150, zorder=5,
                    edgecolors='darkgreen', linewidths=2, label='Actual')

    stab_ahead = calculate_ahead_behind(stab_current, start_subsections, START_DATE, STABILITY_TARGET_DATE)
    stab_status = f"+{stab_ahead:.1f} ahead" if stab_ahead >= 0 else f"{stab_ahead:.1f} behind"

    ax1.set_title(f'Stability ({TOTAL_SUBSECTIONS} subsections)\n{stab_status}', fontsize=12)
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Subsections Remaining')
    ax1.set_ylim(bottom=0, top=start_subsections + 2)
    ax1.set_xlim(START_DATE - timedelta(days=1), STABILITY_TARGET_DATE + timedelta(days=1))
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
    ax1.xaxis.set_major_locator(mdates.DayLocator(interval=5))
    ax1.legend(loc='upper right')
    ax1.grid(True, alpha=0.3)
    ax1.axhline(y=0, color='black', linestyle='-', linewidth=0.5)

    ax1.annotate(f'{stab_current}', (today, stab_current), textcoords="offset points",
                 xytext=(10, 5), fontsize=10, fontweight='bold', color='green')

    # --- Mastery Burndown ---
    mast_current = stats['cards_needing_mastery']

    # Only show mastery burndown if there are cards in stable subsections
    if start_mastery > 0 or mast_current > 0:
        mast_target_dates, mast_target_values = generate_staircase_target(
            start_mastery, START_DATE, MASTERY_TARGET_DATE
        )

        ax2.plot(mast_target_dates, mast_target_values, 'b--', linewidth=2, label='Target', alpha=0.7)

        if history:
            hist_dates = [h[0] for h in history]
            hist_mastery = [h[2] for h in history]
            ax2.plot(hist_dates, hist_mastery, 'g-', linewidth=2, alpha=0.7)
            ax2.scatter(hist_dates, hist_mastery, color='green', s=100, zorder=5,
                        edgecolors='darkgreen', linewidths=2, label='Actual')
        else:
            ax2.scatter([today], [mast_current], color='green', s=150, zorder=5,
                        edgecolors='darkgreen', linewidths=2, label='Actual')

        mast_ahead = calculate_ahead_behind(mast_current, start_mastery, START_DATE, MASTERY_TARGET_DATE)
        mast_status = f"+{mast_ahead:.1f} ahead" if mast_ahead >= 0 else f"{mast_ahead:.1f} behind"

        ax2.set_title(f'Mastery (cards in stable subsections)\n{mast_status}', fontsize=12)
        y_max = max(start_mastery, mast_current) + 5 if max(start_mastery, mast_current) > 0 else 10
    else:
        ax2.text(0.5, 0.5, 'No stable subsections yet\n\nMark subsections stable to\nstart tracking mastery',
                 ha='center', va='center', transform=ax2.transAxes, fontsize=12, color='gray')
        ax2.set_title('Mastery (cards in stable subsections)', fontsize=12)
        y_max = 10

    ax2.set_xlabel('Date')
    ax2.set_ylabel('Cards Needing Mastery')
    ax2.set_ylim(bottom=0, top=y_max)
    ax2.set_xlim(START_DATE - timedelta(days=1), MASTERY_TARGET_DATE + timedelta(days=1))
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
    ax2.xaxis.set_major_locator(mdates.DayLocator(interval=7))
    ax2.legend(loc='upper right')
    ax2.grid(True, alpha=0.3)
    ax2.axhline(y=0, color='black', linestyle='-', linewidth=0.5)

    if mast_current > 0:
        ax2.annotate(f'{mast_current}', (today, mast_current), textcoords="offset points",
                     xytext=(10, 5), fontsize=10, fontweight='bold', color='green')

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

    return {
        'stability_ahead': stab_ahead,
        'mastery_ahead': mast_ahead if start_mastery > 0 else 0,
    }


def generate_burndown_section(stats, burndown_config, chart_path='images/burndown.png'):
    """Generate markdown section for burndown display."""
    today = date.today()

    stability_days = (STABILITY_TARGET_DATE - today).days
    mastery_days = (MASTERY_TARGET_DATE - today).days

    start_subsections = burndown_config.get('start_subsections_remaining', TOTAL_SUBSECTIONS)
    start_mastery = burndown_config.get('start_cards_needing_mastery', 0)

    stab_ahead = calculate_ahead_behind(
        stats['subsections_remaining'], start_subsections, START_DATE, STABILITY_TARGET_DATE
    )

    stab_status = f"**+{stab_ahead:.1f} ahead**" if stab_ahead >= 0 else f"**{stab_ahead:.1f} behind**"

    # Daily rates needed from today
    stab_rate = stats['subsections_remaining'] / stability_days if stability_days > 0 else stats['subsections_remaining']

    lines = [
        '## Burndown Progress',
        '',
        f'![Burndown Chart]({chart_path})',
        '',
        '### Stability',
        '',
        f'| Metric | Value |',
        f'|--------|-------|',
        f'| Remaining | {stats["subsections_remaining"]}/{TOTAL_SUBSECTIONS} subsections |',
        f'| Target Date | Jan 15, 2026 ({stability_days}d) |',
        f'| Rate Needed | {stab_rate:.1f}/day |',
        f'| Status | {stab_status} |',
        '',
    ]

    # Mastery section only if there are stable subsections
    if stats['cards_in_stable'] > 0:
        mast_ahead = calculate_ahead_behind(
            stats['cards_needing_mastery'], start_mastery, START_DATE, MASTERY_TARGET_DATE
        )
        mast_status = f"**+{mast_ahead:.1f} ahead**" if mast_ahead >= 0 else f"**{mast_ahead:.1f} behind**"
        mast_rate = stats['cards_needing_mastery'] / mastery_days if mastery_days > 0 else stats['cards_needing_mastery']

        lines.extend([
            '### Mastery',
            '',
            f'| Metric | Value |',
            f'|--------|-------|',
            f'| Cards in Stable | {stats["cards_in_stable"]} |',
            f'| Needing Mastery | {stats["cards_needing_mastery"]} |',
            f'| Target Date | Jan 31, 2026 ({mastery_days}d) |',
            f'| Rate Needed | {mast_rate:.1f}/day |',
            f'| Status | {mast_status} |',
            '',
        ])
    else:
        lines.extend([
            '### Mastery',
            '',
            '*No stable subsections yet. Mark subsections stable to start tracking mastery.*',
            '',
        ])

    return lines


def get_burndown_stats(progress_file=None):
    """Load progress data and return burndown stats."""
    if progress_file is None:
        repo_root = Path(__file__).parent.parent
        progress_file = repo_root / 'progress.yaml'

    with open(progress_file, 'r') as f:
        data = yaml.safe_load(f)

    return calculate_burndown_stats(data), data


def generate_chart(progress_file=None, output_path=None):
    """Generate the burndown chart image."""
    if progress_file is None:
        repo_root = Path(__file__).parent.parent
        progress_file = repo_root / 'progress.yaml'

    if output_path is None:
        repo_root = Path(__file__).parent.parent
        output_path = repo_root / 'images' / 'burndown.png'

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(progress_file, 'r') as f:
        data = yaml.safe_load(f)

    stats = calculate_burndown_stats(data)
    return generate_burndown_chart(stats, output_path, data=data)


def main():
    """Generate burndown chart and print status."""
    repo_root = Path(__file__).parent.parent
    progress_file = repo_root / 'progress.yaml'
    output_path = repo_root / 'images' / 'burndown.png'

    with open(progress_file, 'r') as f:
        data = yaml.safe_load(f)

    stats = calculate_burndown_stats(data)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    status = generate_burndown_chart(stats, output_path, data=data)

    print(f"Generated: {output_path}")
    print(f"\nStability: {stats['subsections_remaining']}/{TOTAL_SUBSECTIONS} remaining", end="")
    if status['stability_ahead'] >= 0:
        print(f" (+{status['stability_ahead']:.1f} ahead)")
    else:
        print(f" ({status['stability_ahead']:.1f} behind)")

    if stats['cards_in_stable'] > 0:
        print(f"Mastery: {stats['cards_needing_mastery']}/{stats['cards_in_stable']} needing work", end="")
        if status['mastery_ahead'] >= 0:
            print(f" (+{status['mastery_ahead']:.1f} ahead)")
        else:
            print(f" ({status['mastery_ahead']:.1f} behind)")
    else:
        print("Mastery: No stable subsections yet")


if __name__ == '__main__':
    main()
