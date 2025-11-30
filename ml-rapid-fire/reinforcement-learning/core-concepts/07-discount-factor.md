# Discount Factor

**Q:** What is the discount factor γ and how does it affect learning?
- Definition
- Why discount
- Effect of γ values

**A:**

- **Definition**: γ ∈ [0,1] weights future rewards
  - G_t = R_{t+1} + γR_{t+2} + γ²R_{t+3} + ...
- **Why discount**:
  - Mathematical: ensures finite return in infinite horizon
  - Practical: immediate rewards more certain than distant
  - Economic: "time value" of rewards (prefer now vs later)
- **Effect of γ values**:
  - γ = 0: myopic, only care about immediate reward
  - γ → 1: far-sighted, value long-term outcomes
  - γ = 1: undiscounted (only for episodic tasks)
- **Trade-offs**:
  - High γ: learns long-term strategies but slower, higher variance
  - Low γ: faster learning but shortsighted
- **Typical values**: 0.9 - 0.99

---
