# Spectral Theorem (Eigendecomposition)

**Q:** What is the spectral theorem and when does it apply?
- Statement
- When it applies
- Matrix form
- Why it's useful

**A:**

- **Statement**: symmetric matrix A can be decomposed as A = QΛQᵀ where Q = orthogonal eigenvector matrix, Λ = diagonal eigenvalue matrix
- **Applies when**: A is symmetric (real) or Hermitian (complex)
- **Matrix form**: A = Σᵢ λᵢqᵢqᵢᵀ (sum of rank-1 outer products)
- **Why useful**:
  - Powers: Aᵏ = QΛᵏQᵀ (fast computation)
  - Inverse: A⁻¹ = QΛ⁻¹Qᵀ
  - Foundation for PCA (covariance matrix is symmetric)

---
