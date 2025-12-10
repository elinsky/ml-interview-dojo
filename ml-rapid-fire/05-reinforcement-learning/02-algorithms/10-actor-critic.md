# Actor-Critic Methods

**Q:** What are actor-critic methods and why combine policy and value?
- Architecture
- Why combine
- Advantage actor-critic

**A:**

- **Architecture**: two components
  - **Actor**: policy network π_θ(a|s) — decides actions
  - **Critic**: value network V_φ(s) or Q_φ(s,a) — evaluates actions
- **Why combine**:
  - Policy gradient has high variance (uses full return)
  - Critic provides lower-variance estimate of return
  - Actor: ∇log π_θ(a|s) · A(s,a) instead of · G_t
- **Advantage actor-critic (A2C)**:
  - Use advantage A(s,a) = Q(s,a) - V(s) ≈ r + γV(s') - V(s)
  - Subtracting baseline V(s) reduces variance without bias
- **A3C** (Asynchronous): multiple workers in parallel
- **Key insight**: critic learns faster (supervised on rewards), guides actor's updates

---
