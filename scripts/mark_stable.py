#!/usr/bin/env python3
"""Mark a subsection as stable (or remove stable status).

When a subsection is marked stable:
1. Its cards enter the mastery burndown
2. The burndown target adjusts to include cards needing mastery

Usage:
    # Mark a subsection as stable
    python scripts/mark_stable.py --subsection ml-basics

    # Remove stable status
    python scripts/mark_stable.py --subsection ml-basics --unmark

    # List stable subsections
    python scripts/mark_stable.py --list
"""

import argparse
from datetime import datetime, date
from pathlib import Path
import yaml

from burndown import (
    ALL_SUBSECTIONS, TOTAL_SUBSECTIONS, START_DATE,
    get_subsection_from_path, is_mastered, calculate_burndown_stats
)


PROGRESS_FILE = Path(__file__).parent.parent / "progress.yaml"

# Map short names to full subsection paths
SUBSECTION_ALIASES = {}
for subsection in ALL_SUBSECTIONS:
    short_name = subsection.split('/')[-1].lstrip('0123456789-')
    SUBSECTION_ALIASES[short_name] = subsection
    numbered_name = subsection.split('/')[-1]
    SUBSECTION_ALIASES[numbered_name] = subsection
    SUBSECTION_ALIASES[subsection] = subsection


def load_progress():
    if PROGRESS_FILE.exists():
        with open(PROGRESS_FILE, 'r') as f:
            return yaml.safe_load(f) or {}
    return {}


def save_progress(data):
    with open(PROGRESS_FILE, 'w') as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)


def resolve_subsection(name):
    """Resolve a subsection name/alias to the full path."""
    name_lower = name.lower().replace('_', '-')

    if name_lower in SUBSECTION_ALIASES:
        return SUBSECTION_ALIASES[name_lower]

    for alias, full_path in SUBSECTION_ALIASES.items():
        if name_lower in alias.lower():
            return full_path

    return None


def count_cards_in_subsection(data, subsection):
    """Count total cards and cards needing mastery in a subsection."""
    flashcards = data.get('flashcards', {})

    total = 0
    needing_mastery = 0

    for file_path, card_data in flashcards.items():
        card_subsection = get_subsection_from_path(file_path)
        if card_subsection == subsection:
            total += 1
            if not is_mastered(card_data):
                needing_mastery += 1

    return total, needing_mastery


def list_stable_subsections(data):
    """Print stable subsections."""
    stability = data.get('stability', {})
    flashcards = data.get('flashcards', {})

    stable = []
    for subsection in ALL_SUBSECTIONS:
        sub_data = stability.get(subsection, {})
        if sub_data.get('stable', False):
            total, needing = count_cards_in_subsection(data, subsection)
            stable.append({
                'name': subsection,
                'stable_date': sub_data.get('stable_date', 'Unknown'),
                'total_cards': total,
                'needing_mastery': needing,
            })

    print("\nStable Subsections:")
    print("=" * 80)

    if not stable:
        print("No subsections marked as stable yet.")
    else:
        print(f"{'Subsection':<45} {'Date':<12} {'Cards':<8} {'Need Work':<10}")
        print("-" * 80)
        for s in stable:
            date_str = s['stable_date'][:10] if s['stable_date'] else 'Unknown'
            print(f"{s['name']:<45} {date_str:<12} {s['total_cards']:<8} {s['needing_mastery']:<10}")

        total_cards = sum(s['total_cards'] for s in stable)
        total_needing = sum(s['needing_mastery'] for s in stable)
        print("-" * 80)
        print(f"{'Total':<45} {'':<12} {total_cards:<8} {total_needing:<10}")

    print(f"\n{len(stable)}/{TOTAL_SUBSECTIONS} subsections stable")


