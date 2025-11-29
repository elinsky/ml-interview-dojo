# The Kernel Trick

**Q:** What is the kernel trick?

**A:**

- Maps data to **higher-dimensional space** where it becomes linearly separable
- **Trick**: compute dot products in high-dim space without explicitly transforming
- K(x, x') = φ(x) · φ(x') — kernel computes inner product directly
- Avoids computational cost of high-dimensional transformation
- Enables non-linear decision boundaries in original space

---
