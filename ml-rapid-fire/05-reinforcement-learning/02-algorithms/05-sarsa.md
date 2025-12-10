# SARSA

**Q:** What is SARSA and how does it differ from Q-learning?
- Name meaning
- Algorithm
- Comparison to Q-learning

**A:**

- **SARSA**: State-Action-Reward-State-Action
  - Name comes from tuple used in update: (S, A, R, S', A')
- **Algorithm**:
  1. Initialize Q(s,a) arbitrarily
  2. Choose a from s using policy (e.g., ε-greedy)
  3. For each step:
     - Take action a, observe r, s'
     - Choose a' from s' using policy
     - Q(s,a) ← Q(s,a) + α[r + γQ(s',a') - Q(s,a)]
     - s ← s', a ← a'
- **Comparison to Q-learning**:
  - SARSA: uses Q(s',a') where a' is actual next action (on-policy)
  - Q-learning: uses max_a' Q(s',a') (off-policy)
  - SARSA is more conservative — learns policy it's actually following
- **When SARSA preferred**: when exploration matters (cliff walking example)

---
