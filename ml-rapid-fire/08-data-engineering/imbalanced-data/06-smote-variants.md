# SMOTE Variants

**Q:** What are common SMOTE variants and when to use them?
- Borderline-SMOTE
- SMOTE-ENN
- ADASYN

**A:**

- **Borderline-SMOTE**: only oversample minority points near decision boundary
  - Focuses on "difficult" examples
  - Less likely to create noisy interior samples
- **SMOTE-ENN** (SMOTE + Edited Nearest Neighbors):
  - Apply SMOTE, then clean with ENN
  - ENN removes samples whose class differs from majority of neighbors
  - Cleans up noisy synthetic samples
- **ADASYN** (Adaptive Synthetic):
  - Generate more synthetic samples for minority examples harder to learn
  - Focuses on regions where minority samples have more majority neighbors
- **SMOTE-Tomek**: SMOTE + remove Tomek links (pairs of nearest neighbors from different classes)
- **When to use**: when basic SMOTE creates too many noisy samples, or when you want to focus on boundary regions

---
