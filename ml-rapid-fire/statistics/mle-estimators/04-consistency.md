# Consistency of Estimators

**Q:** What does it mean for an estimator to be consistent?
- Definition
- Relationship to bias and variance
- Why it matters

**A:**

- **Definition**: θ̂ₙ → θ in probability as n → ∞ (estimate converges to true value with more data)
- **Sufficient conditions**: if Bias → 0 and Var → 0 as n → ∞, then consistent
- **Why it matters**: guarantees that with enough data, we get arbitrarily close to truth
- **Note**: unbiased ≠ consistent (could be unbiased but high variance that doesn't shrink)
- **Example**: sample mean is consistent for population mean (LLN)

---
