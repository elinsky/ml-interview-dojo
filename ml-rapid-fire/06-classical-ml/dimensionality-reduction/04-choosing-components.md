# Choosing Number of PCA Components

**Q:** How do you choose the number of principal components?

**A:**

- **Explained variance ratio**: fraction of total variance each PC captures
- **Cumulative explained variance**: sum of variance ratios
- Common threshold: keep components that explain **95%** or **99%** of variance
- **Scree plot**: plot eigenvalues, look for "elbow"
- **Kaiser criterion**: keep components with eigenvalue > 1
- For visualization: use 2 or 3 components
- Trade-off: more components = more information but less compression
- **Experimental approach**: try different n_components with cross-validation, pick best
- scikit-learn: `pca.explained_variance_ratio_`

---
