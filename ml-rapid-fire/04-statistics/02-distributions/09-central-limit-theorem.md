# Central Limit Theorem

**Q:** What is the Central Limit Theorem and why does it matter?
- Statement
- Requirements
- Why it's important
- When it fails

**A:**

- **Statement**: sample mean of n iid RVs → N(μ, σ²/n) as n → ∞, regardless of original distribution
- **Requirements**: finite mean and variance; samples are independent
- **Why it matters**: justifies normal assumption for averages; enables hypothesis testing and confidence intervals
- **When it fails**:
  - Heavy-tailed distributions (infinite variance) — convergence is slow or doesn't happen
  - Small n with highly skewed data
- **Rule of thumb**: n ≥ 30 often sufficient for "nice" distributions

---
