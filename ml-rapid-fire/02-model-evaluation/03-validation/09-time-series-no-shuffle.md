# Why No Random Shuffle for Time Series

**Q:** Why can't you use random shuffle cross-validation for time series?

**A:**
- Temporal dependence: values depend on previous ones; shuffling destroys structure
- Leakage risk: future info can slip into training via scaling/feature engineering
- Non-stationarity (drift): data distribution changes over time

---
