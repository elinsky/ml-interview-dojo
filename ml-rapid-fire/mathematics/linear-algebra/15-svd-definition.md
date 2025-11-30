# Singular Value Decomposition (SVD)

**Q:** What is SVD and how does it differ from eigendecomposition?
- Formula
- Components explained
- When it applies
- Relationship to eigendecomposition

**A:**

- **Formula**: A = UΣVᵀ for any m×n matrix
  - U (m×m): left singular vectors (orthonormal)
  - Σ (m×n): diagonal with singular values σᵢ ≥ 0
  - V (n×n): right singular vectors (orthonormal)
- **Key difference**: works for ANY matrix (not just square symmetric)
- **Relationship**:
  - AᵀA = VΣ²Vᵀ (eigendecomposition of AᵀA)
  - AAᵀ = UΣ²Uᵀ (eigendecomposition of AAᵀ)
  - Singular values = √(eigenvalues of AᵀA)

---
