# Adjusted R²

**Q:** What is Adjusted R² and when should you use it?

**A:**

- Adjusted R² = 1 - [(SSE/df_e) / (SST/df_t)]
- df_e = n - p - 1 (error degrees of freedom)
- **Penalizes adding features** that don't improve model
- Can decrease when adding useless features
- Use to compare models with different numbers of predictors

**See also:** [[202107041617 Adjusted R-Squared]], [[202107270653 Model Selection for Linear Regression]]

---
