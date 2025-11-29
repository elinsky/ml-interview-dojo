# AdaBoost

**Q:** What is AdaBoost?

**A:**

- **Adaptive Boosting** (Freund & Schapire) — adjusts sample weights each iteration
- Uses **weighted training set**: misclassified → higher weight
- Each model weighted by log((1-error)/error)
- Final prediction = **weighted vote** of all models
- Sensitive to **noisy data and outliers**

[[202104161653]] [[202104171010]]

---
