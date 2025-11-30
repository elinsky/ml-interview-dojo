# KNN Imputation

**Q:** How does KNN imputation work and when should you use it?
- Method
- Advantages
- Disadvantages

**A:**

- **Method**: find k nearest neighbors (using non-missing features), impute with mean/mode of neighbors' values
- **Advantages**:
  - Uses relationships between features
  - Can capture local patterns
  - Works for both numerical and categorical
- **Disadvantages**:
  - Computationally expensive: O(n²) distance calculations
  - Sensitive to scale (need to normalize first)
  - Choice of k and distance metric matter
  - Struggles with high missingness rates
- **Sklearn**: `KNNImputer`
- **When to use**: moderate-sized datasets where feature relationships are important

---
