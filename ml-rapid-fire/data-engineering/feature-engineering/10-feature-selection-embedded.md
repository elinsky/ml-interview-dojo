# Embedded Methods for Feature Selection

**Q:** What are embedded methods for feature selection?
- How they work
- Common techniques
- Pros and cons

**A:**

- **How they work**: feature selection built into model training
- **Common techniques**:
  - L1 regularization (Lasso): drives coefficients to exactly zero
  - Tree feature importance: based on split quality improvement
  - ElasticNet: combines L1 and L2
- **Pros**:
  - More efficient than wrappers (single training)
  - Considers feature interactions
  - Less prone to overfitting than wrappers
- **Cons**: model-specific, may not transfer to other models
- **Sklearn**: `SelectFromModel` with L1 or tree-based estimator

---
