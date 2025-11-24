# ML Interview Dojo

Personal repository for preparing for machine learning interviews.

## Source Material

Questions are from [Machine Learning Interviews Book](https://huyenchip.com/ml-interviews-book/) by Chip Huyen:
- Questions: https://github.com/chiphuyen/ml-interviews-book/tree/master/contents

## Progress Scorecard

### Overall Mastery

```
[░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 0.0% (0/23)
```

### Card Status

| Status | Count | Percentage |
|--------|-------|------------|
| 🏆 Mastered | 0 | 0.0% |
| 💪 Learning | 0 | 0.0% |
| ⭐ New | 23 | 100.0% |
| **Total** | **23** | **100%** |


## Quick Start

```bash
# Start a review session
python3 srs.py review

# View your stats
python3 srs.py stats

# Update this README
python3 scripts/generate_readme.py
```

## How the SRS Works

This uses a **queue-based spaced repetition system** (not date-based like Anki):

- **No due dates**: Cards are prioritized in a smart queue based on performance
- **No pile-up**: Come back after months and continue right where you left off
- **Adaptive**: Struggles with a card? It gets higher priority automatically
- **Mastery tracking**: Cards graduate from New → Learning → Mastered

**Mastery Criteria**: 3+ consecutive reviews with score ≥4, spaced at least 1 hour apart

## Status Legend

- 🏆 **Mastered**: Consistently perfect recall
- 💪 **Strong**: Average score ≥4.0, still in practice
- 👍 **Learning**: Average score ≥3.0, making progress
- 📖 **Practicing**: Reviewed but needs more work
- ⭐ **New**: Not yet reviewed

## Topics by Category


### 01 Basics

**Progress:** [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 0.0% (0/23) | 🏆 0 | 💪 0 | ⭐ 23

- ⭐ [01-learning-types](ml-workflows/01-basics/01-learning-types.md): Explain supervised, unsupervised, weakly supervised, semi-supervised, and active...
- ⭐ [02-empirical-risk](ml-workflows/01-basics/02-empirical-risk.md): What's the risk in empirical risk minimization?
- ⭐ [03-why-empirical](ml-workflows/01-basics/03-why-empirical.md): Why is it empirical?
- ⭐ [04-minimize-risk](ml-workflows/01-basics/04-minimize-risk.md): How do we minimize that risk?
- ⭐ [05-occams-razor](ml-workflows/01-basics/05-occams-razor.md): "Occam's razor states that when the simple explanation and complex explanation b...
- ⭐ [06-deep-learning-conditions](ml-workflows/01-basics/06-deep-learning-conditions.md): What are the conditions that allowed deep learning to gain popularity in the las...
- ⭐ [07-wide-vs-deep](ml-workflows/01-basics/07-wide-vs-deep.md): If we have a wide NN and a deep NN with the same number of parameters, which one...
- ⭐ [08-universal-approximation](ml-workflows/01-basics/08-universal-approximation.md): "The Universal Approximation Theorem states that a neural network with 1 hidden ...
- ⭐ [09-saddle-points-local-minima](ml-workflows/01-basics/09-saddle-points-local-minima.md): What are saddle points and local minima? Which are thought to cause more problem...
- ⭐ [10-parameters-vs-hyperparameters](ml-workflows/01-basics/10-parameters-vs-hyperparameters.md): What are the differences between parameters and hyperparameters?
- ⭐ [11-hyperparameter-tuning-importance](ml-workflows/01-basics/11-hyperparameter-tuning-importance.md): Why is hyperparameter tuning important?
- ⭐ [12-hyperparameter-tuning-algorithm](ml-workflows/01-basics/12-hyperparameter-tuning-algorithm.md): Explain the algorithm for tuning hyperparameters.
- ⭐ [13-classification-vs-regression](ml-workflows/01-basics/13-classification-vs-regression.md): What makes a classification problem different from a regression problem?
- ⭐ [14-classification-regression-conversion](ml-workflows/01-basics/14-classification-regression-conversion.md): Can a classification problem be turned into a regression problem and vice versa?
- ⭐ [15-parametric-vs-nonparametric](ml-workflows/01-basics/15-parametric-vs-nonparametric.md): What's the difference between parametric and non-parametric methods? Give exampl...
- ⭐ [16-when-parametric-vs-nonparametric](ml-workflows/01-basics/16-when-parametric-vs-nonparametric.md): When should we use parametric versus non-parametric methods?
- ⭐ [17-ensembling-benefits](ml-workflows/01-basics/17-ensembling-benefits.md): Why does ensembling independently trained models generally improve performance?
- ⭐ [18-l1-vs-l2-regularization](ml-workflows/01-basics/18-l1-vs-l2-regularization.md): Why does L1 regularization tend to lead to sparsity while L2 regularization push...
- ⭐ [19-production-degradation](ml-workflows/01-basics/19-production-degradation.md): Why does an ML model's performance degrade in production?
- ⭐ [20-deploying-large-models](ml-workflows/01-basics/20-deploying-large-models.md): What problems might we run into when deploying large machine learning models?
- ⭐ [21-production-performance-hypotheses](ml-workflows/01-basics/21-production-performance-hypotheses.md): What are your hypotheses about the causes of good test performance but poor prod...
- ⭐ [22-validate-hypotheses](ml-workflows/01-basics/22-validate-hypotheses.md): How do you validate whether your hypotheses are correct?
- ⭐ [23-address-causes](ml-workflows/01-basics/23-address-causes.md): How would you address the identified causes?

---

*Last updated: 2025-11-24 01:17:47*

*Generated by [scripts/generate_readme.py](scripts/generate_readme.py)*