# Curse of Dimensionality

**Q:** How does the curse of dimensionality affect KNN?

**A:**

- In high dimensions, **all points become equidistant** — distance loses meaning
- Volume of space grows exponentially; data becomes sparse
- Need exponentially more data to maintain same density
- Nearest neighbor may not be meaningfully "near"
- **Mitigation**: dimensionality reduction (PCA), feature selection
- KNN particularly vulnerable — relies entirely on distance calculations

---
