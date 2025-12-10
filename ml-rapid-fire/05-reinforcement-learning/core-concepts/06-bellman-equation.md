# Bellman Equation

**Q:** What is the Bellman equation and why is it fundamental to RL?
- Bellman expectation equation
- Bellman optimality equation
- Why fundamental

**A:**

- **Bellman expectation equation** (for policy π):
  - V^π(s) = Σ_a π(a|s) Σ_{s'} P(s'|s,a)[R(s,a,s') + γV^π(s')]
  - "Value = immediate reward + discounted future value"
- **Bellman optimality equation**:
  - V*(s) = max_a Σ_{s'} P(s'|s,a)[R(s,a,s') + γV*(s')]
  - Q*(s,a) = Σ_{s'} P(s'|s,a)[R(s,a,s') + γ max_{a'} Q*(s',a')]
- **Why fundamental**:
  - Recursive structure enables dynamic programming
  - Basis for value iteration, policy iteration
  - Q-learning uses Bellman equation as update target
- **Key insight**: optimal value of a state = best action's immediate reward + discounted optimal value of next state

---
