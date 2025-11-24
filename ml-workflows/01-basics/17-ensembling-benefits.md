# Question

Why does ensembling independently trained models generally improve performance?

# Answer

Ensembling improves performance by combining multiple models (hypotheses) to reduce prediction errors through diversity. The fundamental insight is that if individual models make different mistakes—that is, their errors are somewhat independent—then aggregating their predictions can cancel out individual errors and produce more accurate overall predictions.

**Core Principle: Error Independence**

The key assumption is that models' errors should be uncorrelated. While perfect independence is unrealistic (models trained on the same data will be similarly misled by its characteristics), even partial independence where models are "at least a little bit different" can significantly improve ensemble performance. The goal is to create diverse models that don't all make the same mistakes.

**How Ensembling Improves Performance:**

1. **Variance Reduction (Bagging)**: By training models on different bootstrap samples of the data and averaging their predictions, bagging reduces variance while maintaining similar bias. Each individual predictor may have higher bias than one trained on the full dataset, but aggregation reduces both bias and variance, resulting in an ensemble with similar bias but lower variance than a single predictor.

2. **Sequential Error Correction (Boosting)**: Boosting trains predictors sequentially, with each new predictor focusing on correcting the mistakes of previous ones. This combines many **weak learners** (models that perform only slightly better than random guessing, e.g., 50% + ε accuracy) into a **strong learner** with high accuracy.

3. **Averaging Out Random Errors**: When models make independent errors, aggregating predictions (through voting for classification or averaging for regression) tends to cancel out random individual errors, leaving the systematic signal.

**When Ensembling Works Best:**

- **Unstable predictors**: Bagging works particularly well when small changes in the training data cause large changes in the learned model (high variance models like decision trees). Bagging these unstable classifiers usually improves them significantly.

- **Stable predictors**: Bagging stable classifiers (low variance models like linear regression) is generally not beneficial, as there's little variance to reduce.

**Trade-offs:**

- **Pros**: Increased accuracy through error reduction
- **Cons**: Reduced interpretability (ensemble of 500 trees is harder to understand than a single tree), increased computational cost

---

## Extracts from my notes

### 202104171003 Ensemble Learning.txt

```
From Russell and Norvig [@russell2010artificial, p. 748]:

> The idea of ensemble learning methods is to select a collection, or ensemble, of hypotheses from the hypothesis space and combine their predictions.

Ideally, you want the errors made by each hypothesis to be independent of each other.  You don't want each model to make the same mistakes.

From Russell and Norvig [@russell2010artificial, p. 748]:

> Now, obviously the assumption of independence is unreasonable, because hypotheses are likely to be misled in the same way by any misleading aspects of the training data.  But if the hypotheses are at least a little bit different, thereby reducing the correlation between their errors, then ensemble learning can be very useful.

## Type of Ensemble Learning Algorithms

* [[202104161650 Boosting (Hypothesis Boosting)]]
    * [[202104161654 Gradient Boosting]]
    * [[202104161653 AdaBoost (Adaptive Boosting)]]
* [[202104161606 Bagging (Bootstrap Aggregating)]]
    * [[202104160934 Random Forests]]
* [[202104190752 Stacking (Stacked Generalization)]]

## Ensembles and Imbalanced Classification

Ensemble models work particularly well when you have an imbalanced classification problem, and you decide to downsample your training dataset. See [[202202230815 Combining Downsampling and Ensemble Learning for Imbalanced Classification]].
```

### 202104161606 Bagging (Bootstrap Aggregating).txt

```
### Objective

The idea behind bagging is to train many models with bootstrap samples (see [[202101080707 The Bootstrap]]), then aggregate each model's prediction into an ensemble model that makes the final prediction.

Geron describes the benefit of this approach [@geron2017hands, p. 193]:

> Each individual predictor has a higher bias than if it were trained on the original training set, but aggregation reduces both bias and variance.  Generally, the net result is that the ensemble has similar bias but a lower variance than a single predictor trained on the original training set.

A bagging predictor will work particularly well when a small change in your dataset causes a large change in the predictor model constructed [@BreimanLeo1996Bp, p. 123].  You could describe this as an ```instability of the prediction method``` [@BreimanLeo1996Bp, p. 123].  ```Bagging unstable classifiers usually improves them.  Bagging stable classifiers is not a good idea.``` [@BreimanLeo1996Bp, p. 131].

### Pros

* Increased accuracy [@BreimanLeo1996Bp, p. 137].

### Cons

* Reduced interpretability [@BreimanLeo1996Bp, p. 137].
```

### 202104161650 Boosting (Hypothesis Boosting).txt

```
The big idea behind boosting is to combine **many weak learners** (see [[202104171015 Weak Learner]]) to produce a **strong learner**.  Generally boosting methods will train predictors sequentially, with each predictor trying to correct for the mistakes of the previous predictor.

There are many boosting methods, but three of the most popular are AdaBoost (see [[202104161653 AdaBoost (Adaptive Boosting)]]) , and Gradient Boosting (see [[202104161654 Gradient Boosting]]) [@geron2017hands, p. 199].

## See Also

* [[202107170842 XGBoost]]
```

### 202104171015 Weak Learner.txt

```
A weak learning algorithm is an algorithm that [@russell2010artificial, p. 749]:

> always returns a hypothesis with accuracy on the training set that is slightly better than random guessing (i.e., 50% + $\epsilon$ for Boolean classification).
```

## Gaps filled by me (not from notes)

The explanation of how error independence leads to error cancellation through aggregation, the bulleted list of when ensembling works best, and the synthesis of how bagging and boosting achieve different types of improvement were created to directly answer the question. My notes provided the foundational concepts but didn't explicitly explain the mechanism by which diverse errors improve ensemble performance.
