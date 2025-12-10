# Simple Imputation Methods

**Q:** What are simple imputation methods and their tradeoffs?
- Mean/median/mode
- Constant value
- Pros and cons

**A:**

- **Mean imputation**: replace with feature mean
  - Preserves mean, but reduces variance
  - Assumes MCAR
- **Median imputation**: replace with feature median
  - More robust to outliers than mean
  - Good for skewed distributions
- **Mode imputation**: replace with most frequent value
  - Use for categorical features
- **Constant value**: replace with fixed value (0, -1, "MISSING")
  - Makes missingness explicit
- **Pros**: simple, fast, easy to implement
- **Cons**: ignores relationships between features, underestimates variance, can bias results if not MCAR
- **Sklearn**: `SimpleImputer`

---
