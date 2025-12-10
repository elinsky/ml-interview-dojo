# Target Encoding

**Q:** What is target encoding and what's the main risk?
- How it works
- Advantages
- Risk and mitigation

**A:**

- **How it works**: replace category with mean of target variable for that category
- **Example**: encode city by average house price in that city
- **Advantages**:
  - Handles high cardinality well (single column)
  - Captures relationship between category and target
- **Risk**: **target leakage** — encoding uses target info, can cause overfitting
- **Mitigation**:
  - Use cross-validation folds (encode using out-of-fold target means)
  - Add smoothing/regularization toward global mean
  - Add noise
- **Finance example**: encode ticker symbol by historical average return

---
