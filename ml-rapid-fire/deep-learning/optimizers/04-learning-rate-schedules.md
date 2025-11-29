# Learning Rate Schedules

**Q:** What are common learning rate schedules?

**A:**

- **Step decay**: reduce LR by factor every N epochs
- **Exponential decay**: LR = LR_0 * e^(-kt)
- **Cosine annealing**: smooth decrease following cosine curve
- **Warmup**: start low, increase, then decay
- **ReduceLROnPlateau**: reduce when validation loss stalls

---
