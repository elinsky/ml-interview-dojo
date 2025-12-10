# Return: Episodic vs Continuing Tasks

**Q:** How does the return differ for episodic vs continuing tasks?
- Episodic tasks
- Continuing tasks
- Handling the difference

**A:**

- **Episodic tasks**:
  - Clear end point (terminal state)
  - Return: G_t = R_{t+1} + γR_{t+2} + ... + R_T
  - Finite sum, can use γ = 1
  - Examples: games, navigation to goal
- **Continuing tasks**:
  - No natural end, runs forever
  - Must have γ < 1 (otherwise return infinite)
  - Or use average reward formulation
  - Examples: robot balancing, process control
- **Handling the difference**:
  - Use γ < 1 for both (common in practice)
  - Treat terminal states specially: V(terminal) = 0
  - For continuing: sometimes artificially create episodes (time limits)
- **Finance**: trading is continuing (no natural end), but often divided into episodes (trading days, quarters)

---
