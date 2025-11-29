# Data Leakage

**Q:** What is data leakage and how do you prevent it?

**A:**

- Information from test/validation leaks into training
- Examples: fitting scaler on full data, time-based leakage
- Prevent: fit preprocessing only on training data
- Prevent: split before any data processing
- Leave test set unmodified even when resampling for imbalance

**See also:** [[202202230714 Imbalanced Classification]], [[202101241624 Data Preprocessing for Neural Networks]]

---
