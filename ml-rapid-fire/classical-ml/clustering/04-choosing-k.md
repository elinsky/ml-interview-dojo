# Choosing K (Number of Clusters)

**Q:** How do you choose the number of clusters k?

**A:**

- **Elbow method**: plot inertia vs k, look for "elbow" where improvement slows
- **Silhouette score**: measures how similar points are to own cluster vs others
  - Range: -1 to 1 (higher is better)
  - s(i) = (b - a) / max(a, b) where a = intra-cluster dist, b = nearest-cluster dist
- **Gap statistic**: compare inertia to null reference distribution
- **Domain knowledge**: sometimes k is given by the problem (e.g., marketing expert)
- **Dendrogram** (hierarchical): cut horizontal line where branches aren't too distanced/concentrated
- **Too few clusters** → not meaningful distinctions
- **Too many clusters** → overfitting, poor generalization
- No universally best method — often subjective

---
