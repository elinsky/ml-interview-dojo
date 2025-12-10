# Clustering Evaluation

**Q:** How do you evaluate clustering quality without labels?

**A:**

- **Internal metrics** (no ground truth needed):
  - **Silhouette score**: cohesion vs separation (-1 to 1)
  - **Inertia**: within-cluster sum of squares (lower is better)
  - **Davies-Bouldin index**: avg similarity between clusters (lower is better)
  - **Calinski-Harabasz**: ratio of between/within cluster dispersion (higher is better)
- **External metrics** (if ground truth available):
  - **Adjusted Rand Index (ARI)**: similarity to true labels (-1 to 1)
  - **Normalized Mutual Information (NMI)**: shared information (0 to 1)
  - **Homogeneity, Completeness, V-measure**
- Visual inspection often important

---
