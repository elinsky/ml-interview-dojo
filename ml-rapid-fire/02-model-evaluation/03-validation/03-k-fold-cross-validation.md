# K-Fold Cross-Validation

**Q:** How does k-fold cross-validation work?
- How data is partitioned
- Training/validation rotation
- How final performance is computed

**A:**

- **Partition**: split data into k equal folds (commonly k=5 or k=10)
- **Rotation**: train on k-1 folds, validate on remaining fold; repeat k times so each fold serves as validation once
- **Final performance**: average metrics across all k folds

**See also:** [[202101080742 Cross Validation (K-Fold)]]

---
