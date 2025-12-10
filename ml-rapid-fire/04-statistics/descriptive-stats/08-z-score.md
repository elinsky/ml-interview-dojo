# Z-Score (Standardization)

**Q:** What is a z-score and when do you use it?
- Formula
- Interpretation
- Use cases

**A:**

- **Formula**: z = (x - μ) / σ — how many standard deviations from mean
- **Interpretation**: z = 2 means value is 2 standard deviations above mean
- **Use cases**:
  - Compare values from different distributions (standardize to same scale)
  - Identify outliers (|z| > 3 often flagged)
  - Feature scaling in ML (zero mean, unit variance)
  - Convert to probability under normal assumption
- **Example**: compare Sharpe ratios of different strategies (returns standardized by volatility)

---