def update_burndown_history(data):
    """Add or update today's entry in burndown history."""
    if 'burndown' not in data:
        data['burndown'] = {
            'start_date': START_DATE.isoformat(),
            'stability_target_date': '2025-01-15',
            'mastery_target_date': '2025-01-31',
            'start_subsections_remaining': TOTAL_SUBSECTIONS,
            'start_cards_needing_mastery': 0,
            'history': [],
        }

    stats = calculate_burndown_stats(data)

    today_str = date.today().isoformat()

    # Find or create today's entry
    history = data['burndown'].get('history', [])
    today_entry = None
    for entry in history:
        if entry.get('date', '').startswith(today_str):
            today_entry = entry
            break

    if today_entry:
        today_entry['subsections_remaining'] = stats['subsections_remaining']
        today_entry['cards_needing_mastery'] = stats['cards_needing_mastery']
        today_entry['cards_in_stable'] = stats['cards_in_stable']
    else:
        history.append({
            'date': today_str,
            'subsections_remaining': stats['subsections_remaining'],
            'cards_needing_mastery': stats['cards_needing_mastery'],
            'cards_in_stable': stats['cards_in_stable'],
        })

    data['burndown']['history'] = history


def mark_stable(data, subsection):
    """Mark a subsection as stable."""
    if 'stability' not in data:
        data['stability'] = {}

    if subsection not in data['stability']:
        data['stability'][subsection] = {
            'passes_without_changes': 0,
            'last_pass_date': None,
            'stable': False,
            'stable_date': None,
        }

    sub_data = data['stability'][subsection]

    if sub_data.get('stable', False):
        print(f"{subsection} is already marked as stable.")
        return False

    # Count cards that will enter mastery burndown
    total, needing = count_cards_in_subsection(data, subsection)

    sub_data['stable'] = True
    sub_data['stable_date'] = datetime.now().isoformat()

    print(f"Marked stable: {subsection}")
    print(f"  - {total} cards now in mastery burndown")
    print(f"  - {needing} cards needing mastery")

    # Update burndown config if this increases the mastery target
    if 'burndown' not in data:
        data['burndown'] = {
            'start_date': START_DATE.isoformat(),
            'stability_target_date': '2025-01-15',
            'mastery_target_date': '2025-01-31',
            'start_subsections_remaining': TOTAL_SUBSECTIONS,
            'start_cards_needing_mastery': 0,
            'history': [],
        }

    # Add cards needing mastery to the starting target
    data['burndown']['start_cards_needing_mastery'] = (
        data['burndown'].get('start_cards_needing_mastery', 0) + needing
    )

    update_burndown_history(data)

    return True


def unmark_stable(data, subsection):
    """Remove stable status from a subsection."""
    stability = data.get('stability', {})

    if subsection not in stability:
        print(f"{subsection} is not tracked.")
        return False

    sub_data = stability[subsection]

    if not sub_data.get('stable', False):
        print(f"{subsection} is not marked as stable.")
        return False

    # Count cards that will leave mastery burndown
    total, needing = count_cards_in_subsection(data, subsection)

    sub_data['stable'] = False
    sub_data['stable_date'] = None

    print(f"Unmarked: {subsection}")
    print(f"  - {total} cards removed from mastery burndown")

    # Adjust burndown config
    if 'burndown' in data:
        data['burndown']['start_cards_needing_mastery'] = max(
            0,
            data['burndown'].get('start_cards_needing_mastery', 0) - needing
        )

    update_burndown_history(data)

    return True


def main():
    parser = argparse.ArgumentParser(description='Mark a subsection as stable')
    parser.add_argument('--subsection', '-s', type=str, help='Subsection name (e.g., ml-basics)')
    parser.add_argument('--unmark', '-u', action='store_true', help='Remove stable status')
    parser.add_argument('--list', '-l', action='store_true', help='List stable subsections')

    args = parser.parse_args()

    data = load_progress()

    if args.list:
        list_stable_subsections(data)
        return

    if not args.subsection:
        parser.error("--subsection is required (or use --list)")

    subsection = resolve_subsection(args.subsection)
    if not subsection:
        print(f"Error: Unknown subsection '{args.subsection}'")
        print("\nAvailable subsections:")
        for s in ALL_SUBSECTIONS:
            print(f"  {s.split('/')[-1]}")
        return 1

    if args.unmark:
        if unmark_stable(data, subsection):
            save_progress(data)
            print("Progress saved.")
    else:
        if mark_stable(data, subsection):
            save_progress(data)
            print("Progress saved.")


if __name__ == '__main__':
    main()