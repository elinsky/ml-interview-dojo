# Data Leakage

**Q:** What is data leakage and how do you prevent it?
- Definition
- Common examples (2 types)
- Prevention strategies (3 types)

**A:**

- **Definition**: information that wouldn't be available at inference time leaks into training (gives away the answer)
- **Examples**:
  - Target leakage: future info in features (e.g., full OHLC bar at start of minute)
  - Preprocessing leakage: fitting scaler on full data before split (test stats leak into training)
- **Prevention**:
  - Split data before any preprocessing
  - Fit transformers only on training data
  - Don't resample test set for imbalanced data

**See also:** [[202202230714 Imbalanced Classification]], [[202101241624 Data Preprocessing for Neural Networks]]

---
