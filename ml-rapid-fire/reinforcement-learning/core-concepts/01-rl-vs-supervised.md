# RL vs Supervised Learning

**Q:** How does reinforcement learning differ from supervised learning?
- Key differences
- What RL learns from
- Unique challenges

**A:**

- **Key differences**:
  - Supervised: learn from labeled examples (input → output)
  - RL: learn from interaction and reward signals
  - No explicit "correct action" in RL — only feedback on how good action was
- **What RL learns from**:
  - Rewards (scalar feedback, possibly delayed)
  - Experience (state, action, reward, next state)
  - Trial and error, not examples
- **Unique RL challenges**:
  - Credit assignment: which action caused the reward?
  - Exploration vs exploitation: try new things vs use what works
  - Non-stationary: agent's policy affects future data
  - Delayed rewards: actions have long-term consequences
- **Finance example**: portfolio optimization — reward is returns, but market reacts to trades

---
