# Wrapper Methods for Feature Selection

**Q:** What are wrapper methods for feature selection?
- How they work
- Common techniques
- Pros and cons

**A:**

- **How they work**: use model performance to evaluate feature subsets
- **Common techniques**:
  - Forward selection: start empty, add best feature iteratively
  - Backward elimination: start with all, remove worst iteratively
  - Recursive Feature Elimination (RFE): train model, remove least important, repeat
- **Pros**: considers feature interactions, optimizes for specific model
- **Cons**: computationally expensive (many model fits), risk of overfitting to validation set
- **Sklearn**: `RFE`, `RFECV` (with cross-validation)
- **Complexity**: O(k × n) model fits for forward/backward (k features selected from n)

---
