# Jacobian

**Q:** What is a Jacobian matrix?
- Definition
- When you need it
- Relationship to gradient

**A:**

- **Definition**: matrix of all first-order partial derivatives for vector-valued function f: ℝⁿ → ℝᵐ
  - J[i,j] = ∂fᵢ/∂xⱼ
  - Shape: m × n (m outputs, n inputs)
- **When needed**: function outputs a vector, not scalar
- **Relationship to gradient**: gradient is Jacobian of scalar function (1 × n, often written as column)
- **Chain rule with Jacobian**: J[f∘g] = J[f] · J[g] (matrix multiplication)
- **ML context**: layer transformations, change of variables in probability

---
