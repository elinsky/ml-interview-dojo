# PPO (Proximal Policy Optimization)

**Q:** What is PPO and why is it widely used?
- Key idea
- Clipped objective
- Why popular

**A:**

- **Key idea**: improve policy while staying close to old policy
  - Large policy updates can be catastrophic
  - Constrain how much policy can change
- **Clipped objective**:
  - r_t(θ) = π_θ(a|s) / π_old(a|s) (probability ratio)
  - L = min(r_t · A_t, clip(r_t, 1-ε, 1+ε) · A_t)
  - ε typically 0.1-0.2
  - Clips objective when ratio deviates too much
- **Intuition**: if advantage positive and ratio > 1+ε, don't get extra credit (already increased enough)
- **Why popular**:
  - Simple to implement
  - Good performance across many domains
  - Robust to hyperparameters
  - Stable training
- **Used in**: ChatGPT (RLHF), robotics, games

---
