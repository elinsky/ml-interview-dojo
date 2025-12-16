# Development Environment

This project uses pyenv with a virtualenv named `ml-interview-dojo`. The `.python-version` file specifies this.

When running Python scripts, use the virtualenv:
```bash
~/.pyenv/versions/ml-interview-dojo/bin/python scripts/script_name.py
```

---

# Study Plan & Goals

## Timeline
- **Now → Jan 15, 2026**: Get all 36 subsections stable
- **Now → Jan 31, 2026**: Master all cards in stable subsections

## What "Stable" Means
A subsection is stable after 3 passes through it without making any changes to the cards. This ensures card quality is locked in before focusing on mastery.

## Workflow
1. **Stabilize subsections** - Review cards, refine questions/answers until no changes needed for 3 passes
2. **Mark stable** - Once stable, cards enter the mastery burndown
3. **Master cards** - Drill stable cards until all are at partial+ or full recall

---

# Progress Tracking System

## Burndown Charts
Two burndowns track progress toward Jan 31 goals:
1. **Stability** - 36 subsections → 0 (target: Jan 15)
2. **Mastery** - Cards needing work in stable subsections → 0 (target: Jan 31)

## Scripts

### Log a stability pass
After reviewing all cards in a subsection:
```bash
# No changes during pass (increments counter)
~/.pyenv/versions/ml-interview-dojo/bin/python scripts/log_stability_pass.py --subsection ml-basics

# Had changes to cards (resets counter to 0)
~/.pyenv/versions/ml-interview-dojo/bin/python scripts/log_stability_pass.py --subsection ml-basics --changes

# List all subsections and their status
~/.pyenv/versions/ml-interview-dojo/bin/python scripts/log_stability_pass.py --list
```

### Mark a subsection stable
After 3 passes without changes:
```bash
~/.pyenv/versions/ml-interview-dojo/bin/python scripts/mark_stable.py --subsection ml-basics

# List stable subsections
~/.pyenv/versions/ml-interview-dojo/bin/python scripts/mark_stable.py --list

# Remove stable status (if needed)
~/.pyenv/versions/ml-interview-dojo/bin/python scripts/mark_stable.py --subsection ml-basics --unmark
```

### Log a card attempt
```bash
~/.pyenv/versions/ml-interview-dojo/bin/python scripts/log_attempt.py --file "ml-rapid-fire/path/to/card.md" --recall full
```

### Update README with burndown
```bash
~/.pyenv/versions/ml-interview-dojo/bin/python scripts/generate_readme.py
```

## Mastery Definition
- **Mastered** = most recent attempt is partial+ or full
- Cards can regress (if latest attempt is worse, they need work again)

---

# Flashcard Design Principles

## 1. Question guides the answer
- Bullet hints under the question show what a complete answer looks like
- If you want a formula, ask for it explicitly
- Question should make scoring clear (e.g., "4 bullets = 4 things to say")

## 2. Bullets = scoring criteria
- Top-level bullets are graded points
- Sub-bullets are ungraded context/elaboration (helpful during review, not required for full marks)

## 3. Smaller cards > larger cards
- Easier to grade
- Easier to learn to perfect recall
- Split by: definition → formula → properties → when to use/application

## 4. Cards are ordered
- Assume sequential review
- Comparison cards come after both topics are introduced
- Build on prior knowledge

## 5. Right depth for the set
- One card in a larger topic set shouldn't go deeper than others
- Match the level of sibling cards

## 6. No artificial bullet count
- Use as many as needed (1 is fine, 6 is fine)
- But more bullets → consider splitting

## 7. Interview relevance
- Delete cards that are too niche
- Ask: "Would this actually come up in an interview?"

## 8. Consistent terminology
- Use score vs error consistently (and clarify which)
- Match terminology to what interviewers expect

## 9. Formula cards are standalone
- Formulas are hard to recall
- Give them their own card with an explicit "What is the formula for X?" question

## 10. Common card pattern for concepts
- Definition: "What is X?"
- Formula: "What is the formula for X?"
- Properties: "What are the key properties of X?"
- When to use: "When do you use X?"
- How to use: "How do you use X?" or "What are the steps to use X?"

## 11. Simple is good
- Simple questions with straightforward answers are valuable
- Don't assume something is "too obvious" - rusty knowledge needs reinforcement

---

# Quiz Grading

## Grading Scale
| Level | Criteria |
|-------|----------|
| 🟢 Full | Got everything |
| 🔵 Partial+ | More than half of checklist |
| 🟡 Partial- | Less than half of checklist |
| 🟠 None | Didn't know it |
| ⚫ New | Not yet attempted |

## Grading Process
1. Go bullet by bullet, marking each as ✅ made or ❌ missed
2. Propose overall grade based on the scale above
3. Wait for user sign-off before logging the attempt
4. Log the attempt using `scripts/log_attempt.py --file <path> --recall <none|partial-|partial+|full>` after user confirms
5. Audit cards as we go: if a card is too broad, unclear, or doesn't meet the flashcard design principles, propose edits (split, reword, clarify) before continuing
6. At end of session, run `scripts/generate_readme.py` to update the README
