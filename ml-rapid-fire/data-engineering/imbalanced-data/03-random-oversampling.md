# Random Oversampling

**Q:** What is random oversampling and what are its risks?
- Method
- Advantages
- Risks

**A:**

- **Method**: duplicate minority class examples randomly until classes balanced
- **Advantages**:
  - Simple to implement
  - No information loss (all data retained)
  - Works with any classifier
- **Risks**:
  - **Overfitting**: model memorizes duplicated examples
  - Increased training time (more samples)
  - Doesn't add new information
- **Implementation**: `imblearn.over_sampling.RandomOverSampler`
- **Mitigation**: use with cross-validation, oversample only training folds
- **When to use**: when you have very few minority samples and can't afford to lose any

---
