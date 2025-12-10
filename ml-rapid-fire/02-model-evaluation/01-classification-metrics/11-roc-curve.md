# ROC Curve

**Q:** What is an ROC curve?
- What it plots (axes)
- What the diagonal means
- Where a perfect classifier is
- What tradeoff it visualizes

**A:**

- Plot of **Sensitivity (aka Recall, TPR, 'hit rate')** vs **1 - Specificity (aka FPR, 'false alarm')** at all decision thresholds
- Sensitivity = TP / (TP + FN)
- FPR = FP / (FP + TN) = 1 - Specificity
- Diagonal line = random classifier (baseline)
- Top-left corner = perfect classifier
- Visualizes the **sensitivity-specificity tradeoff**

---
