# MSE vs MAE

**Q:** When should you use MSE vs MAE?

**A:**

- **MSE**: when large errors are particularly costly
- **MAE**: when outliers should not dominate the metric
- **MSE**: easier to optimize (smooth, differentiable everywhere)
- **MAE**: more interpretable ("average error in units")
- MSE punishes outliers quadratically; MAE treats all errors linearly

---
