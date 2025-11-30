# SMOTE

**Q:** How does SMOTE work and what are its limitations?
- Algorithm
- Advantages over random oversampling
- Limitations

**A:**

- **SMOTE**: Synthetic Minority Over-sampling Technique
- **Algorithm**:
  1. For each minority sample, find k nearest minority neighbors
  2. Randomly select one neighbor
  3. Create synthetic sample along line segment between original and neighbor
  4. x_new = x + rand(0,1) × (x_neighbor - x)
- **Advantages over random oversampling**:
  - Creates NEW synthetic examples (not duplicates)
  - Expands decision region for minority class
  - Reduces overfitting risk
- **Limitations**:
  - Can create noisy samples in overlapping regions
  - Doesn't consider majority class (may create samples in majority region)
  - Assumes linear interpolation is meaningful
- **Implementation**: `imblearn.over_sampling.SMOTE`

---
