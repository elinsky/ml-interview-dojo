# Reward Design

**Q:** Why is reward design challenging and what can go wrong?
- Importance
- Common pitfalls
- Reward shaping

**A:**

- **Importance**: reward defines the objective — agent optimizes whatever you measure
- **Common pitfalls**:
  - **Sparse rewards**: too rare to learn from (e.g., only reward at goal)
  - **Reward hacking**: agent finds unintended way to maximize reward
  - **Misaligned rewards**: optimizes metric but not true objective
  - Example: robot learns to touch goal flag by falling over
- **Reward shaping**: add intermediate rewards to guide learning
  - Dense rewards easier to learn from
  - Risk: agent may exploit shaped rewards, not solve real task
  - Potential-based shaping preserves optimal policy
- **Finance example**: trading agent — reward = returns? Sharpe? Risk-adjusted returns? Each leads to different behavior

---
