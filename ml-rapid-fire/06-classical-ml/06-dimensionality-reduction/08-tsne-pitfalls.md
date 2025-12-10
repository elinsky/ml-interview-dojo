# t-SNE Pitfalls

**Q:** What are common pitfalls when using t-SNE?

**A:**

- **Cluster sizes don't mean anything** — t-SNE expands dense clusters
- **Distances between clusters are meaningless** — only local structure preserved
- **Different runs give different results** — stochastic, set random_state
- **Perplexity matters** — try multiple values (5, 30, 50)
- **Can create false clusters** — always verify with other methods
- **Slow on large datasets** — use PCA first to reduce to ~50 dimensions
- **Cannot project new points** — must rerun on full dataset
- **Not for preprocessing** — only for visualization
- Run for enough iterations (default 1000 often not enough)

---
