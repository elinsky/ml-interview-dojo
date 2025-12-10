# SGD vs Batch Gradient Descent

**Q:** What's the difference between batch, mini-batch, and stochastic gradient descent?
- Batch GD
- Stochastic GD
- Mini-batch GD

**A:**

- **Batch GD**: use all n samples to compute gradient
  - Accurate gradient, but expensive per step
  - Smooth convergence
- **Stochastic GD (SGD)**: use 1 sample per step
  - Noisy gradient estimate, but cheap per step
  - Can escape local minima; acts as regularization
- **Mini-batch GD**: use batch of b samples (typically 32-256)
  - Balances noise and efficiency
  - Enables GPU parallelism
  - Most common in practice
- **Tradeoff**: smaller batch → more noise, more updates per epoch, potential regularization effect

---
