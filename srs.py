#!/usr/bin/env python3
"""
ML Interview Dojo - Queue-based Spaced Repetition System
No due dates, no pile-up. Just a smart queue that adapts to your performance.
"""

import json
import os
import glob
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional
import random


class SRSCard:
    """Represents a single flashcard with its review history"""

    def __init__(self, filepath: str, data: Optional[Dict] = None):
        self.filepath = filepath
        self.reviews = data.get('reviews', []) if data else []
        self.mastered = data.get('mastered', False) if data else False
        self.consecutive_correct = data.get('consecutive_correct', 0) if data else 0
        self.last_reviewed = data.get('last_reviewed') if data else None

    def to_dict(self) -> Dict:
        return {
            'reviews': self.reviews,
            'mastered': self.mastered,
            'consecutive_correct': self.consecutive_correct,
            'last_reviewed': self.last_reviewed
        }

    @property
    def is_new(self) -> bool:
        return len(self.reviews) == 0

    @property
    def average_score(self) -> float:
        if not self.reviews:
            return 0.0
        return sum(r['score'] for r in self.reviews) / len(self.reviews)

    @property
    def hours_since_review(self) -> float:
        if not self.last_reviewed:
            return float('inf')
        last_time = datetime.fromisoformat(self.last_reviewed)
        return (datetime.now() - last_time).total_seconds() / 3600

    def calculate_priority(self) -> float:
        """
        Calculate priority score for queue position.
        Higher score = higher priority (should be reviewed sooner)
        """
        # New cards get medium-high priority
        if self.is_new:
            return 70 + random.uniform(0, 10)  # Randomize to mix them up

        # Mastered cards get very low priority
        if self.mastered:
            return 5 + (self.hours_since_review / 1000)  # Occasional review

        # Cards in learning phase
        base_priority = 50

        # Factor 1: Lower average score = higher priority
        score_factor = (5 - self.average_score) * 10  # 0-50 points

        # Factor 2: Time since last review (gentle curve, not strict)
        # After 24 hours, adds ~10 points. After 168 hours (week), adds ~20 points
        time_factor = min(self.hours_since_review / 10, 30)

        # Factor 3: Struggling cards (low consecutive correct) get boosted
        struggle_factor = max(0, (3 - self.consecutive_correct) * 5)

        priority = base_priority + score_factor + time_factor + struggle_factor

        # Add small random factor to prevent getting stuck in same order
        priority += random.uniform(-2, 2)

        return priority


