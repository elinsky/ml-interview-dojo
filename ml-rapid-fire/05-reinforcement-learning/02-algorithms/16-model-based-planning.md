# Model-Based Planning

**Q:** How do model-based methods use learned models for planning?
- Learn model
- Planning approaches
- Trade-offs

**A:**

- **Learn model**: predict next state and reward from (state, action)
  - P_θ(s'|s,a): transition model
  - R_θ(s,a): reward model
  - Can be neural networks
- **Planning approaches**:
  - **Shooting**: sample action sequences, simulate, pick best
  - **MPC** (Model Predictive Control): replan at each step
  - **Dyna**: use model to generate synthetic experience for Q-learning
  - **MCTS** (Monte Carlo Tree Search): tree search with model simulation
- **Trade-offs**:
  - Pro: sample efficient (plan without real interaction)
  - Con: model errors compound over long horizons
  - Con: model may not capture true dynamics
- **AlphaGo/AlphaZero**: MCTS + learned model + neural network value/policy

---
