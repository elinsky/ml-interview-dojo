# Vanishing and Exploding Gradients

**Q:** What are vanishing and exploding gradients?

**A:**

- **Vanishing**: gradients shrink to ~0 in deep networks (early layers don't learn)
- **Exploding**: gradients grow huge, weights become NaN
- Caused by repeated multiplication through layers
- Solutions: ReLU, proper initialization, batch norm, residual connections

---
