# SAC (Soft Actor-Critic)

**Q:** What is SAC and what's "soft" about it?
- Maximum entropy RL
- Objective
- Benefits

**A:**

- **Maximum entropy RL**: augment reward with entropy bonus
  - Encourage exploration by rewarding stochastic policies
  - Objective: maximize reward + entropy: J = E[Σ r_t + α H(π(·|s_t))]
- **"Soft" value functions**:
  - V(s) = E[Q(s,a) - α log π(a|s)]
  - Includes entropy term
- **Benefits**:
  - Better exploration (entropy encourages trying different actions)
  - More robust policies (captures multiple good solutions)
  - Stable learning (entropy regularization)
  - State-of-the-art sample efficiency
- **Architecture**: actor (stochastic policy) + two critics (double Q, reduces overestimation)
- **When to use**: continuous control, robotics — often better than DDPG

---
