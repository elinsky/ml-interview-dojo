# Policy Iteration

**Q:** What is policy iteration and how does it differ from value iteration?
- Algorithm
- Policy evaluation
- Policy improvement

**A:**

- **Algorithm**:
  1. Initialize policy π arbitrarily
  2. **Policy evaluation**: compute V^π (solve Bellman equation for current π)
  3. **Policy improvement**: π(s) ← argmax_a Σ P(s'|s,a)[R + γV^π(s')]
  4. Repeat until policy stable
- **Policy evaluation**:
  - Solve system of linear equations, or
  - Iterate: V(s) ← Σ_a π(a|s) Σ_{s'} P(s'|s,a)[R + γV(s')]
- **Policy improvement theorem**: new policy at least as good
- **Comparison to value iteration**:
  - Value iteration: one backup per state, implicit policy
  - Policy iteration: full evaluation, then improvement
  - Policy iteration often fewer iterations, but each more expensive
- **Convergence**: finite number of policies → must converge

---
