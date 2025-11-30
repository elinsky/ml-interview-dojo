# Metrics for Imbalanced Data

**Q:** What metrics should you use for imbalanced classification?
- Bad metrics
- Good metrics
- Why

**A:**

- **Bad**: accuracy (misleading when classes unbalanced)
- **Good metrics**:
  - **Precision-Recall**: focus on positive class performance
  - **F1 score**: harmonic mean of precision and recall
  - **AUPRC**: area under precision-recall curve (better than AUROC for imbalanced)
  - **AUROC**: still useful but can be optimistic
  - **Confusion matrix**: see full picture of errors
- **Class-specific**:
  - Recall (sensitivity): TP / (TP + FN) — of actual positives, how many caught?
  - Precision: TP / (TP + FP) — of predicted positives, how many correct?
- **Finance example**: fraud detection — high recall (catch fraud) often more important than precision (some false alarms acceptable)

---
