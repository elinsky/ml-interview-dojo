# MLE Derivation Process

**Q:** How do you derive an MLE estimate?
- Steps to derive
- Why use log-likelihood
- Example setup

**A:**

- **Steps**:
  1. Write likelihood: L(θ) = ∏ᵢ P(xᵢ | θ) (product for iid data)
  2. Take log: ℓ(θ) = Σᵢ log P(xᵢ | θ) (sum is easier)
  3. Differentiate: ∂ℓ/∂θ = 0
  4. Solve for θ̂
- **Why log**: products → sums (easier calculus); log is monotonic so same argmax
- **Example**: for Normal(μ, σ²) with known σ², MLE for μ is sample mean x̄
- **Note**: verify it's a maximum (second derivative < 0 or check boundary)

---
