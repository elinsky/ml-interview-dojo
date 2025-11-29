# Choosing K

**Q:** How do you choose K in KNN?

**A:**

- **Small K** (e.g., 1-3): low bias, high variance → sensitive to noise, overfitting
- **Large K**: high bias, low variance → smoother boundaries, underfitting
- K=1: Voronoi tessellation — each point defines a region
- **Odd K** for even number of classes; **even K** for odd number of classes (avoid ties)
- Typical approach: try K from 1 to 21, use cross-validation
- Common starting point: K = √n (where n = training samples)

---
