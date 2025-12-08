# When to Choose L1 (Lasso)

**Q:** When would you choose L1 regularization (Lasso)? (3 reasons)

**A:**

- For **feature selection** when many features are irrelevant/redundant
- For a **sparse, interpretable** model (fewer features = easier to explain than L2's dense model)
- When you can tolerate **instability with correlated** predictors
  - L1 keeps one correlated predictor, drops others to 0 — which one it keeps can vary with the data

---
