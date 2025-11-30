# Policy Gradient Basics

**Q:** What is the policy gradient approach and how does it differ from value-based methods?
- Key idea
- Policy gradient theorem
- REINFORCE

**A:**

- **Key idea**: directly parameterize and optimize policy π_θ(a|s)
  - No value function needed (though often used)
  - Optimize: J(θ) = E[sum of rewards under π_θ]
- **Policy gradient theorem**:
  - ∇J(θ) = E_π[∇log π_θ(a|s) · G_t]
  - "Increase probability of actions that led to high returns"
- **REINFORCE algorithm**:
  1. Sample episode using π_θ
  2. For each step: θ ← θ + α · ∇log π_θ(a_t|s_t) · G_t
  3. G_t = return from step t
- **Advantages over value-based**:
  - Natural for continuous actions
  - Can learn stochastic policies
  - Smoother optimization landscape
- **Disadvantage**: high variance (complete return G_t)

---
