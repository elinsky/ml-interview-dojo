# DBSCAN

**Q:** How does DBSCAN work and when should you use it?

**A:**

- **Density-Based Spatial Clustering of Applications with Noise**
- Parameters: **ε** (epsilon, neighborhood radius), **minPts** (minimum points)
- Point types:
  - **Core point**: ≥ minPts within ε distance
  - **Border point**: within ε of a core point but < minPts neighbors
  - **Noise point**: neither core nor border (outliers)
- Clusters = connected core points + their border points
- **Advantages**: finds arbitrary-shaped clusters, identifies outliers, no need to specify k
- **Disadvantages**: struggles with varying densities, sensitive to ε and minPts
- Time complexity: O(n²) naive, O(n log n) with spatial index

---
