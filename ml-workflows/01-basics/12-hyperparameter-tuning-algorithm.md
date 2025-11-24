# Question

Explain the algorithm for tuning hyperparameters.

# Answer

There are several approaches to hyperparameter tuning, each with different trade-offs between computational cost and likelihood of finding optimal values:

**1. Grid Search**
- Define a discrete set of values for each hyperparameter
- Train and evaluate the model on every possible combination
- Select the combination with best validation performance
- **Pros**: Exhaustive, guaranteed to find best combination in the grid
- **Cons**: Exponentially expensive as number of hyperparameters increases; may miss optimal values between grid points

**2. Random Search**
- Define distributions for each hyperparameter
- Sample random combinations of values
- Train and evaluate for a fixed budget of trials
- Select the best performing combination
- **Pros**: More efficient than grid search; can explore wider range; often finds good solutions faster
- **Cons**: No guarantee of finding optimal values

**3. Bayesian Optimization**
- Build a probabilistic model of the objective function (e.g., Gaussian Process)
- Use acquisition function to decide which hyperparameters to try next
- Balance exploration (trying new regions) vs exploitation (refining known good regions)
- Update model after each trial
- **Pros**: Sample-efficient; good for expensive evaluations; principled exploration
- **Cons**: More complex to implement; overhead for building surrogate model

**General Algorithm (applies to all methods):**

1. **Define search space**: Specify which hyperparameters to tune and their ranges/distributions
2. **Choose validation strategy**: K-fold cross-validation or hold-out validation set
3. **Select evaluation metric**: Accuracy, F1, AUC, etc. depending on problem
4. **Sample hyperparameter configurations**: According to chosen method (grid, random, Bayesian)
5. **For each configuration:**
   - Train model with those hyperparameters on training data
   - Evaluate on validation data
   - Record performance metric
6. **Select best configuration**: Choose hyperparameters that achieved best validation performance
7. **Final evaluation**: Retrain with best hyperparameters and evaluate on held-out test set

**Best Practices:**

- Use cross-validation to get robust performance estimates
- Search on log scale for parameters like learning rate (e.g., 0.001, 0.01, 0.1, 1.0)
- Start with coarse search, then refine around promising regions
- Monitor for overfitting to validation set if doing many iterations

---

## Extracts from my notes

### 202101080742 Cross Validation (K-Fold).txt

```
Cross validation is a general technique that estimates how well a model will **generalize** to new data.  K-Fold cross validation is a method that attempts to get the most out of your data.  **The goal is to use all the data for learning while still being able to measure an accurate generalization error** [@russell2010artificial, p. 708].

How does it work?

1. First split the data into train and test sets.  Leave the test set alone until you have your final model.

1. Then take the training data, and partition it into $K$ (usually 5) folds.

1. Train $K$ models:

```code
for i in k:
    train a model on all folds except fold i
    evaluate performance on i
```

4. When complete, you have $K$ performance scores for your model.  These can be used to estimate generalization error, and it's standard deviation.

After evaluating the performance of a model, you can tweak the hyperparameters, and follow the same process again.  Only after you have chosen a final model do you evaluate on [the test set]

**Note**:  These models are thrown away when you are done.  Usually you would then train your final model over **all** the training data.  Then do your final evaluation of the model on the test set, only using the test set once.
```

### 202101241506 Simple Hold-Out Validation.txt

```
This is the simplest validation technique.  Train on the training set.  Evaluate your performance on the validation set.  At this point you can tune your model, retrain it on the training set, and re-evaluate performance on the validation set.  Only once you have a final model do you evaluate performance on the test set.

From François Chollet [@chollet2018deep, p. 99]:

> This is the simplest evaluation protocol, and it suffers from one flaw; if little data is available, then your validation and test sets may contain too few samples to be statistically representative of the data at hand.
```

### 202107270653 Model Selection for Linear Regression.txt

```
Given a regression problem, model selection is the process of determining the functional form of the regression equation. This involves deciding which variables will be included in the model (see [[202107210815 Variable Selection Problem in Regression]]). It also involves deciding if there will be any transformations or interactions. Then given a set of candidate models, you need to decide how to compare them to each other.

Wasserman lists a few methods that better estimate risk (test error) [@wasserman2004all, p. 219]:

* Mallow's $C_p$
* [[202107260847 Akaike information criterion (AIC)]]
* [[202107271816 Bayesian information criterion (BIC)]]
* Leave-one-out cross-validation
* [[202101080742 Cross Validation (K-Fold)]] - this directly estimates test error. Whereas AIC, BIC, and Adjusted-R Squared make an adjustment to the training error to account for the bias due to overfitting.
```

## Gaps filled by me (not from notes)

The specific descriptions of grid search, random search, and Bayesian optimization methods, their trade-offs, and the general algorithm structure were synthesized from ML best practices, as my notes focused more on validation strategies rather than explicit hyperparameter search algorithms.
