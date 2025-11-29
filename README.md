# ML Interview Dojo

Personal repository for ML interview prep flashcards.

## Tier System

| Tier | Name | Criteria |
|------|------|----------|
| 0 | ☑️ Attempted | Tried but couldn't recall |
| 1 | 👍 Recalled | Partial recall, or used hints/peeked |
| 2 | 💪 Independent | Full recall, no hints, no peeking |
| 3 | 🏆 Mastered | Independent + answered in ≤2 min |
| - | ⭐ New | Not yet attempted |

## Progress Summary

**Mastery Progress:** [██░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 8.7% (19/218)

| Status | Count |
|--------|-------|
| 🏆 Mastered | 19 |
| 💪 Independent | 0 |
| 👍 Recalled | 24 |
| ☑️ Attempted | 5 |
| ⭐ New | 170 |
| **Total** | **218** |

## Quick Start

```bash
# Log an attempt
python3 scripts/log_attempt.py --file "ml-rapid-fire/classical-ml/logistic-regression/01-what-is-logistic-regression.md" --time 2 --hints false --looked false --recall full

# Update this README
python3 scripts/generate_readme.py
```

## Flashcards

### Classical Ml

**Progress:** [█████████████░░░░░░░░░░░░░░░░░] 44.4% (4/9)

- 👍 [What is Logistic Regression](ml-rapid-fire/classical-ml/logistic-regression/01-what-is-logistic-regression.md) `1 attempts`
- 🏆 [Why Not Linear Regression](ml-rapid-fire/classical-ml/logistic-regression/02-why-not-linear-regression.md) `1 attempts`
- ☑️ [Sigmoid Function](ml-rapid-fire/classical-ml/logistic-regression/03-sigmoid-function.md) `1 attempts`
- 🏆 [How Trained](ml-rapid-fire/classical-ml/logistic-regression/04-how-trained.md) `1 attempts`
- 👍 [Coefficient Interpretation](ml-rapid-fire/classical-ml/logistic-regression/05-coefficient-interpretation.md) `1 attempts`
- 👍 [Decision Boundary](ml-rapid-fire/classical-ml/logistic-regression/06-decision-boundary.md) `1 attempts`
- 🏆 [Multi-class](ml-rapid-fire/classical-ml/logistic-regression/07-multi-class.md) `1 attempts`
- 🏆 [Loss Function](ml-rapid-fire/classical-ml/logistic-regression/08-loss-function.md) `1 attempts`
- ⭐ [Linearly Separable](ml-rapid-fire/classical-ml/logistic-regression/09-linearly-separable.md)

### Classification Metrics

**Progress:** [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 0.0% (0/10)

- ⭐ [Confusion Matrix](ml-rapid-fire/model-evaluation/classification-metrics/01-confusion-matrix.md)
- ⭐ [Accuracy](ml-rapid-fire/model-evaluation/classification-metrics/02-accuracy.md)
- ⭐ [Precision](ml-rapid-fire/model-evaluation/classification-metrics/03-precision.md)
- ⭐ [Recall](ml-rapid-fire/model-evaluation/classification-metrics/04-recall.md)
- ⭐ [F1 Score](ml-rapid-fire/model-evaluation/classification-metrics/05-f1-score.md)
- ⭐ [Precision-Recall Tradeoff](ml-rapid-fire/model-evaluation/classification-metrics/06-precision-recall-tradeoff.md)
- ⭐ [ROC Curve](ml-rapid-fire/model-evaluation/classification-metrics/07-roc-curve.md)
- ⭐ [AUC-ROC](ml-rapid-fire/model-evaluation/classification-metrics/08-auc-roc.md)
- ⭐ [PR Curve vs ROC](ml-rapid-fire/model-evaluation/classification-metrics/09-pr-curve-vs-roc.md)
- ⭐ [Specificity](ml-rapid-fire/model-evaluation/classification-metrics/10-specificity.md)

### Clustering

**Progress:** [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 0.0% (0/9)

- ⭐ [What is Clustering](ml-rapid-fire/classical-ml/clustering/01-what-is-clustering.md)
- ⭐ [K-Means Clustering](ml-rapid-fire/classical-ml/clustering/02-k-means.md)
- ⭐ [K-Means++ Initialization](ml-rapid-fire/classical-ml/clustering/03-k-means-plus-plus.md)
- ⭐ [Choosing K](ml-rapid-fire/classical-ml/clustering/04-choosing-k.md)
- ⭐ [DBSCAN](ml-rapid-fire/classical-ml/clustering/05-dbscan.md)
- ⭐ [Hierarchical Clustering](ml-rapid-fire/classical-ml/clustering/06-hierarchical-clustering.md)
- ⭐ [Linkage Methods](ml-rapid-fire/classical-ml/clustering/07-linkage-methods.md)
- ⭐ [Clustering Evaluation](ml-rapid-fire/classical-ml/clustering/08-clustering-evaluation.md)
- ⭐ [Clustering Algorithm Comparison](ml-rapid-fire/classical-ml/clustering/09-comparison.md)

### Cnns

**Progress:** [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 0.0% (0/9)

- ⭐ [What is a CNN](ml-rapid-fire/deep-learning/cnns/01-what-is-cnn.md)
- ⭐ [Convolution Operation](ml-rapid-fire/deep-learning/cnns/02-convolution-operation.md)
- ⭐ [CNN Hyperparameters](ml-rapid-fire/deep-learning/cnns/03-cnn-hyperparameters.md)
- ⭐ [Pooling](ml-rapid-fire/deep-learning/cnns/04-pooling.md)
- ⭐ [CNN Architecture](ml-rapid-fire/deep-learning/cnns/05-cnn-architecture.md)
- ⭐ [Receptive Field](ml-rapid-fire/deep-learning/cnns/06-receptive-field.md)
- ⭐ [1x1 Convolutions](ml-rapid-fire/deep-learning/cnns/07-1x1-convolutions.md)
- ⭐ [Famous CNN Architectures](ml-rapid-fire/deep-learning/cnns/08-famous-architectures.md)
- ⭐ [Transfer Learning in CNNs](ml-rapid-fire/deep-learning/cnns/09-transfer-learning.md)

### Cross Entropy

**Progress:** [███████░░░░░░░░░░░░░░░░░░░░░░░] 25.0% (2/8)

- 👍 [01-what-is-cross-entropy](ml-rapid-fire/classical-ml/cross-entropy/01-what-is-cross-entropy.md) `1 attempts`
- ☑️ [02-why-not-mse](ml-rapid-fire/classical-ml/cross-entropy/02-why-not-mse.md) `1 attempts`
- ☑️ [03-binary-cross-entropy-formula](ml-rapid-fire/classical-ml/cross-entropy/03-binary-cross-entropy-formula.md) `1 attempts`
- 🏆 [04-confident-correct](ml-rapid-fire/classical-ml/cross-entropy/04-confident-correct.md) `1 attempts`
- 👍 [05-confident-wrong](ml-rapid-fire/classical-ml/cross-entropy/05-confident-wrong.md) `1 attempts`
- ☑️ [06-categorical-cross-entropy](ml-rapid-fire/classical-ml/cross-entropy/06-categorical-cross-entropy.md) `1 attempts`
- 👍 [07-calculate-cross-entropy](ml-rapid-fire/classical-ml/cross-entropy/07-calculate-cross-entropy.md) `1 attempts`
- 🏆 [08-calculate-categorical-cross-entropy](ml-rapid-fire/classical-ml/cross-entropy/08-calculate-categorical-cross-entropy.md) `1 attempts`

### Decision Trees

**Progress:** [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 0.0% (0/16)

- ⭐ [What is a Decision Tree](ml-rapid-fire/classical-ml/decision-trees/01-what-is-decision-tree.md)
- ⭐ [How Decision Trees Split](ml-rapid-fire/classical-ml/decision-trees/02-how-splits-decided.md)
- ⭐ [Gini Impurity](ml-rapid-fire/classical-ml/decision-trees/03-gini-impurity.md)
- ⭐ [Information Gain / Entropy](ml-rapid-fire/classical-ml/decision-trees/04-information-gain.md)
- ⭐ [Preventing Overfitting in Decision Trees](ml-rapid-fire/classical-ml/decision-trees/05-prevent-overfitting.md)
- ⭐ [Decision Tree Pros and Cons](ml-rapid-fire/classical-ml/decision-trees/06-pros-cons.md)
- ⭐ [Ensemble Methods](ml-rapid-fire/classical-ml/decision-trees/07-ensemble-methods.md)
- ⭐ [Bagging](ml-rapid-fire/classical-ml/decision-trees/08-bagging.md)
- ⭐ [Random Forest](ml-rapid-fire/classical-ml/decision-trees/09-random-forest.md)
- ⭐ [Why Random Forest Reduces Variance](ml-rapid-fire/classical-ml/decision-trees/10-why-rf-reduces-variance.md)
- ⭐ [Boosting](ml-rapid-fire/classical-ml/decision-trees/11-boosting.md)
- ⭐ [Bagging vs Boosting](ml-rapid-fire/classical-ml/decision-trees/12-bagging-vs-boosting.md)
- ⭐ [AdaBoost](ml-rapid-fire/classical-ml/decision-trees/13-adaboost.md)
- ⭐ [Gradient Boosting](ml-rapid-fire/classical-ml/decision-trees/14-gradient-boosting.md)
- ⭐ [XGBoost](ml-rapid-fire/classical-ml/decision-trees/15-xgboost.md)
- ⭐ [Boosting Bias or Variance](ml-rapid-fire/classical-ml/decision-trees/16-boosting-bias-variance.md)

### Dimensionality Reduction

**Progress:** [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 0.0% (0/9)

- ⭐ [What is Dimensionality Reduction](ml-rapid-fire/classical-ml/dimensionality-reduction/01-what-is-dimensionality-reduction.md)
- ⭐ [PCA Overview](ml-rapid-fire/classical-ml/dimensionality-reduction/02-pca-overview.md)
- ⭐ [PCA Algorithm](ml-rapid-fire/classical-ml/dimensionality-reduction/03-pca-algorithm.md)
- ⭐ [Choosing PCA Components](ml-rapid-fire/classical-ml/dimensionality-reduction/04-choosing-components.md)
- ⭐ [PCA Limitations](ml-rapid-fire/classical-ml/dimensionality-reduction/05-pca-limitations.md)
- ⭐ [t-SNE Overview](ml-rapid-fire/classical-ml/dimensionality-reduction/06-tsne-overview.md)
- ⭐ [t-SNE Algorithm](ml-rapid-fire/classical-ml/dimensionality-reduction/07-tsne-algorithm.md)
- ⭐ [t-SNE Pitfalls](ml-rapid-fire/classical-ml/dimensionality-reduction/08-tsne-pitfalls.md)
- ⭐ [PCA vs t-SNE](ml-rapid-fire/classical-ml/dimensionality-reduction/09-pca-vs-tsne.md)

### Knn

**Progress:** [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 0.0% (0/9)

- ⭐ [What is KNN](ml-rapid-fire/classical-ml/knn/01-what-is-knn.md)
- ⭐ [KNN Prediction](ml-rapid-fire/classical-ml/knn/02-prediction.md)
- ⭐ [Distance Metrics](ml-rapid-fire/classical-ml/knn/03-distance-metrics.md)
- ⭐ [Choosing K](ml-rapid-fire/classical-ml/knn/04-choosing-k.md)
- ⭐ [Curse of Dimensionality](ml-rapid-fire/classical-ml/knn/05-curse-of-dimensionality.md)
- ⭐ [Feature Scaling for KNN](ml-rapid-fire/classical-ml/knn/06-feature-scaling.md)
- ⭐ [Weighted KNN](ml-rapid-fire/classical-ml/knn/07-weighted-knn.md)
- ⭐ [KNN Computational Complexity](ml-rapid-fire/classical-ml/knn/08-computational-complexity.md)
- ⭐ [KNN Pros and Cons](ml-rapid-fire/classical-ml/knn/09-pros-cons.md)

### Linear Regression

**Progress:** [█████████████░░░░░░░░░░░░░░░░░] 45.5% (5/11)

- 🏆 [01-what-is-linear-regression](ml-rapid-fire/classical-ml/linear-regression/01-what-is-linear-regression.md) `1 attempts`
- 🏆 [02-simple-vs-multiple](ml-rapid-fire/classical-ml/linear-regression/02-simple-vs-multiple.md) `1 attempts`
- 👍 [03-linear-regression-formula](ml-rapid-fire/classical-ml/linear-regression/03-linear-regression-formula.md) `1 attempts`
- 🏆 [04-loss-function](ml-rapid-fire/classical-ml/linear-regression/04-loss-function.md) `1 attempts`
- 👍 [05-ordinary-least-squares](ml-rapid-fire/classical-ml/linear-regression/05-ordinary-least-squares.md) `1 attempts`
- ☑️ [06-gradient-descent-for-lr](ml-rapid-fire/classical-ml/linear-regression/06-gradient-descent-for-lr.md) `1 attempts`
- 🏆 [07-coefficient-interpretation](ml-rapid-fire/classical-ml/linear-regression/07-coefficient-interpretation.md) `1 attempts`
- 👍 [08-assumptions](ml-rapid-fire/classical-ml/linear-regression/08-assumptions.md) `1 attempts`
- 👍 [09-ridge-vs-lasso](ml-rapid-fire/classical-ml/linear-regression/09-ridge-vs-lasso.md) `1 attempts`
- 👍 [10-r-squared](ml-rapid-fire/classical-ml/linear-regression/10-r-squared.md) `1 attempts`
- 🏆 [11-mse-formula](ml-rapid-fire/classical-ml/linear-regression/11-mse-formula.md) `1 attempts`

### Loss Functions

**Progress:** [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 0.0% (0/10)

- ⭐ [What is a Loss Function](ml-rapid-fire/model-evaluation/loss-functions/01-what-is-loss-function.md)
- ⭐ [MSE Loss](ml-rapid-fire/model-evaluation/loss-functions/02-mse-loss.md)
- ⭐ [MAE Loss](ml-rapid-fire/model-evaluation/loss-functions/03-mae-loss.md)
- ⭐ [Binary Cross-Entropy](ml-rapid-fire/model-evaluation/loss-functions/04-binary-cross-entropy.md)
- ⭐ [Categorical Cross-Entropy](ml-rapid-fire/model-evaluation/loss-functions/05-categorical-cross-entropy.md)
- ⭐ [Hinge Loss](ml-rapid-fire/model-evaluation/loss-functions/06-hinge-loss.md)
- ⭐ [Huber Loss](ml-rapid-fire/model-evaluation/loss-functions/07-huber-loss.md)
- ⭐ [Log Loss vs Cross-Entropy](ml-rapid-fire/model-evaluation/loss-functions/08-log-loss-vs-cross-entropy.md)
- ⭐ [Softmax Cross-Entropy](ml-rapid-fire/model-evaluation/loss-functions/09-softmax-cross-entropy.md)
- ⭐ [Choosing a Loss Function](ml-rapid-fire/model-evaluation/loss-functions/10-choosing-loss-function.md)

### Ml Basics

**Progress:** [███████████░░░░░░░░░░░░░░░░░░░] 38.1% (8/21)

- 🏆 [01-what-is-ml](ml-rapid-fire/fundamentals/ml-basics/01-what-is-ml.md) `1 attempts`
- 🏆 [02-traditional-vs-ml](ml-rapid-fire/fundamentals/ml-basics/02-traditional-vs-ml.md) `1 attempts`
- 👍 [03-three-components](ml-rapid-fire/fundamentals/ml-basics/03-three-components.md) `1 attempts`
- 🏆 [04-types-of-learning](ml-rapid-fire/fundamentals/ml-basics/04-types-of-learning.md) `1 attempts`
- 👍 [05-classification-vs-regression](ml-rapid-fire/fundamentals/ml-basics/05-classification-vs-regression.md) `1 attempts`
- 🏆 [06-what-is-a-model](ml-rapid-fire/fundamentals/ml-basics/06-what-is-a-model.md) `1 attempts`
- 🏆 [07-what-is-loss-function](ml-rapid-fire/fundamentals/ml-basics/07-what-is-loss-function.md) `1 attempts`
- 👍 [08-what-is-optimization](ml-rapid-fire/fundamentals/ml-basics/08-what-is-optimization.md) `1 attempts`
- 👍 [09-loss-vs-metric](ml-rapid-fire/fundamentals/ml-basics/09-loss-vs-metric.md) `1 attempts`
- 👍 [10-params-vs-hyperparams](ml-rapid-fire/fundamentals/ml-basics/10-params-vs-hyperparams.md) `1 attempts`
- 🏆 [11-what-is-regularization](ml-rapid-fire/fundamentals/ml-basics/11-what-is-regularization.md) `1 attempts`
- 🏆 [12-training-vs-inference](ml-rapid-fire/fundamentals/ml-basics/12-training-vs-inference.md) `1 attempts`
- 🏆 [13-overfitting-underfitting](ml-rapid-fire/fundamentals/ml-basics/13-overfitting-underfitting.md) `1 attempts`
- 👍 [14-bias-variance](ml-rapid-fire/fundamentals/ml-basics/14-bias-variance.md) `1 attempts`
- 👍 [15-when-to-use-ml](ml-rapid-fire/fundamentals/ml-basics/15-when-to-use-ml.md) `1 attempts`
- 👍 [Bias-Variance Decomposition](ml-rapid-fire/fundamentals/ml-basics/16-bias-variance-decomposition.md) `1 attempts`
- 👍 [Diagnosing Bias vs Variance](ml-rapid-fire/fundamentals/ml-basics/17-diagnosing-bias-variance.md) `1 attempts`
- 👍 [Causes of High Variance](ml-rapid-fire/fundamentals/ml-basics/18-causes-high-variance.md) `1 attempts`
- 👍 [How to Reduce Variance](ml-rapid-fire/fundamentals/ml-basics/19-reduce-variance.md) `1 attempts`
- 👍 [Causes of High Bias](ml-rapid-fire/fundamentals/ml-basics/20-causes-high-bias.md) `1 attempts`
- 👍 [How to Reduce Bias](ml-rapid-fire/fundamentals/ml-basics/21-reduce-bias.md) `1 attempts`

### Model Selection

**Progress:** [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 0.0% (0/10)

- ⭐ [What is Hyperparameter Tuning](ml-rapid-fire/model-evaluation/model-selection/01-what-is-hyperparameter-tuning.md)
- ⭐ [Grid Search](ml-rapid-fire/model-evaluation/model-selection/02-grid-search.md)
- ⭐ [Random Search](ml-rapid-fire/model-evaluation/model-selection/03-random-search.md)
- ⭐ [Bayesian Optimization](ml-rapid-fire/model-evaluation/model-selection/04-bayesian-optimization.md)
- ⭐ [Cross-Validation for Model Selection](ml-rapid-fire/model-evaluation/model-selection/05-cv-for-model-selection.md)
- ⭐ [Learning Curves for Diagnosis](ml-rapid-fire/model-evaluation/model-selection/06-learning-curves.md)
- ⭐ [Validation Curve](ml-rapid-fire/model-evaluation/model-selection/07-validation-curve.md)
- ⭐ [Early Stopping as Model Selection](ml-rapid-fire/model-evaluation/model-selection/08-early-stopping.md)
- ⭐ [Regularization Path](ml-rapid-fire/model-evaluation/model-selection/09-regularization-path.md)
- ⭐ [Information Criteria (AIC/BIC)](ml-rapid-fire/model-evaluation/model-selection/10-information-criteria.md)

### Naive Bayes

**Progress:** [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 0.0% (0/9)

- ⭐ [What is Naive Bayes](ml-rapid-fire/classical-ml/naive-bayes/01-what-is-naive-bayes.md)
- ⭐ [Bayes Theorem](ml-rapid-fire/classical-ml/naive-bayes/02-bayes-theorem.md)
- ⭐ [The Naive Assumption](ml-rapid-fire/classical-ml/naive-bayes/03-naive-assumption.md)
- ⭐ [Types of Naive Bayes](ml-rapid-fire/classical-ml/naive-bayes/04-types-of-naive-bayes.md)
- ⭐ [Gaussian Naive Bayes](ml-rapid-fire/classical-ml/naive-bayes/05-gaussian-naive-bayes.md)
- ⭐ [Multinomial Naive Bayes](ml-rapid-fire/classical-ml/naive-bayes/06-multinomial-naive-bayes.md)
- ⭐ [Laplace Smoothing](ml-rapid-fire/classical-ml/naive-bayes/07-laplace-smoothing.md)
- ⭐ [Log Probabilities](ml-rapid-fire/classical-ml/naive-bayes/08-log-probabilities.md)
- ⭐ [Naive Bayes Pros and Cons](ml-rapid-fire/classical-ml/naive-bayes/09-pros-cons.md)

### Neural Network Basics

**Progress:** [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 0.0% (0/9)

- ⭐ [What is a Neural Network](ml-rapid-fire/deep-learning/neural-network-basics/01-what-is-neural-network.md)
- ⭐ [Forward Pass](ml-rapid-fire/deep-learning/neural-network-basics/02-forward-pass.md)
- ⭐ [Backpropagation](ml-rapid-fire/deep-learning/neural-network-basics/03-backpropagation.md)
- ⭐ [Why Activation Functions](ml-rapid-fire/deep-learning/neural-network-basics/04-why-activation-functions.md)
- ⭐ [Common Activation Functions](ml-rapid-fire/deep-learning/neural-network-basics/05-common-activations.md)
- ⭐ [Loss Functions](ml-rapid-fire/deep-learning/neural-network-basics/06-loss-functions.md)
- ⭐ [Weight Initialization](ml-rapid-fire/deep-learning/neural-network-basics/07-weight-initialization.md)
- ⭐ [Training Loop](ml-rapid-fire/deep-learning/neural-network-basics/08-training-loop.md)
- ⭐ [Vanishing and Exploding Gradients](ml-rapid-fire/deep-learning/neural-network-basics/09-vanishing-exploding-gradients.md)

### Optimizers

**Progress:** [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 0.0% (0/9)

- ⭐ [What is an Optimizer](ml-rapid-fire/deep-learning/optimizers/01-what-is-optimizer.md)
- ⭐ [Gradient Descent Variants](ml-rapid-fire/deep-learning/optimizers/02-gradient-descent-variants.md)
- ⭐ [Learning Rate](ml-rapid-fire/deep-learning/optimizers/03-learning-rate.md)
- ⭐ [Learning Rate Schedules](ml-rapid-fire/deep-learning/optimizers/04-learning-rate-schedules.md)
- ⭐ [Momentum](ml-rapid-fire/deep-learning/optimizers/05-momentum.md)
- ⭐ [RMSprop](ml-rapid-fire/deep-learning/optimizers/06-rmsprop.md)
- ⭐ [Adam Optimizer](ml-rapid-fire/deep-learning/optimizers/07-adam.md)
- ⭐ [Choosing an Optimizer](ml-rapid-fire/deep-learning/optimizers/08-choosing-optimizer.md)
- ⭐ [Common Optimizer Problems](ml-rapid-fire/deep-learning/optimizers/09-common-problems.md)

### Regression Metrics

**Progress:** [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 0.0% (0/7)

- ⭐ [Mean Squared Error](ml-rapid-fire/model-evaluation/regression-metrics/01-mse.md)
- ⭐ [Root Mean Squared Error](ml-rapid-fire/model-evaluation/regression-metrics/02-rmse.md)
- ⭐ [Mean Absolute Error](ml-rapid-fire/model-evaluation/regression-metrics/03-mae.md)
- ⭐ [MSE vs MAE](ml-rapid-fire/model-evaluation/regression-metrics/04-mse-vs-mae.md)
- ⭐ [R-Squared](ml-rapid-fire/model-evaluation/regression-metrics/05-r-squared.md)
- ⭐ [R-Squared Limitations](ml-rapid-fire/model-evaluation/regression-metrics/06-r-squared-limitations.md)
- ⭐ [Adjusted R-Squared](ml-rapid-fire/model-evaluation/regression-metrics/07-adjusted-r-squared.md)

### Regularization

**Progress:** [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 0.0% (0/16)

- ⭐ [L2 (Ridge) Penalty Formula](ml-rapid-fire/classical-ml/regularization/01-l2-ridge-formula.md)
- ⭐ [L1 (Lasso) Penalty Formula](ml-rapid-fire/classical-ml/regularization/02-l1-lasso-formula.md)
- ⭐ [Why L1 Produces Sparsity](ml-rapid-fire/classical-ml/regularization/03-why-l1-sparse.md)
- ⭐ [Why L2 Only Shrinks Weights](ml-rapid-fire/classical-ml/regularization/04-why-l2-shrinks.md)
- ⭐ [When to Choose L1 vs L2](ml-rapid-fire/classical-ml/regularization/05-when-l1-vs-l2.md)
- ⭐ [Elastic Net](ml-rapid-fire/classical-ml/regularization/06-elastic-net.md)
- ⭐ [Regularization Hyperparameter](ml-rapid-fire/classical-ml/regularization/07-lambda-hyperparameter.md)
- ⭐ [What is Regularization](ml-rapid-fire/deep-learning/regularization/01-what-is-regularization.md)
- ⭐ [Dropout](ml-rapid-fire/deep-learning/regularization/02-dropout.md)
- ⭐ [Why Dropout Works](ml-rapid-fire/deep-learning/regularization/03-why-dropout-works.md)
- ⭐ [Batch Normalization](ml-rapid-fire/deep-learning/regularization/04-batch-normalization.md)
- ⭐ [Why Batch Norm Works](ml-rapid-fire/deep-learning/regularization/05-why-batch-norm-works.md)
- ⭐ [Early Stopping](ml-rapid-fire/deep-learning/regularization/06-early-stopping.md)
- ⭐ [Data Augmentation](ml-rapid-fire/deep-learning/regularization/07-data-augmentation.md)
- ⭐ [Weight Decay](ml-rapid-fire/deep-learning/regularization/08-weight-decay.md)
- ⭐ [Label Smoothing](ml-rapid-fire/deep-learning/regularization/09-label-smoothing.md)

### Rnns

**Progress:** [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 0.0% (0/9)

- ⭐ [What is an RNN](ml-rapid-fire/deep-learning/rnns/01-what-is-rnn.md)
- ⭐ [RNN Applications](ml-rapid-fire/deep-learning/rnns/02-rnn-applications.md)
- ⭐ [RNN Limitations](ml-rapid-fire/deep-learning/rnns/03-rnn-limitations.md)
- ⭐ [LSTM](ml-rapid-fire/deep-learning/rnns/04-lstm.md)
- ⭐ [LSTM Gates](ml-rapid-fire/deep-learning/rnns/05-lstm-gates.md)
- ⭐ [GRU](ml-rapid-fire/deep-learning/rnns/06-gru.md)
- ⭐ [Sequence-to-Sequence](ml-rapid-fire/deep-learning/rnns/07-seq2seq.md)
- ⭐ [Bidirectional RNNs](ml-rapid-fire/deep-learning/rnns/08-bidirectional-rnn.md)
- ⭐ [Teacher Forcing](ml-rapid-fire/deep-learning/rnns/09-teacher-forcing.md)

### Svm

**Progress:** [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 0.0% (0/9)

- ⭐ [What is an SVM](ml-rapid-fire/classical-ml/svm/01-what-is-svm.md)
- ⭐ [Margin and Support Vectors](ml-rapid-fire/classical-ml/svm/02-margin-support-vectors.md)
- ⭐ [Hard Margin vs Soft Margin](ml-rapid-fire/classical-ml/svm/03-hard-vs-soft-margin.md)
- ⭐ [The Kernel Trick](ml-rapid-fire/classical-ml/svm/04-kernel-trick.md)
- ⭐ [Common Kernel Functions](ml-rapid-fire/classical-ml/svm/05-common-kernels.md)
- ⭐ [The C Parameter](ml-rapid-fire/classical-ml/svm/06-c-parameter.md)
- ⭐ [The Gamma Parameter](ml-rapid-fire/classical-ml/svm/07-gamma-parameter.md)
- ⭐ [SVM Pros and Cons](ml-rapid-fire/classical-ml/svm/08-pros-cons.md)
- ⭐ [Multiclass SVM](ml-rapid-fire/classical-ml/svm/09-multiclass.md)

### Transformers

**Progress:** [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 0.0% (0/9)

- ⭐ [What is Attention](ml-rapid-fire/deep-learning/transformers/01-what-is-attention.md)
- ⭐ [Scaled Dot-Product Attention](ml-rapid-fire/deep-learning/transformers/02-scaled-dot-product-attention.md)
- ⭐ [Self-Attention vs Cross-Attention](ml-rapid-fire/deep-learning/transformers/03-self-vs-cross-attention.md)
- ⭐ [Multi-Head Attention](ml-rapid-fire/deep-learning/transformers/04-multi-head-attention.md)
- ⭐ [Positional Encoding](ml-rapid-fire/deep-learning/transformers/05-positional-encoding.md)
- ⭐ [Transformer Architecture](ml-rapid-fire/deep-learning/transformers/06-transformer-architecture.md)
- ⭐ [BERT Pre-training](ml-rapid-fire/deep-learning/transformers/07-bert-pretraining.md)
- ⭐ [GPT vs BERT](ml-rapid-fire/deep-learning/transformers/08-gpt-vs-bert.md)
- ⭐ [Encoder vs Decoder Models](ml-rapid-fire/deep-learning/transformers/09-encoder-vs-decoder-models.md)

### Validation

**Progress:** [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 0.0% (0/10)

- ⭐ [Train/Test Split](ml-rapid-fire/model-evaluation/validation/01-train-test-split.md)
- ⭐ [Validation Set Purpose](ml-rapid-fire/model-evaluation/validation/02-validation-set-purpose.md)
- ⭐ [K-Fold Cross-Validation](ml-rapid-fire/model-evaluation/validation/03-k-fold-cross-validation.md)
- ⭐ [Stratified K-Fold](ml-rapid-fire/model-evaluation/validation/04-stratified-k-fold.md)
- ⭐ [Leave-One-Out Cross-Validation](ml-rapid-fire/model-evaluation/validation/05-loocv.md)
- ⭐ [Holdout vs Cross-Validation](ml-rapid-fire/model-evaluation/validation/06-holdout-vs-cv.md)
- ⭐ [Data Leakage](ml-rapid-fire/model-evaluation/validation/07-data-leakage.md)
- ⭐ [Time Series Validation](ml-rapid-fire/model-evaluation/validation/08-time-series-validation.md)
- ⭐ [Bias-Variance in Cross-Validation](ml-rapid-fire/model-evaluation/validation/09-bias-variance-cv.md)
- ⭐ [Nested Cross-Validation](ml-rapid-fire/model-evaluation/validation/10-nested-cross-validation.md)

---

*Last updated: 2025-11-28 19:42:47*