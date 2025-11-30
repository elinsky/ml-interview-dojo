# Mean Absolute Error (MAE)

**Q:** What is MAE and when should you use it?
- Formula
- Advantage over MSE/RMSE
- Why it has that advantage (type of penalty)
- Optimization tradeoff
- When to use it

**A:**

- **Formula**: MAE = (1/n) * Σ|y - ŷ|
- **Advantage**: More robust to outliers than MSE/RMSE
- **Why**: Linear penalty treats all errors proportionally (a $10 error is 10x worse than $1, not 100x)
- **Optimization tradeoff**: Not differentiable at 0, harder to optimize than MSE
- **When to use**: When outliers shouldn't dominate; when you want interpretable "average error"; when median is more meaningful than mean

---
