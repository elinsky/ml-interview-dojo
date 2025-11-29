# Hierarchical Clustering

**Q:** What is hierarchical clustering?

**A:**

- Builds a **hierarchy of clusters** (tree structure)
- Result is a **dendrogram** — can cut at any level to get k clusters
- Two approaches:
  - **Agglomerative** (bottom-up): start with each point as cluster, merge pairs
  - **Divisive** (top-down): start with one cluster, recursively split
- Agglomerative is more common
- No need to specify k upfront — choose after seeing dendrogram
- Time complexity: O(n³) naive, O(n² log n) with optimization
- Space complexity: O(n²) for distance matrix
- Good for small datasets, understanding cluster relationships

---
