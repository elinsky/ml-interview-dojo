# PCA vs t-SNE

**Q:** When would you use PCA vs t-SNE?

**A:**

**Use PCA when:**
- Need to reduce dimensions for ML preprocessing
- Want interpretable components
- Need to transform new data
- Data has linear relationships
- Speed is important
- Want to preserve global structure

**Use t-SNE when:**
- Visualization is the goal (2D/3D plots)
- Data has nonlinear structure
- Want to see cluster separation
- Local neighborhood structure matters

**Common pattern**: PCA first (to ~50D), then t-SNE for visualization

**Alternative**: **UMAP** — faster than t-SNE, preserves more global structure

---
