# Common Matrix Decompositions

**Q:** What are the main matrix decompositions and when do you use each?
- LU decomposition
- Cholesky decomposition
- QR decomposition

**A:**

- **LU**: A = LU (lower × upper triangular)
  - Use: solving linear systems, computing determinants
  - Requires: square matrix, may need pivoting
- **Cholesky**: A = LLᵀ (lower triangular × its transpose)
  - Use: positive definite matrices, faster than LU
  - Requires: symmetric positive definite
  - Application: sampling from multivariate normal
- **QR**: A = QR (orthogonal × upper triangular)
  - Use: least squares, eigenvalue algorithms
  - Works for: any matrix
  - More numerically stable than normal equations

---
