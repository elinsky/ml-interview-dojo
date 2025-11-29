# Momentum

**Q:** How does momentum improve gradient descent?

**A:**

- Accumulates velocity from past gradients
- v = Bv + (1-B)grad, then w = w - a*v
- Helps escape local minima and saddle points
- Reduces oscillation in ravines
- Typical B (beta) = 0.9

---
