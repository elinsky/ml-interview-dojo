# Gradient

**Q:** What is a gradient and what properties does it have?
- Definition
- Key properties
- Relationship to directional derivatives

**A:**

- **Definition**: ∇f = [∂f/∂x₁, ∂f/∂x₂, ..., ∂f/∂xₙ]ᵀ — vector of all partial derivatives
- **Key properties**:
  - Points in direction of steepest ascent (−∇f for steepest descent)
  - Magnitude = rate of steepest ascent
  - Perpendicular to level sets (contour lines)
- **Directional derivative**: Dᵤf = ∇f · u — rate of change in direction u (unit vector)
  - Maximum when u aligned with ∇f
- **Gradient descent**: θ ← θ - α∇L — move opposite to gradient to minimize

---
