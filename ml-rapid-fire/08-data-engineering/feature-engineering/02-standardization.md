# Standardization (Z-Score Scaling)

**Q:** What is standardization and when should you use it?
- Formula
- Properties of result
- When to use

**A:**

- **Formula**: z = (x - μ) / σ
- **Result properties**: mean = 0, std = 1
- **When to use**:
  - Data is approximately Gaussian
  - Algorithms assume zero-centered data (PCA, many neural networks)
  - Outliers are meaningful (standardization doesn't bound them)
- **Sklearn**: `StandardScaler`
- **Note**: fit on training data only, transform both train and test

---
