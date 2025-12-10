# Clustering Algorithm Comparison

**Q:** When would you use k-means vs DBSCAN vs hierarchical clustering?

**A:**

**K-means:**
- Large datasets (scales well)
- Spherical, similar-sized clusters expected
- Know k in advance
- Fast and simple

**DBSCAN:**
- Arbitrary-shaped clusters
- Unknown number of clusters
- Need to detect outliers
- Clusters have similar density

**Hierarchical:**
- Small to medium datasets
- Want to explore cluster relationships
- Need flexibility in choosing k after clustering
- Interpretability important (dendrograms)

**Similarity metrics:**
- **Euclidean** for compact, spherical clusters
- **Cosine/Manhattan** for irregular structures

**General tips**: always scale features, try multiple algorithms, visualize results

---
