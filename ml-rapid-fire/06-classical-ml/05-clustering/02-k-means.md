# K-Means Clustering

**Q:** How does k-means clustering work?

**A:**

- **Partitioning algorithm** — divides data into k non-overlapping clusters
- **Requires specifying k a priori** (unlike hierarchical)
- Algorithm:
  1. Initialize k cluster centroids (randomly or k-means++)
  2. **Assign** each point to nearest centroid
  3. **Update** centroids to mean of assigned points
  4. Repeat until convergence (assignments don't change)
- Minimizes **inertia**: sum of squared distances to nearest centroid
- Converges to local minimum — sensitive to initialization
- **Standardize features** (StandardScaler) — helps find higher-quality clusters
- Time complexity: O(n · k · d · i) where i = iterations
- Assumes **spherical clusters** of similar size

---
