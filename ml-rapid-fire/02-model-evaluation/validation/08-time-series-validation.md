# Time Series Validation

**Q:** How do you validate time series models?
- Core principle (1 sentence)
- Why no random shuffle (3 reasons)
- Walk-forward validation approaches (2 types with tradeoffs)

**A:**

- **Core principle**: train on past → validate/test on later timestamps (no random shuffling)
- **Why time ≠ IID**:
  - Temporal dependence: values depend on previous ones; shuffling destroys structure
  - Leakage risk: future info can slip into training via scaling/feature engineering
  - Non-stationarity (drift): data distribution changes over time
- **Walk-forward validation** (aka forward chaining, rolling origin):
  - Expanding window: train [t₀..t₃], validate [t₄]; train [t₀..t₄], validate [t₅]... (more data, but older data may drift)
  - Sliding window: train [t₀..t₃], validate [t₄]; train [t₁..t₄], validate [t₅]... (emphasizes recency, good under drift)

**See also:** [[202101080742 Cross Validation (K-Fold)]]

---
