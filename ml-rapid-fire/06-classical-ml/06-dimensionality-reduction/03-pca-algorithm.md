# PCA Algorithm

**Q:** How does PCA work mathematically?

**A:**

1. **Center** the data (subtract mean from each feature)
2. Compute **covariance matrix** of centered data
3. Find **eigenvectors** and **eigenvalues** of covariance matrix
4. Sort eigenvectors by eigenvalue (descending)
5. Select top k eigenvectors as principal components
6. **Project** data onto these k components

- Eigenvectors = directions of maximum variance (principal components)
- Eigenvalues = amount of variance in each direction
- Alternatively: use **Singular Value Decomposition (SVD)**
- Must **standardize** features first if scales differ
- scikit-learn: use **Pipeline** to combine scaling + PCA + model
- `Pipeline([('scaler', StandardScaler()), ('pca', PCA(n_components=k)), ('model', LogisticRegression())])`

---
