# Gradient Descent Basics

**Q:** How does gradient descent work?
- Update rule
- Learning rate role
- Convergence conditions

**A:**

- **Update rule**: θₜ₊₁ = θₜ - α∇L(θₜ)
  - α = learning rate (step size)
  - ∇L = gradient of loss with respect to parameters
- **Learning rate**:
  - Too small: slow convergence
  - Too large: overshooting, oscillation, divergence
- **Convergence** (for convex, smooth f):
  - Guaranteed to converge to global minimum
  - Rate: O(1/t) for general convex, O(ρᵗ) for strongly convex (exponential)
- **Stopping criteria**: gradient norm < ε, loss change < ε, max iterations

---
