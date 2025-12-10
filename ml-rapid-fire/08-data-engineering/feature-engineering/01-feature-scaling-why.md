# Why Feature Scaling

**Q:** Why is feature scaling important in machine learning?
- Which algorithms need it
- Which don't need it
- What goes wrong without it

**A:**

- **Algorithms that need scaling**:
  - Gradient-based: neural networks, logistic regression (convergence speed)
  - Distance-based: KNN, K-means, SVM (distances dominated by large-scale features)
  - Regularized models: L1/L2 penalties affected by feature scale
- **Algorithms that don't need scaling**:
  - Tree-based: decision trees, random forests, gradient boosting (split on thresholds)
  - Naive Bayes (probabilities independent of scale)
- **What goes wrong**: slow convergence, features with larger ranges dominate, regularization applied unevenly

---
