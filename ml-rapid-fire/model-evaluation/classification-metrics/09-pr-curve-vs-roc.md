# PR Curve vs ROC

**Q:** When should you use Precision-Recall curve instead of ROC?

**A:**

- Use PR curve when classes are **highly imbalanced**
- ROC can be overly optimistic with imbalanced data
- PR curve focuses on positive class performance
- AUC-PR often more informative than AUC-ROC for rare events
- ROC includes TN in FPR; PR ignores TNs entirely

**See also:** [[202202230714 Imbalanced Classification]]

---
