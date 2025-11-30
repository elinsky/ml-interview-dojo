# Temporal Difference Learning

**Q:** What is temporal difference (TD) learning?
- Key idea
- TD update
- Comparison to Monte Carlo

**A:**

- **Key idea**: update estimates based on other estimates (bootstrapping)
  - Don't wait until end of episode
  - Learn from incomplete sequences
- **TD(0) update** for V:
  - V(s) ← V(s) + α[R + γV(s') - V(s)]
  - Target: R + γV(s') (one-step lookahead)
  - Error: R + γV(s') - V(s) (TD error)
- **Comparison to Monte Carlo**:
  - MC: wait for complete return, no bootstrapping
  - TD: update after each step, bootstrap from next state
  - TD: lower variance (one random step vs many), some bias (uses estimate)
  - MC: unbiased but high variance
- **TD(λ)**: interpolate between TD(0) and MC using eligibility traces

---
