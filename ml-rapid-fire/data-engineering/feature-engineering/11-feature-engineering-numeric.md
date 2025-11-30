# Numeric Feature Engineering

**Q:** What are common techniques for engineering numeric features?
- Transformations
- Interactions
- Domain-specific

**A:**

- **Transformations**:
  - Log transform: reduces skewness, handles multiplicative relationships
  - Square root, Box-Cox: normalize distributions
  - Binning/discretization: convert to categorical (can capture non-linear)
- **Interactions**:
  - Products: x₁ × x₂
  - Ratios: x₁ / x₂
  - Polynomial features: x², x₁x₂, etc.
- **Domain-specific (finance examples)**:
  - Rolling statistics: moving averages, rolling std
  - Differences: returns = (P_t - P_{t-1}) / P_{t-1}
  - Technical indicators: RSI, MACD, Bollinger bands
  - Relative values: price / 52-week high

---
