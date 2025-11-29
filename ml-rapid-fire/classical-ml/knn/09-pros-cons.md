# KNN Pros and Cons

**Q:** What are the pros and cons of KNN?

**A:**

- **Pros**:
  - Simple to understand and implement
  - No training phase — adapts immediately to new data
  - Non-parametric — no assumptions about functional form
  - Naturally handles multi-class problems
  - Can model complex decision boundaries
- **Cons**:
  - Slow prediction: O(n) per query (without indexing)
  - High memory: must store all training data
  - Sensitive to irrelevant features and feature scaling
  - Suffers from curse of dimensionality
  - Doesn't work well with imbalanced data (majority class dominates)
- **Data prep**: rescale features, handle missing values, reduce dimensionality

---
