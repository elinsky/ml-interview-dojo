# Function Approximation in RL

**Q:** Why do we need function approximation in RL and what are the challenges?
- Why needed
- Approaches
- Challenges

**A:**

- **Why needed**:
  - Large or continuous state/action spaces (can't store table)
  - Generalization to unseen states
  - Example: video games have ~10^100 possible states
- **Approaches**:
  - Linear function approximation: V(s) = w^T φ(s)
  - Neural networks (deep RL): V(s) = NN(s; θ)
  - Can approximate V, Q, or policy π
- **Challenges**:
  - **Deadly triad**: function approximation + bootstrapping + off-policy → instability
  - Non-stationary targets (policy changes)
  - Correlated samples (sequential data)
  - No convergence guarantees (unlike tabular)
- **Solutions**: experience replay, target networks, careful architecture design

---
