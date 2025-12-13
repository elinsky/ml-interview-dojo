# Nested Cross-Validation

**Q:** What is nested cross-validation and when is it needed?
- Two-loop structure (what each does)
- Problem it solves
- When to use

**A:**

- **Structure**: CV inside CV
  - Outer loop: estimates unbiased generalization error
  - Inner loop: tunes hyperparameters on each outer training set
- **Problem solved**: single CV for both tuning and evaluation → optimistic bias (hyperparams chosen to work well on validation folds)
- **When to use**: small datasets where you need both tuning AND unbiased performance estimate; rigorous academic evaluation

**See also:** [[202101080742 Cross Validation (K-Fold)]], [[202107270653 Model Selection for Linear Regression]]

---
