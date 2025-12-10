# Markov Decision Process (MDP)

**Q:** What is an MDP and what are its components?
- Definition
- Components (S, A, P, R, γ)
- Markov property

**A:**

- **Definition**: mathematical framework for sequential decision making
- **Components**:
  - **S**: state space (all possible states)
  - **A**: action space (all possible actions)
  - **P(s'|s,a)**: transition probability (dynamics)
  - **R(s,a,s')**: reward function
  - **γ**: discount factor ∈ [0,1]
- **Markov property**: future depends only on current state, not history
  - P(s_{t+1}|s_t, a_t) = P(s_{t+1}|s_0, a_0, ..., s_t, a_t)
  - "The future is independent of the past given the present"
- **Episode**: sequence from initial state to terminal state
- **Goal**: find policy that maximizes expected cumulative reward

---
