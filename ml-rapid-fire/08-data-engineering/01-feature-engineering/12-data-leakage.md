# Data Leakage

**Q:** What is data leakage and how do you prevent it?
- Definition
- Common causes
- Prevention

**A:**

- **Definition**: using information during training that wouldn't be available at prediction time
- **Common causes**:
  - **Target leakage**: features derived from target (e.g., "account_closed" predicting churn)
  - **Train-test contamination**: fitting scaler on full data before split
  - **Temporal leakage**: using future data to predict past (critical in finance)
  - **Duplicate/near-duplicate rows**: same data in train and test
- **Prevention**:
  - Split data FIRST, then preprocess
  - Use pipelines to encapsulate preprocessing
  - For time series: always split by time, no shuffling
  - Scrutinize features that seem "too good"
- **Signs of leakage**: suspiciously high validation scores that don't hold in production

---
