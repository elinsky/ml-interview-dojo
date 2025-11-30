# Why Class Imbalance Matters

**Q:** Why is class imbalance a problem and when does it matter?
- The problem
- When it matters
- When it doesn't

**A:**

- **The problem**: model can achieve high accuracy by predicting majority class, ignoring minority
  - Example: 99% negative, 1% positive → always predict negative = 99% accuracy, 0% recall
- **When it matters**:
  - Minority class is the class of interest (fraud, disease, default)
  - Cost of false negatives is high
  - Need good recall on minority class
- **When it doesn't**:
  - Both classes equally important
  - Dataset large enough that minority class has sufficient examples
  - Probabilistic predictions matter more than hard classifications
- **Key insight**: the issue isn't imbalance per se, it's that standard metrics and loss functions don't reflect true objectives

---
