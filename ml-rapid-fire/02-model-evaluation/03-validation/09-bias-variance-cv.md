# Bias-Variance in Cross-Validation

**Q:** How does k affect the bias and variance of the CV performance estimate?
- What we're estimating
- Higher k effect on estimate bias (with reason)
- Higher k effect on estimate variance (with reason)
- Typical k values

**A:**

- **Goal**: estimate generalization error of a model trained on full dataset
- **Higher k → lower bias**: each fold trains on (k-1)/k of data, closer to full-data model
- **Higher k → higher variance**: training sets overlap heavily → correlated estimates → averaging helps less
- **Typical values**: k=5 or k=10 balances bias-variance; LOOCV has lowest bias but highest variance

**See also:** [[202101080742 Cross Validation (K-Fold)]]

---
