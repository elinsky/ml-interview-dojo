# Holdout vs Cross-Validation

**Q:** When should you use simple holdout vs cross-validation?
- When to use holdout (2 reasons)
- When to use CV (2 reasons)
- Why CV gives better estimates

**A:**

- **Holdout**: large datasets (can afford to "waste" data); expensive models (train once vs k times)
- **CV**: smaller datasets (need all data for training); hyperparameter tuning (need reliable comparisons)
- **Why CV is better**: averaging k estimates reduces variance in performance estimate

**See also:** [[202101241506 Simple Hold-Out Validation]], [[202101080742 Cross Validation (K-Fold)]]

---
