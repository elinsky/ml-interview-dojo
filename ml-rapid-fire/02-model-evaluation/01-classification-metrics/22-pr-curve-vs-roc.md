# PR Curve vs ROC

**Q:** When should you use Precision-Recall curve instead of ROC?
- When to prefer PR curve
- Why ROC can be misleading
- What PR curve focuses on
- Technical difference between them

**A:**

- **When to prefer Precision-Recall**: When classes are **highly imbalanced** (e.g., rare disease, fraud detection)
- **Why ROC misleads**: ROC can be overly optimistic with imbalanced data - False Positive Rate stays low even with many False Positives because True Negatives dominate denominator
- **What Precision-Recall focuses on**: Positive class performance only
- **Technical difference**: ROC uses True Negatives in False Positive Rate; Precision-Recall ignores True Negatives entirely

**See also:** [[202202230714 Imbalanced Classification]]

---
