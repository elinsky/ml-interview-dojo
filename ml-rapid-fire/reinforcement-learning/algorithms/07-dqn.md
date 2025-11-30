# DQN (Deep Q-Network)

**Q:** What is DQN and what made it a breakthrough?
- Architecture
- Key innovations
- Why breakthrough

**A:**

- **Architecture**: neural network approximates Q(s,a)
  - Input: state (e.g., raw pixels)
  - Output: Q-value for each action
- **Key innovations**:
  1. **Experience replay**: break correlation, reuse data
  2. **Target network**: separate network for target Q values, updated periodically
     - Stabilizes training (target doesn't change every step)
     - θ⁻ updated to θ every C steps
  3. **Frame stacking**: stack 4 frames for velocity information
- **Loss**: MSE between Q(s,a;θ) and target r + γ max_a' Q(s',a';θ⁻)
- **Why breakthrough** (DeepMind 2013/2015):
  - First to combine deep learning with RL at scale
  - Human-level performance on Atari games
  - Showed neural networks can approximate value functions

---
