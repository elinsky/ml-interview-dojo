# ML Interview Dojo - Setup Guide

## What You've Got

A **queue-based Spaced Repetition System** (SRS) that solves the "pile-up problem" with traditional flashcard apps like Anki.

### Key Features

✅ **No due dates** - Just a smart queue that adapts to your performance
✅ **No pile-up** - Take a 6-month break? Pick up right where you left off
✅ **Gamified** - XP, levels, streaks, mastery tracking
✅ **Auto-updating README** - Live progress tracking in your repo

## Quick Start

### 1. Start Your First Review Session

```bash
python3 srs.py review
```

This will:
- Show you questions from your flashcards
- Ask you to rate your recall (1-5)
- Track your progress automatically
- Update the README when you're done

### 2. Check Your Stats

```bash
python3 srs.py stats
```

Shows your current scorecard with:
- Mastery progress bar
- Card breakdown (New, Learning, Mastered)
- Study streak
- XP and level

### 3. View Progress in README

Just open `README.md` - it updates automatically after each review session!

Or manually update it:

```bash
python3 scripts/generate_readme.py
```

## How It Works

### The Queue Algorithm

Unlike Anki's date-based system, this uses a **priority queue**:

1. **New cards** get medium-high priority
2. **Struggling cards** (low scores) get boosted priority
3. **Time since review** adds gentle upward pressure
4. **Mastered cards** stay in rotation but at very low priority

This means:
- No "200 cards due today" after a break
- Cards you struggle with naturally come up more often
- You always work on what matters most

### Mastery System

Cards progress through stages:

- **⭐ New** → Never reviewed
- **📖 Practicing** → Reviewed, avg score < 3
- **👍 Learning** → Reviewed, avg score ≥ 3
- **💪 Strong** → Reviewed, avg score ≥ 4
- **🏆 Mastered** → 3+ consecutive reviews with score ≥4, spaced 1+ hours apart

### Scoring Guide

When rating your recall:

- **5 - Perfect**: Instant recall, could explain to someone else
- **4 - Good**: Recalled correctly with minor hesitation
- **3 - OK**: Struggled but got it eventually
- **2 - Hard**: Needed the answer, but recognized it
- **1 - Forgot**: Completely blanked

## Files

- `srs.py` - Main SRS engine and CLI
- `scripts/generate_readme.py` - README generator
- `.srs-data.json` - Your review history (auto-created, gitignored)
- `README.md` - Auto-generated progress tracker

## Tips

### Daily Practice

```bash
# Quick morning session (review until you hit 'q')
python3 srs.py review

# Check your streak
python3 srs.py stats
```

### After a Long Break

Just run `python3 srs.py review` - the queue picks up right where you left off. No overwhelming pile of "due" cards!

### Focusing on Weak Areas

The algorithm automatically prioritizes cards you struggle with. Just keep reviewing - the queue adapts to your performance.

### Tracking Progress

The README updates automatically after each session. Perfect for:
- Tracking long-term progress
- GitHub portfolio
- Motivation (watching that progress bar fill!)

## Advanced: Customization

### Adjusting Priority Algorithm

Edit the `calculate_priority()` method in `srs.py`:

```python
def calculate_priority(self) -> float:
    # Tune these factors to your preference
    score_factor = (5 - self.average_score) * 10  # Weight of performance
    time_factor = min(self.hours_since_review / 10, 30)  # Weight of time
    struggle_factor = max(0, (3 - self.consecutive_correct) * 5)  # Weight of struggles
```

### Changing Mastery Criteria

Currently: 3+ consecutive good reviews, 1+ hour apart

Edit in `record_review()`:

```python
if card.consecutive_correct >= 3 and len(card.reviews) >= 5:
    # Change the 3 and the timedelta to adjust mastery criteria
```

## Troubleshooting

**Q: README not updating?**
Run manually: `python3 scripts/generate_readme.py`

**Q: Lost my progress?**
Check if `.srs-data.json` exists. Don't delete it!

**Q: Want to reset a card?**
Edit `.srs-data.json` and remove its entry (or edit the review history)

**Q: Cards in wrong order?**
That's the algorithm! It's adapting to your performance. Trust the queue.

## Philosophy

This system is built on a simple idea: **Learning should adapt to you, not the calendar.**

Traditional SRS systems create artificial deadlines that punish you for taking breaks. This one doesn't. It's a queue, not a schedule. Come back in a week, a month, or a year - the system remembers what you need to work on.

Happy learning! 🚀
