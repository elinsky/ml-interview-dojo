# PCA Assumptions and Limitations

**Q:** What are the assumptions and limitations of PCA?

**A:**

**Assumptions:**
- **Linear** relationships between features
- Large variance = important information
- Principal components are orthogonal

**Limitations:**
- Cannot capture **nonlinear** relationships
- Sensitive to **feature scaling** — must standardize
- Sensitive to **outliers** (affect covariance)
- Components may be hard to interpret
- Maximizes variance, not class separability (use LDA for that)

**When PCA fails:**
- Data lies on curved manifold (use t-SNE, UMAP)
- Features have different meanings/units (must scale)

---
