# Monte Carlo Methods

**Q:** How do Monte Carlo methods work in RL?
- Key idea
- Algorithm for Q estimation
- Pros and cons

**A:**

- **Key idea**: estimate values from complete episode returns
  - No bootstrapping — wait until episode ends
  - Average returns over many episodes
- **Algorithm** (first-visit MC for Q):
  1. Generate episode using policy
  2. For each (s,a) first visited in episode:
     - G ← return from that point
     - Q(s,a) ← Q(s,a) + α(G - Q(s,a))
  3. Improve policy (e.g., ε-greedy on Q)
- **Pros**:
  - No model needed (learn from experience)
  - Unbiased estimates (use actual returns)
  - Simple to implement
- **Cons**:
  - High variance (full returns vary a lot)
  - Only for episodic tasks
  - Must wait until episode ends
  - Slow learning (especially long episodes)

---