class MLSRS:
    """Main SRS system controller"""

    # All content directories to scan
    CONTENT_DIRS = [
        'ml-workflows',
        'ml-rapid-fire',
        'math-quant-foundations'
    ]

    def __init__(self):
        self.data_file = Path(".srs-data.json")
        self.cards: Dict[str, SRSCard] = {}
        self.stats = {
            'total_reviews': 0,
            'current_streak': 0,
            'best_streak': 0,
            'xp': 0,
            'last_review_date': None
        }
        self.load_data()
        self.scan_cards()

    def scan_cards(self):
        """Scan for all markdown and PDF files in content directories"""
        for base_dir in self.CONTENT_DIRS:
            base_path = Path(base_dir)
            if not base_path.exists():
                continue

            # Scan for both .md and .pdf files
            for ext in ['*.md', '*.pdf']:
                pattern = str(base_path / "**" / ext)
                all_files = glob.glob(pattern, recursive=True)

                for filepath in all_files:
                    if filepath not in self.cards:
                        self.cards[filepath] = SRSCard(filepath)

    def load_data(self):
        """Load review history from JSON file"""
        if self.data_file.exists():
            with open(self.data_file, 'r') as f:
                data = json.load(f)

                for filepath, card_data in data.get('items', {}).items():
                    self.cards[filepath] = SRSCard(filepath, card_data)

                self.stats = data.get('stats', self.stats)

    def save_data(self):
        """Save review history to JSON file"""
        data = {
            'items': {path: card.to_dict() for path, card in self.cards.items()},
            'stats': self.stats
        }

        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=2)

    def get_next_card(self) -> Optional[SRSCard]:
        """Get the highest priority card from the queue"""
        # Filter out mastered cards unless all cards are mastered
        active_cards = [c for c in self.cards.values() if not c.mastered]

        if not active_cards:
            # All mastered! Pick one for review
            active_cards = list(self.cards.values())

        if not active_cards:
            return None

        # Sort by priority (highest first)
        active_cards.sort(key=lambda c: c.calculate_priority(), reverse=True)

        return active_cards[0]

    def record_review(self, card: SRSCard, score: int):
        """
        Record a review for a card.
        Score: 1 (couldn't recall) to 5 (perfect recall)
        """
        now = datetime.now().isoformat()

        card.reviews.append({
            'timestamp': now,
            'score': score
        })
        card.last_reviewed = now

        # Update consecutive correct counter
        if score >= 4:  # Good recall
            card.consecutive_correct += 1
        else:
            card.consecutive_correct = 0

        # Check for mastery: 3+ consecutive good reviews with increasing gaps
        if card.consecutive_correct >= 3 and len(card.reviews) >= 5:
            # Additional check: reviews should be spread over time
            recent_reviews = card.reviews[-3:]
            times = [datetime.fromisoformat(r['timestamp']) for r in recent_reviews]

            # Check that reviews are at least 1 hour apart
            if all(times[i+1] - times[i] >= timedelta(hours=1) for i in range(len(times)-1)):
                card.mastered = True

        # Update stats
        self.stats['total_reviews'] += 1

        # XP calculation
        xp_gain = score * 10
        if card.mastered and card.consecutive_correct == 3:
            xp_gain += 100  # Mastery bonus!
        self.stats['xp'] += xp_gain

        # Streak tracking
        today = datetime.now().date().isoformat()
        if self.stats.get('last_review_date') == today:
            pass  # Same day, no streak change
        elif self.stats.get('last_review_date'):
            last_date = datetime.fromisoformat(self.stats['last_review_date']).date()
            yesterday = datetime.now().date() - timedelta(days=1)
            if last_date == yesterday:
                self.stats['current_streak'] += 1
                self.stats['best_streak'] = max(self.stats['best_streak'], self.stats['current_streak'])
            else:
                self.stats['current_streak'] = 1
        else:
            self.stats['current_streak'] = 1

        self.stats['last_review_date'] = today

        self.save_data()

        return xp_gain, card.mastered and card.consecutive_correct == 3

    def get_scorecard(self) -> Dict:
        """Generate current progress scorecard"""
        total_cards = len(self.cards)
        mastered_cards = sum(1 for c in self.cards.values() if c.mastered)
        new_cards = sum(1 for c in self.cards.values() if c.is_new)
        learning_cards = total_cards - mastered_cards - new_cards

        return {
            'total': total_cards,
            'mastered': mastered_cards,
            'learning': learning_cards,
            'new': new_cards,
            'mastery_percentage': (mastered_cards / total_cards * 100) if total_cards > 0 else 0,
            'total_reviews': self.stats['total_reviews'],
            'current_streak': self.stats['current_streak'],
            'best_streak': self.stats['best_streak'],
            'xp': self.stats['xp']
        }

    def read_card_content(self, card: SRSCard) -> Dict[str, str]:
        """Read the question and answer from a card file"""
        filepath = Path(card.filepath)

        # Handle PDF files
        if filepath.suffix.lower() == '.pdf':
            # Use filename as question, prompt user to open PDF
            question = filepath.stem.replace('_', ' ').replace('-', ' ')
            return {
                'question': f"[PDF Card] {question}",
                'answer': f"📄 Open the PDF to see the answer:\n   {card.filepath}",
                'filepath': card.filepath,
                'is_pdf': True
            }

        # Handle markdown files
        with open(card.filepath, 'r') as f:
            content = f.read()

        # Simple parser: split on # Question and # Answer
        parts = content.split('# Answer')
        question = parts[0].replace('# Question', '').strip() if parts else ""
        answer = parts[1].strip() if len(parts) > 1 else ""

        return {
            'question': question,
            'answer': answer,
            'filepath': card.filepath,
            'is_pdf': False
        }


