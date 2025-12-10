# Ensemble Methods for Imbalanced Data

**Q:** How can ensemble methods help with imbalanced data?
- Balanced bagging
- EasyEnsemble
- Why ensembles help

**A:**

- **Balanced Bagging**:
  - Bootstrap samples that undersample majority class
  - Each base learner sees balanced subset
  - Aggregate predictions
- **EasyEnsemble**:
  - Train multiple classifiers on different undersampled subsets
  - Combine predictions (voting or averaging)
  - Uses all majority class data across ensemble
- **BalancedRandomForest**: random forest with balanced bootstrap samples
- **Why ensembles help**:
  - Reduces variance from undersampling
  - Uses more of majority class data (different subsets per model)
  - Combines multiple views of the data
- **Implementation**: `imblearn.ensemble.BalancedBaggingClassifier`, `BalancedRandomForestClassifier`

---
