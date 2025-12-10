# Random Undersampling

**Q:** What is random undersampling and what are its tradeoffs?
- Method
- Advantages
- Disadvantages

**A:**

- **Method**: randomly remove majority class examples until classes balanced
- **Advantages**:
  - Simple and fast
  - Reduces training time
  - No overfitting risk from duplication
- **Disadvantages**:
  - **Information loss**: discards potentially useful data
  - May remove important examples
  - Can hurt model performance if majority class is already small
- **Implementation**: `imblearn.under_sampling.RandomUnderSampler`
- **When to use**: very large datasets where majority class has redundant examples
- **Variant**: can combine with ensemble (train multiple models on different undersampled subsets)

---
