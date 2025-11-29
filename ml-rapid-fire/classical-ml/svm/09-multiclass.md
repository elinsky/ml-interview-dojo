# Multiclass SVM

**Q:** How do SVMs handle multiclass classification?

**A:**

- SVMs are inherently **binary classifiers** — must extend for multiclass
- **One-vs-One (OvO)**: Train k(k-1)/2 classifiers for k classes; vote to predict
- **One-vs-Rest (OvR)**: Train k classifiers; each separates one class from all others
- SVC uses OvO internally (libsvm), LinearSVC uses OvR (liblinear)
- OvO: more classifiers, smaller training sets per classifier
- OvR: fewer classifiers, larger imbalanced training sets

---
