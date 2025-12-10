# DDPG (Deep Deterministic Policy Gradient)

**Q:** What is DDPG and when do you use it?
- Problem it solves
- Architecture
- Key components

**A:**

- **Problem**: Q-learning requires max over actions — intractable for continuous actions
- **Solution**: deterministic policy μ_θ(s) directly outputs action
  - No need for max: Q(s, μ(s)) gives value of policy
- **Architecture** (actor-critic):
  - Actor: μ_θ(s) → a (deterministic action)
  - Critic: Q_φ(s,a) → value
- **Key components**:
  - Experience replay (like DQN)
  - Target networks for both actor and critic
  - **Soft updates**: θ' ← τθ + (1-τ)θ' (slow tracking, τ ~ 0.001)
  - Exploration: add noise to actions (e.g., Ornstein-Uhlenbeck)
- **When to use**: continuous action spaces (robotics, control)
- **Limitation**: can be brittle, sensitive to hyperparameters

---
