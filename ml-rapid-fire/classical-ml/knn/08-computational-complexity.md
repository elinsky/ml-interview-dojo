# KNN Computational Complexity

**Q:** What is the computational complexity of KNN?

**A:**

- **Training**: O(1) — just stores data (lazy learning)
- **Prediction (brute force)**: O(n·d) per query — compare to all n samples, d features
- **Space**: O(n·d) — must store entire training set
- Complexity increases with training set size
- **Speedups**:
  - **KD-Tree**: O(d·log n) average case, degrades in high dimensions
  - **Ball Tree**: better for high dimensions than KD-Tree
  - **Stochastic KNN**: sample from training set for very large datasets
  - Approximate nearest neighbors (LSH, Annoy, FAISS)

---
