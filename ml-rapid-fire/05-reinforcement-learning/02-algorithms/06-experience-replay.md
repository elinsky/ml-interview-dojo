# Experience Replay

**Q:** What is experience replay and why is it important for deep RL?
- Concept
- Why needed
- Implementation

**A:**

- **Concept**: store transitions (s, a, r, s') in buffer, sample randomly for training
- **Why needed** (solves two problems):
  1. **Correlated samples**: sequential experiences are correlated, bad for neural networks (i.i.d. assumption). Random sampling breaks correlation.
  2. **Sample efficiency**: reuse each experience many times
- **Implementation**:
  - Replay buffer: fixed-size FIFO queue
  - Store: (s, a, r, s', done)
  - Sample: random minibatch for each update
- **Prioritized experience replay**: sample more important transitions more often
  - Priority based on TD error (surprising transitions)
- **Key insight**: enables off-policy learning — learn from any past experience
- **Used in**: DQN, DDPG, SAC, most off-policy deep RL

---
