# Variance and MSE of Estimators

**Q:** How do you evaluate estimator quality beyond bias?
- Variance of estimator
- Mean Squared Error formula
- Bias-variance tradeoff for estimators

**A:**

- **Variance**: Var(θ̂) — how much the estimate varies across samples
- **MSE**: MSE(θ̂) = E[(θ̂ - θ)²] = Var(θ̂) + Bias(θ̂)²
- **Bias-variance tradeoff**: sometimes accepting small bias yields much lower variance → lower MSE overall
- **Example**: ridge regression introduces bias but reduces variance of coefficient estimates, often improving prediction
- **Standard error**: SE(θ̂) = √Var(θ̂) — estimated standard deviation of the estimator

---
