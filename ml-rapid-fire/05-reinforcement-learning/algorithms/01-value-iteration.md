# Value Iteration

**Q:** What is value iteration and how does it work?
- Algorithm
- When it applies
- Convergence

**A:**

- **Algorithm** (dynamic programming):
  1. Initialize V(s) arbitrarily
  2. Repeat until convergence:
     - For each state s:
       V(s) ← max_a Σ_{s'} P(s'|s,a)[R(s,a,s') + γV(s')]
  3. Extract policy: π(s) = argmax_a [...]
- **When it applies**:
  - Known model: P(s'|s,a) and R available
  - Discrete, finite state and action spaces
  - Planning, not learning from experience
- **Convergence**:
  - Guaranteed to converge to V*
  - Contraction: error decreases by factor γ each iteration
  - Complexity: O(|S|²|A|) per iteration
- **Limitation**: requires full model, doesn't scale to large state spaces

---
