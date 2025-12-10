# PCA and Eigenvalues

**Q:** How do eigenvalues connect to PCA?
- What PCA finds
- Role of covariance matrix
- Eigenvalue interpretation

**A:**

- **PCA finds**: directions of maximum variance in data (principal components)
- **Process**: compute covariance matrix Σ → find its eigenvalues/eigenvectors
- **Eigenvectors**: principal component directions (sorted by eigenvalue)
- **Eigenvalues**: variance explained along each principal component
- **Dimensionality reduction**: keep top k eigenvectors (largest eigenvalues) → captures most variance with fewer dimensions
- **Explained variance ratio**: λᵢ / Σⱼλⱼ = fraction of variance explained by component i

---
