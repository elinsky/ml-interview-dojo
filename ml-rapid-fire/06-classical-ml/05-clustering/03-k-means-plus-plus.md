# K-Means++ Initialization

**Q:** What is k-means++ and why use it?

**A:**

- **Smart initialization** for k-means centroids
- Problem: random initialization can lead to poor local minima
- K-means++ algorithm:
  1. Choose first centroid uniformly at random
  2. For each remaining centroid: choose point with probability proportional to D(x)² (squared distance to nearest existing centroid)
  3. Points far from existing centroids more likely to be chosen
- Spreads initial centroids apart
- **O(log k) competitive** with optimal clustering
- Default in scikit-learn's KMeans

---
