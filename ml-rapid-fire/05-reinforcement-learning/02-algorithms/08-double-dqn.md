# Double DQN

**Q:** What problem does Double DQN solve?
- Overestimation problem
- Solution
- Update rule

**A:**

- **Overestimation problem** in Q-learning:
  - Target uses max_a' Q(s',a') — max over noisy estimates
  - Noise in Q → max is biased upward
  - Overestimation accumulates, hurts learning
- **Solution**: decouple action selection from evaluation
  - Use online network to select action: a* = argmax_a' Q(s',a';θ)
  - Use target network to evaluate: Q(s',a*;θ⁻)
- **Update rule**:
  - Standard DQN: r + γ max_a' Q(s',a';θ⁻)
  - Double DQN: r + γ Q(s', argmax_a' Q(s',a';θ); θ⁻)
- **Result**: less overestimation, more stable learning, better performance
- **Simple change**: minimal code modification to DQN, significant improvement

---
