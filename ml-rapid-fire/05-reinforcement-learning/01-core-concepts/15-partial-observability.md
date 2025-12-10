# Partial Observability (POMDP)

**Q:** What is a POMDP and how does it differ from an MDP?
- Definition
- Components
- Approaches

**A:**

- **POMDP**: Partially Observable Markov Decision Process
- **Key difference**: agent doesn't observe true state, only observations
- **Additional components**:
  - **O**: observation space
  - **Ω(o|s',a)**: observation probability
  - Agent receives observation o, not state s
- **Belief state**: probability distribution over states given history
  - b(s) = P(S_t = s | o_1, a_1, ..., o_t)
  - Decision making on belief state (continuous, high-dimensional)
- **Approaches**:
  - **History-based**: use sequence of observations (RNNs, LSTMs)
  - **Belief state**: maintain and plan on belief distribution
  - **Frame stacking**: stack recent observations (DQN for Atari)
- **Example**: poker (don't see opponent's cards), trading (don't know others' intentions)

---
