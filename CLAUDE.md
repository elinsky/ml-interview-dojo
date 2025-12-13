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
