# Imputation Best Practices

**Q:** What are best practices for handling missing data in ML pipelines?
- Analysis first
- Pipeline integration
- Validation

**A:**

- **Analysis first**:
  - Visualize missingness patterns (heatmaps, bar plots)
  - Test for MCAR vs MAR (Little's MCAR test)
  - Understand domain reason for missingness
- **Pipeline integration**:
  - Impute AFTER train/test split (prevent leakage)
  - Fit imputer on training data only
  - Use sklearn pipelines to ensure consistency
- **Validation**:
  - Compare multiple imputation strategies
  - Check if imputation affects model performance
  - Consider sensitivity analysis (how results change with different methods)
- **Documentation**: record imputation method and rationale for reproducibility
- **Don't forget**: sometimes missingness is the feature — add missing indicators

---
