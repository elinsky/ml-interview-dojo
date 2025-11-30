# Adjusted R²

**Q:** What is Adjusted R² and when should you use it?
- What R² limitation it addresses
- How it differs from R² (key behavior)
- When to use it

**A:**

- **Formula**: Adjusted R² = 1 - [(SSE/df_e) / (SST/df_t)]
  - df_e = n - p - 1 (error degrees of freedom)
  - df_t = n - 1 (total degrees of freedom)
- **What it addresses**: R² always increases with more features; Adjusted R² penalizes model complexity
- **Key behavior**: Can decrease when adding useless features (unlike R²)
- **When to use**: To compare models with different numbers of predictors

**See also:** [[202107041617 Adjusted R-Squared]], [[202107270653 Model Selection for Linear Regression]]

---
