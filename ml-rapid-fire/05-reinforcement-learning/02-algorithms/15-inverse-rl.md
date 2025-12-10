# Inverse Reinforcement Learning

**Q:** What is inverse RL and when do you use it?
- Problem setup
- Why useful
- Approaches

**A:**

- **Problem setup**: given expert demonstrations, recover reward function
  - Standard RL: given R, find π*
  - Inverse RL: given π*, find R
- **Why useful**:
  - Reward design is hard — learn it from examples
  - Transfer: learned reward generalizes to new situations
  - Understand agent behavior (what were they optimizing?)
- **Approaches**:
  - **MaxEnt IRL**: find reward making expert trajectories most likely
  - **GAIL** (Generative Adversarial IL): discriminator distinguishes expert from agent
  - **AIRL**: recovers transferable reward function
- **Ill-posed problem**: many rewards explain same behavior
  - e.g., R = 0 everywhere makes any policy optimal
- **Finance**: infer trader's utility function from trading history

---
