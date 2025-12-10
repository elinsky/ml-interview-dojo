# MSE vs MAE

**Q:** When should you use MSE vs MAE?
- Outliers
- Large errors
- Optimization
- Interpretability

**A:**

- **Outliers**: MAE (linear penalty, robust); MSE (quadratic, sensitive)
- **Large errors matter**: MSE (penalizes heavily); MAE (treats proportionally)
- **Optimization**: MSE (smooth, differentiable); MAE (not differentiable at 0)
- **Interpretability**: MAE ("average error in units"); MSE (squared units)

---
