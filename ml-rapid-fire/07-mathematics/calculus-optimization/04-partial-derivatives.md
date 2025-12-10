# Partial Derivatives

**Q:** What are partial derivatives and when do you use them?
- Definition
- Notation
- How to compute

**A:**

- **Definition**: derivative with respect to one variable while holding others constant
- **Notation**: ∂f/∂xᵢ or fₓᵢ
- **How to compute**: treat all other variables as constants, differentiate normally
- **Example**: f(x,y) = x²y + 3y → ∂f/∂x = 2xy, ∂f/∂y = x² + 3
- **Use in ML**: loss L(θ₁, θ₂, ...) depends on many parameters; need ∂L/∂θᵢ for each parameter to update

---