def print_scorecard(srs: MLSRS):
    """Display a beautiful scorecard"""
    scorecard = srs.get_scorecard()

    print("\n" + "="*60)
    print("📊 ML INTERVIEW DOJO - SCORECARD")
    print("="*60)

    # Progress bar
    mastery_pct = scorecard['mastery_percentage']
    bar_length = 40
    filled = int(bar_length * mastery_pct / 100)
    bar = "█" * filled + "░" * (bar_length - filled)
    print(f"\n🎯 Mastery Progress: {mastery_pct:.1f}%")
    print(f"   [{bar}]")

    # Card breakdown
    print(f"\n📚 Cards:")
    print(f"   ✅ Mastered: {scorecard['mastered']}/{scorecard['total']}")
    print(f"   📖 Learning: {scorecard['learning']}")
    print(f"   ⭐ New: {scorecard['new']}")

    # Stats
    print(f"\n📈 Stats:")
    print(f"   🔄 Total Reviews: {scorecard['total_reviews']}")
    print(f"   🔥 Current Streak: {scorecard['current_streak']} days")
    print(f"   🏆 Best Streak: {scorecard['best_streak']} days")
    print(f"   ⚡ XP: {scorecard['xp']}")

    # Level calculation (just for fun)
    level = scorecard['xp'] // 1000 + 1
    xp_to_next = 1000 - (scorecard['xp'] % 1000)
    print(f"   📊 Level: {level} ({xp_to_next} XP to next level)")

    print("="*60 + "\n")


def update_readme():
    """Update README.md with latest stats"""
    try:
        import subprocess
        result = subprocess.run(
            ['python3', 'scripts/generate_readme.py'],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            print("📝 README.md updated!")
        else:
            print(f"⚠️  Warning: Could not update README: {result.stderr}")
    except Exception as e:
        print(f"⚠️  Warning: Could not update README: {e}")


def interactive_review(srs: MLSRS):
    """Interactive review session"""
    print("\n🎓 Starting review session...")
    print("Rate your recall: 1 (forgot) to 5 (perfect)")
    print("Type 'q' to quit, 's' for scorecard\n")

    reviews_this_session = 0

    while True:
        card = srs.get_next_card()

        if not card:
            print("No cards available!")
            break

        content = srs.read_card_content(card)

        # Show category and status
        category = Path(card.filepath).parent.name
        status = "NEW" if card.is_new else f"Review #{len(card.reviews)+1}"
        if card.mastered:
            status = "MASTERED"

        print(f"\n{'='*60}")
        print(f"📁 Category: {category} | Status: {status}")
        print(f"{'='*60}")

        # Show question
        print(f"\n❓ QUESTION:\n")
        print(content['question'])

        input("\n[Press Enter to reveal answer...]")

        # Show answer
        print(f"\n💡 ANSWER:\n")
        print(content['answer'])

        # Get rating
        while True:
            rating_input = input("\n📝 Rate your recall (1-5, or 'q'/'s'): ").strip().lower()

            if rating_input == 'q':
                print("\n👋 Session complete!")
                print_scorecard(srs)

                # Update README if any reviews were done
                if reviews_this_session > 0:
                    print("\n📊 Updating README with your progress...")
                    update_readme()

                return

            if rating_input == 's':
                print_scorecard(srs)
                continue

            try:
                rating = int(rating_input)
                if 1 <= rating <= 5:
                    break
                else:
                    print("Please enter a number between 1 and 5")
            except ValueError:
                print("Please enter a valid number")

        # Record review
        xp_gain, just_mastered = srs.record_review(card, rating)
        reviews_this_session += 1

        # Feedback
        if just_mastered:
            print(f"\n🎉 MASTERED! +{xp_gain} XP (+100 mastery bonus!)")
        elif rating >= 4:
            print(f"✅ Great! +{xp_gain} XP (Consecutive: {card.consecutive_correct})")
        elif rating == 3:
            print(f"👍 Good! +{xp_gain} XP")
        else:
            print(f"📚 Keep practicing! +{xp_gain} XP")


def main():
    """Main CLI interface"""
    import sys

    srs = MLSRS()

    if len(sys.argv) > 1:
        command = sys.argv[1]

        if command == 'stats':
            print_scorecard(srs)
        elif command == 'review':
            interactive_review(srs)
        else:
            print(f"Unknown command: {command}")
            print("Usage: python srs.py [stats|review]")
    else:
        # Default: start review
        interactive_review(srs)


if __name__ == "__main__":
    main()
