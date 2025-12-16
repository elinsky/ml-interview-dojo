#!/usr/bin/env python3
"""Log a stability pass for a subsection.

Usage:
    # Log a pass with no changes (increments counter)
    python scripts/log_stability_pass.py --subsection ml-basics

    # Log a pass with changes (resets counter to 0)
    python scripts/log_stability_pass.py --subsection ml-basics --changes

    # List all subsections and their status
    python scripts/log_stability_pass.py --list
"""

import argparse
from datetime import datetime
from pathlib import Path
import yaml

from burndown import ALL_SUBSECTIONS


PROGRESS_FILE = Path(__file__).parent.parent / "progress.yaml"

# Map short names to full subsection paths
SUBSECTION_ALIASES = {}
for subsection in ALL_SUBSECTIONS:
    # e.g., "01-core-ml/01-ml-basics" -> "ml-basics"
    short_name = subsection.split('/')[-1].lstrip('0123456789-')
    SUBSECTION_ALIASES[short_name] = subsection
    # Also allow the numbered version: "01-ml-basics"
    numbered_name = subsection.split('/')[-1]
    SUBSECTION_ALIASES[numbered_name] = subsection
    # And the full path
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

    # Try exact match first
    if name_lower in SUBSECTION_ALIASES:
        return SUBSECTION_ALIASES[name_lower]

    # Try partial match
    for alias, full_path in SUBSECTION_ALIASES.items():
        if name_lower in alias.lower():
            return full_path

    return None


def list_subsections(data):
    """Print all subsections and their stability status."""
    stability = data.get('stability', {})

    print("\nSubsection Stability Status:")
    print("=" * 70)
    print(f"{'Subsection':<45} {'Passes':<8} {'Stable':<8}")
    print("-" * 70)

    for subsection in ALL_SUBSECTIONS:
        sub_data = stability.get(subsection, {})
        passes = sub_data.get('passes_without_changes', 0)
        is_stable = sub_data.get('stable', False)

        status = "Yes" if is_stable else "No"
        print(f"{subsection:<45} {passes:<8} {status:<8}")

    # Summary
    stable_count = sum(1 for s in ALL_SUBSECTIONS if stability.get(s, {}).get('stable', False))
    print("-" * 70)
    print(f"Total: {stable_count}/{len(ALL_SUBSECTIONS)} stable")


def log_pass(data, subsection, had_changes):
    """Log a stability pass for a subsection."""
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
        print(f"Warning: {subsection} is already marked as stable.")
        print("Use mark_stable.py --unmark to remove stable status first.")
        return False

    if had_changes:
        sub_data['passes_without_changes'] = 0
        print(f"Reset: {subsection} - pass had changes, counter reset to 0")
    else:
        sub_data['passes_without_changes'] = sub_data.get('passes_without_changes', 0) + 1
        passes = sub_data['passes_without_changes']
        print(f"Logged: {subsection} - {passes} pass(es) without changes")

        if passes >= 3:
            print(f"\n{subsection} has 3+ passes without changes!")
            print("Consider marking it stable with:")
            print(f"  python scripts/mark_stable.py --subsection {subsection.split('/')[-1]}")

    sub_data['last_pass_date'] = datetime.now().isoformat()
    return True


def main():
    parser = argparse.ArgumentParser(description='Log a stability pass for a subsection')
    parser.add_argument('--subsection', '-s', type=str, help='Subsection name (e.g., ml-basics)')
    parser.add_argument('--changes', '-c', action='store_true', help='Pass had changes (resets counter)')
    parser.add_argument('--list', '-l', action='store_true', help='List all subsections and status')

    args = parser.parse_args()

    data = load_progress()

    if args.list:
        list_subsections(data)
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

    if log_pass(data, subsection, args.changes):
        save_progress(data)
        print("Progress saved.")


if __name__ == '__main__':
    main()
