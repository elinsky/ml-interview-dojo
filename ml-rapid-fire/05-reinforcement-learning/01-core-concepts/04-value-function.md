# Value Function

**Q:** What is a value function and why is it useful?
- State value V(s)
- Definition
- Why useful

**A:**

- **State value function** V^π(s):
  - Expected return starting from state s, following policy π
  - V^π(s) = E_π[G_t | S_t = s]
  - G_t = R_{t+1} + γR_{t+2} + γ²R_{t+3} + ... (return)
- **Definition in words**: "how good is it to be in this state?"
- **Why useful**:
  - Evaluate policies: compare V^π across policies
  - Improve policies: move toward states with higher value
  - Solve for optimal policy: V* gives value under optimal policy
- **Optimal value function** V*(s):
  - Maximum value achievable from state s
  - V*(s) = max_π V^π(s)
- **Key insight**: if we know V*, we can act optimally by choosing actions leading to highest-value states

---
