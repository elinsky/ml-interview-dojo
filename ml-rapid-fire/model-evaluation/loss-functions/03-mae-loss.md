# MAE Loss

**Q:** What is Mean Absolute Error loss and when do you use it?

**A:**

- MAE = (1/n) Σ|y - ŷ|
- More robust to outliers than MSE
- Not differentiable at zero (use subgradient)
- Produces median-like predictions

---
