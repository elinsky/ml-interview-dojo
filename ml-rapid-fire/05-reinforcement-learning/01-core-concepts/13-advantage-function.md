# Advantage Function

**Q:** What is the advantage function and why is it useful?
- Definition
- Interpretation
- Why useful

**A:**

- **Definition**: A^π(s,a) = Q^π(s,a) - V^π(s)
  - How much better is action a compared to average action in state s?
- **Interpretation**:
  - A > 0: action better than average
  - A < 0: action worse than average
  - A = 0: action is average (or optimal in that state)
- **Why useful**:
  - **Variance reduction** in policy gradients: baseline subtraction
  - **Clearer signal**: compares actions within same state (removes state-dependent variance)
  - E_a[A(s,a)] = 0 by definition
- **In practice**:
  - Don't learn A directly
  - Estimate: A(s,a) ≈ R + γV(s') - V(s) (TD error)
  - Used in A2C, A3C, PPO (actor-critic methods)

---
