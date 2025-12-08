# When to Choose L2 (Ridge)

**Q:** When would you choose L2 regularization (Ridge)? (3 reasons)

**A:**

- To **shrink coefficients without dropping** any
- When predictors are **highly correlated** (more stable than L1)
  - L2 shrinks correlated coefficients toward each other, keeping both but reducing their combined effect
- When **prediction accuracy > interpretability** (L2 keeps all features, harder to explain than L1's sparse model)

---
