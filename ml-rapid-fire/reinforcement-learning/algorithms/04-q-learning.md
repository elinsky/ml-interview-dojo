# Q-Learning

**Q:** What is Q-learning and why is it important?
- Algorithm
- Key properties
- Update rule intuition

**A:**

- **Algorithm**:
  1. Initialize Q(s,a) arbitrarily
  2. For each step:
     - Take action a (e.g., ε-greedy), observe r, s'
     - Q(s,a) ← Q(s,a) + α[r + γ max_a' Q(s',a') - Q(s,a)]
     - s ← s'
- **Key properties**:
  - **Off-policy**: learns Q* while following any exploratory policy
  - **Model-free**: learns from experience, no P(s'|s,a) needed
  - **TD method**: updates after each step (bootstraps)
- **Update rule intuition**:
  - Target: r + γ max_a' Q(s',a') (Bellman optimality)
  - Move Q(s,a) toward target
  - α controls step size
- **Convergence**: to Q* given sufficient exploration, decaying α
- **Why important**: foundational algorithm, basis for DQN

---
