# Action-Value Function (Q-function)

**Q:** What is the Q-function and how does it differ from V?
- Definition
- Relationship to V
- Why Q is often preferred

**A:**

- **Q-function** Q^π(s,a):
  - Expected return starting from state s, taking action a, then following π
  - Q^π(s,a) = E_π[G_t | S_t = s, A_t = a]
- **Definition in words**: "how good is it to take action a in state s?"
- **Relationship to V**:
  - V^π(s) = Σ_a π(a|s) Q^π(s,a) — weighted average over actions
  - V^π(s) = Q^π(s, π(s)) for deterministic policy
- **Why Q is often preferred**:
  - Can derive policy directly: π(s) = argmax_a Q(s,a)
  - Don't need to know transition dynamics P(s'|s,a)
  - Model-free methods (Q-learning) learn Q directly
- **Optimal Q-function**: Q*(s,a) = max_π Q^π(s,a)
  - π*(s) = argmax_a Q*(s,a)

---
