# Imitation Learning

**Q:** What is imitation learning and how does it relate to RL?
- Concept
- Behavioral cloning
- Comparison to RL

**A:**

- **Concept**: learn from expert demonstrations instead of rewards
  - Given: trajectories from expert policy
  - Goal: learn policy that mimics expert
- **Behavioral cloning**:
  - Treat as supervised learning: state → action
  - Simple but suffers from distribution shift
  - Small errors compound (agent visits states expert never saw)
- **DAgger** (Dataset Aggregation):
  - Run learned policy, query expert for corrections
  - Aggregate data, retrain
  - Addresses distribution shift
- **Comparison to RL**:
  - No reward needed (learn from examples)
  - Limited by expert's ability
  - Can combine: use demonstrations to initialize RL
- **Applications**: autonomous driving, robotics, game AI

---
