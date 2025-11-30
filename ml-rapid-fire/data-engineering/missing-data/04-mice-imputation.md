# MICE (Multiple Imputation by Chained Equations)

**Q:** What is MICE and why is it considered a gold standard?
- Method
- Why "chained equations"
- Why "multiple"

**A:**

- **Method**: iteratively impute each feature using a model trained on other features
  1. Initialize missing values (e.g., mean)
  2. For each feature with missing values, train model on other features, predict missing
  3. Repeat for multiple iterations until convergence
- **Why "chained equations"**: each feature modeled as function of others (chain of conditional distributions)
- **Why "multiple"**: generate M imputed datasets, analyze each, pool results
  - Captures imputation uncertainty
- **Advantages**: handles MAR well, preserves feature relationships, provides uncertainty estimates
- **Disadvantages**: computationally expensive, requires modeling assumptions
- **Sklearn**: `IterativeImputer` (experimental)

---
