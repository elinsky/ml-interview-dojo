# R² Limitations

**Q:** What are the limitations of R²? (Name at least 4)

**A:**

- **Always increases** (or stays same) when adding features; useless for comparing models with different feature counts
- **Can be negative out-of-sample** if model worse than predicting mean
- **Doesn't indicate bias**: R² only measures variance explained, not whether predictions are systematically off
  - E.g., model could have high R² but consistently underpredict by 10%
- **High R² doesn't guarantee generalization**: R² on training data can be 0.99 while test R² is 0.3
- **Doesn't tell you if model is appropriate**: can fit linear model to nonlinear data and get decent R²

**See also:** [[202107041234 Coefficient of Determination (R-Squared)]], [[202107041617 Adjusted R-Squared]]

---
