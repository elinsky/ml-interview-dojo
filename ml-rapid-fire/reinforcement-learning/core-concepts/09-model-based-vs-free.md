# Model-Based vs Model-Free RL

**Q:** What's the difference between model-based and model-free RL?
- Model-based
- Model-free
- Trade-offs

**A:**

- **Model-based**:
  - Learn or use model of environment: P(s'|s,a), R(s,a)
  - Can plan ahead (simulate trajectories)
  - Examples: Dyna-Q, AlphaGo (MCTS)
- **Model-free**:
  - Learn value function or policy directly from experience
  - No explicit model of dynamics
  - Examples: Q-learning, SARSA, policy gradients
- **Trade-offs**:
  - Model-based: more sample efficient (plan without acting), but model errors compound
  - Model-free: simpler, no model bias, but needs more samples
- **Hybrid approaches**: learn model and use for planning + model-free learning
- **When to use**:
  - Model-based: when dynamics are simple or learnable, sample expensive
  - Model-free: complex dynamics, cheap simulation

---
