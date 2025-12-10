# SVM Pros and Cons

**Q:** What are the pros and cons of SVMs?

**A:**

- **Pros**:
  - Effective in high-dimensional spaces (even when n_features > n_samples)
  - Memory efficient — only stores support vectors
  - Versatile via different kernels
  - Works well with clear margin of separation
- **Cons**:
  - Slow on large datasets: O(n²) to O(n³) training via libsvm
  - **Not scale-invariant** — must standardize features (mean=0, var=1)
  - Requires numeric inputs — categorical must be encoded
  - No native probability outputs (expensive 5-fold CV Platt scaling)
  - Kernel/hyperparameter choice can be tricky
- **Tip**: Use LinearSVC (liblinear) for linear kernels — scales to millions of samples

---
