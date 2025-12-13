# Bayesian Optimization

**Q:** What is Bayesian optimization for hyperparameter tuning?
- How it works (high level)
- Key mechanism

**A:**

- Builds a probabilistic surrogate model of the objective function
  - Objective function: maps hyperparameters → validation score (expensive to evaluate)
  - Surrogate model: cheap approximation (often Gaussian Process) that estimates performance across hyperparameter space
- Uses previous results to guide where to search next
  - Previous results: (hyperparameter config, validation score) pairs from earlier trials
- Acquisition function balances exploration vs exploitation
  - Acquisition function: scores candidate points by combining predicted performance + uncertainty; picks next hyperparameters to try

---
