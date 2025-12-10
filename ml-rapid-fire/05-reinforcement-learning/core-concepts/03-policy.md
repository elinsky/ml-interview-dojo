# Policy

**Q:** What is a policy in RL?
- Definition
- Deterministic vs stochastic
- Optimal policy

**A:**

- **Definition**: mapping from states to actions — tells agent what to do
- **Deterministic policy**: π(s) = a
  - Given state s, always take action a
- **Stochastic policy**: π(a|s) = P(a|s)
  - Probability distribution over actions given state
  - Useful for exploration, continuous action spaces
- **Optimal policy** π*:
  - Achieves maximum expected return from any state
  - May not be unique (multiple optimal policies possible)
- **Policy representation**:
  - Tabular: lookup table for discrete states
  - Function approximation: neural network (deep RL)
- **Notation**: π(a|s) for stochastic, π(s) for deterministic

---
