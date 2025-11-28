#!/usr/bin/env python3
"""
Log a flashcard attempt to progress.yaml
"""

import argparse
import yaml
from datetime import datetime
from pathlib import Path

PROGRESS_FILE = Path(__file__).parent.parent / "progress.yaml"


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
    recall = attempt.get('recall_quality', 'none')
    used_hints = attempt.get('used_hints', False)
    looked = attempt.get('looked_at_answer', False)
    time_min = attempt.get('time_minutes', 999)

    if recall == 'none':
        return 0  # Attempted
    elif recall == 'partial' or used_hints or looked:
        return 1  # Recalled
    elif recall == 'full' and not used_hints and not looked:
        if time_min <= 2:
            return 3  # Mastered
        else:
            return 2  # Independent
    return 0


def get_best_tier(flashcard_data):
    """Get the best tier achieved across all attempts"""
    attempts = flashcard_data.get('attempts', [])
    if not attempts:
        return None
    return max(get_tier(a) for a in attempts)


def log_attempt(file_path, time_minutes, used_hints, looked_at_answer, recall_quality, notes=None):
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
        'time_minutes': time_minutes,
        'used_hints': used_hints,
        'looked_at_answer': looked_at_answer,
        'recall_quality': recall_quality,
    }
    if notes:
        attempt['notes'] = notes

    # Add attempt
    data['flashcards'][file_path]['attempts'].append(attempt)

    # Save
    save_progress(data)

    # Output result
    tier = get_tier(attempt)
    tier_names = {0: 'Attempted ☑️', 1: 'Recalled 👍', 2: 'Independent 💪', 3: 'Mastered 🏆'}
    print(f"Logged: {tier_names[tier]} - {Path(file_path).stem.replace('_', ' ')}")

    return tier


def main():
    parser = argparse.ArgumentParser(description='Log a flashcard attempt')
    parser.add_argument('--file', required=True, help='Path to flashcard file')
    parser.add_argument('--time', type=int, required=True, help='Time in minutes')
    parser.add_argument('--hints', type=lambda x: x.lower() == 'true', required=True, help='Used hints (true/false)')
    parser.add_argument('--looked', type=lambda x: x.lower() == 'true', required=True, help='Looked at answer (true/false)')
    parser.add_argument('--recall', choices=['none', 'partial', 'full'], required=True, help='Recall quality')
    parser.add_argument('--notes', default=None, help='Optional notes')

    args = parser.parse_args()

    log_attempt(
        file_path=args.file,
        time_minutes=args.time,
        used_hints=args.hints,
        looked_at_answer=args.looked,
        recall_quality=args.recall,
        notes=args.notes
    )


if __name__ == '__main__':
    main()
