# Learning Rate Schedules

**Q:** Why use learning rate schedules and what are common approaches?
- Why schedule
- Common schedules
- Warmup

**A:**

- **Why schedule**: large LR early (fast progress), small LR later (fine-tune, converge)
- **Common schedules**:
  - Step decay: reduce by factor every k epochs (e.g., ×0.1 every 30 epochs)
  - Exponential decay: αₜ = α₀ · γᵗ
  - Cosine annealing: smooth decay following cosine curve
  - 1/t decay: αₜ = α₀ / (1 + kt)
- **Warmup**: start with small LR, gradually increase, then decay
  - Helps with unstable early gradients (especially in transformers)
- **Adaptive methods** (Adam, RMSprop): per-parameter learning rates that adapt automatically

---
