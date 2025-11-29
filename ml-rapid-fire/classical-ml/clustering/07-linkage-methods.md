# Linkage Methods

**Q:** What are the different linkage methods in hierarchical clustering?

**A:**

- Linkage determines distance between clusters for merging
- **Single linkage**: min distance between any pair of points
  - Tends to produce long, chain-like clusters
- **Complete linkage**: max distance between any pair
  - Produces compact, similar-diameter clusters
- **Average linkage**: average distance between all pairs
  - Compromise between single and complete
- **Ward's method**: minimizes variance within merged clusters
  - Produces compact, equal-sized, spherical clusters
  - Most commonly used (default in many implementations)
- Choice affects cluster shape significantly

---
