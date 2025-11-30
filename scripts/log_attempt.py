#!/usr/bin/env python3
"""
Log a flashcard attempt to progress.yaml
"""

import argparse
import yaml
from datetime import datetime
from pathlib import Path

PROGRESS_FILE = Path(__file__).parent.parent / "progress.yaml"

# Tier definitions:
# 0 = none (didn't know)
# 1 = partial- (less than half)
# 2 = partial+ (more than half)
# 3 = full (perfect)

VALID_RECALLS = ['none', 'partial-', 'partial+', 'full']


def load_progress():
    if PROGRESS_FILE.exists():
        with open(PROGRESS_FILE, 'r') as f:
            return yaml.safe_load(f) or {'flashcards': {}}
    return {'flashcards': {}}


def save_progress(data):
    with open(PROGRESS_FILE, 'w') as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)


def get_tier(attempt):
    """Calculate tier from attempt data"""
    recall = attempt.get('recall', 'none')

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


def log_attempt(file_path, recall, notes=None):
    data = load_progress()

    # Normalize file path
    file_path = str(file_path)

    # Create flashcard entry if doesn't exist
    if file_path not in data['flashcards']:
        # Extract name and category from path
        path = Path(file_path)
        name = path.stem.replace('_', ' ')
        category = path.parent.name

        data['flashcards'][file_path] = {
            'name': name,
            'category': category,
            'attempts': []
        }

    # Create attempt
    attempt = {
        'date': datetime.now().isoformat(),
        'recall': recall,
    }
    if notes:
        attempt['notes'] = notes

    # Add attempt
    data['flashcards'][file_path]['attempts'].append(attempt)

    # Save
    save_progress(data)

    # Output result
    tier = get_tier(attempt)
    tier_names = {
        0: '🟠 None',
        1: '🟡 Partial-',
        2: '🔵 Partial+',
        3: '🟢 Full',
    }
    print(f"Logged: {tier_names[tier]} - {Path(file_path).stem.replace('_', ' ')}")

    return tier


def main():
    parser = argparse.ArgumentParser(description='Log a flashcard attempt')
    parser.add_argument('--file', required=True, help='Path to flashcard file')
    parser.add_argument('--recall', choices=VALID_RECALLS, required=True,
                        help='Recall quality: none, partial-, partial+, full')
    parser.add_argument('--notes', default=None, help='Optional notes')

    args = parser.parse_args()

    log_attempt(
        file_path=args.file,
        recall=args.recall,
        notes=args.notes
    )


if __name__ == '__main__':
    main()
