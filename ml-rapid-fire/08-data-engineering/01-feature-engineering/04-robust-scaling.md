# Robust Scaling

**Q:** What is robust scaling and when is it preferred?
- Formula
- Why "robust"
- When to use

**A:**

- **Formula**: x' = (x - median) / IQR
  - IQR = Q3 - Q1 (interquartile range)
- **Why robust**: median and IQR are not affected by outliers (unlike mean and std)
- **When to use**:
  - Data has significant outliers you want to keep
  - Don't want outliers to affect scaling of majority of data
- **Sklearn**: `RobustScaler`
- **Finance example**: asset returns with fat tails — robust scaling prevents extreme returns from dominating

---
