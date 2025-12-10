# Filter Methods for Feature Selection

**Q:** What are filter methods for feature selection?
- How they work
- Common techniques
- Pros and cons

**A:**

- **How they work**: score features independently based on statistical measures, select top k or threshold
- **Common techniques**:
  - Correlation with target (Pearson, Spearman)
  - Mutual information
  - Chi-squared test (categorical features)
  - ANOVA F-test (numerical features, categorical target)
  - Variance threshold (remove low-variance features)
- **Pros**: fast, model-agnostic, no overfitting risk
- **Cons**: ignores feature interactions, may select redundant features
- **Sklearn**: `SelectKBest`, `SelectPercentile`, `VarianceThreshold`

---
