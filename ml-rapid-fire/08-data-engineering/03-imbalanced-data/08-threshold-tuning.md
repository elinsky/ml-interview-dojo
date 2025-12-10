# Threshold Tuning

**Q:** How does threshold tuning help with imbalanced data?
- Default threshold
- Why tune
- How to choose

**A:**

- **Default threshold**: classifiers output probabilities, default threshold = 0.5 for binary
- **Why tune**: 0.5 may not be optimal for imbalanced data
  - Lower threshold → more positive predictions → higher recall, lower precision
  - Higher threshold → fewer positive predictions → lower recall, higher precision
- **How to choose**:
  - Plot precision-recall curve at different thresholds
  - Choose based on business requirements (target recall, acceptable precision)
  - Optimize F1 or custom metric
  - Use Youden's J statistic: max(sensitivity + specificity - 1)
- **Advantages**: no retraining needed, can adjust post-hoc
- **Key insight**: train model to produce good probability estimates, then tune threshold separately

---
