# t-SNE Overview

**Q:** What is t-SNE?

**A:**

- **t-distributed Stochastic Neighbor Embedding**
- **Nonlinear** dimensionality reduction for visualization
- Preserves **local structure** (nearby points stay nearby)
- Converts high-D distances to probabilities, matches in low-D
- Uses **t-distribution** in low-D (heavier tails than Gaussian)
- Excellent for visualizing clusters in 2D/3D
- **Cannot** be used to transform new data (no inverse transform)
- Computationally expensive: O(n²)
- Main parameter: **perplexity** (typical: 5-50)

---
