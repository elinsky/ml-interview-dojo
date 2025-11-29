# Distance Metrics

**Q:** What distance metrics are used in KNN?

**A:**

- **Euclidean** (L2): √Σ(xⱼ - xᵢⱼ)² — best when features are similar type (all widths/heights)
- **Manhattan** (L1): Σ|xⱼ - xᵢⱼ| — best when features are different types (age, gender, height)
- **Minkowski**: (Σ|xⱼ - xᵢⱼ|^p)^(1/p) — generalization (p=1: Manhattan, p=2: Euclidean)
- **Hamming**: count of differing bits — for binary/categorical vectors
- **Cosine**: 1 - cos(θ) — angle between vectors, good for text/sparse data
- Others: Mahalanobis, Jaccard, Tanimoto — experiment to find best for your data

---
