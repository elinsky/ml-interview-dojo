# Weighted KNN

**Q:** What is weighted KNN?

**A:**

- Give **closer neighbors more influence** than distant ones
- Common weight: **1/distance** or **1/distance²**
- Reduces sensitivity to choice of K
- Helps when neighbors have varying distances from query point
- In sklearn: `weights='distance'` instead of `weights='uniform'`
- Can help with imbalanced classes

---
