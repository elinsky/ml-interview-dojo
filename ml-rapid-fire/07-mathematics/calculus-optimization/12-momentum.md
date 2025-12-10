# Momentum

**Q:** What is momentum in gradient descent and why does it help?
- Update rule
- Intuition
- Benefits

**A:**

- **Update rule**:
  - vₜ = βvₜ₋₁ + ∇L(θₜ) — accumulate velocity
  - θₜ₊₁ = θₜ - αvₜ — update parameters
  - β typically 0.9
- **Intuition**: "ball rolling downhill" — builds up speed in consistent direction, dampens oscillations
- **Benefits**:
  - Accelerates convergence in ravines (elongated contours)
  - Smooths out noisy gradients
  - Helps escape shallow local minima
- **Nesterov momentum**: look ahead before computing gradient (often slightly better)

---
