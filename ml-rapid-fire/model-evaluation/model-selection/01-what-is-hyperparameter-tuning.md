# What is Hyperparameter Tuning?

**Q:** What is hyperparameter tuning and why is it necessary?
- Definition of hyperparameters (vs learned parameters)
- 5 components of a tuning search
- Why it's necessary

**A:**

- **Hyperparameters**: model settings set before training, not learned from data (e.g., C/kernel/gamma for SVM, alpha for Lasso, tree depth)
- **5 components of a search**:
  1. Estimator (model to tune)
  2. Parameter space (values to try)
  3. Search method (grid, random, Bayesian, etc.)
  4. Cross-validation scheme (how to evaluate each candidate)
  5. Score function (metric to optimize)
- **Why necessary**: too expensive or impossible to learn (discrete choices, non-differentiable); affects model capacity, regularization, learning dynamics

**See also:** [[202101241752 Chollet's Machine Learning Workflow]], [[202101171833 Hyperparameter Tuning for Learning Rate in Neural Networks]]

---
