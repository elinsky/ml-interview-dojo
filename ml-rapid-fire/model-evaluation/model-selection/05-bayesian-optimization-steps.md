# Bayesian Optimization Steps

**Q:** What are the steps to use Bayesian optimization for hyperparameter tuning?

**A:**

- Define the objective function (hyperparameters → validation score via CV)
- Define the search space (range/distribution for each hyperparameter)
- Run the optimization loop (surrogate model proposes candidates, evaluate, update)
- Retrain final model with best hyperparameters on full training data

---
