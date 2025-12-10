# Gradient Boosting

**Q:** What is Gradient Boosting?

**A:**

- Fits new model to **residuals** (errors) of previous model
- Uses **gradient descent in function space**
- Each tree predicts the **negative gradient** of loss
- Final prediction = **sum** of all trees (no voting like AdaBoost)
- Prone to overfitting — use learning rate, **early stopping**
- Breiman introduced; Friedman developed further

[[202104161654]]

---
