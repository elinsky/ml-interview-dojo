# Eigenvalues and Eigenvectors Definition

**Q:** What are eigenvalues and eigenvectors?
- Definition
- Geometric intuition
- How to find them

**A:**

- **Definition**: Av = λv — eigenvector v is only scaled (not rotated) by matrix A; λ is the scaling factor (eigenvalue)
- **Geometric intuition**: eigenvectors are directions that remain unchanged by transformation; eigenvalues tell how much they stretch/shrink
- **Finding them**:
  1. Solve det(A - λI) = 0 for eigenvalues λ (characteristic polynomial)
  2. For each λ, solve (A - λI)v = 0 for eigenvectors
- **Note**: only square matrices have eigenvalues

---
