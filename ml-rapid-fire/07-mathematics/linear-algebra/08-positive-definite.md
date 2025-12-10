# Positive Definite Matrices

**Q:** What is a positive definite matrix and why does it matter?
- Definition
- Equivalent conditions
- Examples in ML
- Why it matters

**A:**

- **Definition**: symmetric matrix A where xᵀAx > 0 for all x ≠ 0
- **Equivalent conditions**:
  - All eigenvalues > 0
  - All leading principal minors > 0
  - Unique Cholesky decomposition exists (A = LLᵀ)
- **Examples**: covariance matrices (positive semi-definite), Hessian at local minimum
- **Why it matters**:
  - Convex quadratic forms → unique minimum
  - Guarantees valid covariance/correlation matrices
  - Hessian positive definite → confirmed local minimum

---
