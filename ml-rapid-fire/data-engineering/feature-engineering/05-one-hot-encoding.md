# One-Hot Encoding

**Q:** What is one-hot encoding and what are its tradeoffs?
- How it works
- Advantages
- Disadvantages

**A:**

- **How it works**: convert categorical variable with k categories into k binary columns (1 for present category, 0 otherwise)
- **Example**: color ∈ {red, green, blue} → [1,0,0], [0,1,0], [0,0,1]
- **Advantages**:
  - No ordinal relationship implied
  - Works with any algorithm
- **Disadvantages**:
  - High cardinality → many columns (curse of dimensionality)
  - Sparse representation
  - Can cause multicollinearity (drop one column for linear models)
- **Sklearn**: `OneHotEncoder`

---
