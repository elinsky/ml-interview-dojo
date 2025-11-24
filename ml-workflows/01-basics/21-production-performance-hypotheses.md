# Question

What are your hypotheses about the causes of good test performance but poor production performance?

# Answer

When a model performs well on test data but poorly in production, the root cause is almost always a violation of the fundamental assumptions underlying model evaluation and generalization. The core assumption—that the probability distribution over examples remains stationary over time—is broken.

**Primary Hypotheses:**

**1. Stationarity Assumption Violated (Distribution Shift)**

**Hypothesis**: The probability distribution over examples has changed between test time and production time.

**From the notes**: "There is a probability distribution over examples that remains stationary over time." When this assumption is violated (non-stationary distribution), test performance no longer predicts production performance.

**Specific manifestations**:

- **Temporal drift**: Test set from 2022, production is 2024 with shifted patterns
- **Population shift**: Test data from one user segment, production serves different segment
- **Environmental changes**: External factors (economy, regulations, technology) change P(X) or P(Y|X)

**Connection to statistical learning**: The Y = f(X) + ε framework (see notes) assumes f is fixed. When f changes over time (concept drift) or when the distribution of X changes (data drift), the learned model no longer generalizes.

**2. Test Set Not Representative of Production (Sample Bias)**

**Hypothesis**: Test set suffers from selection bias—it's not a truly random sample from the production distribution.

**From the notes**: Sample bias occurs when "not having a truly random sample." The three criteria for random samples are:

1. Equal likelihood principle: every unit has equal probability of being chosen
2. Observer can't predict who will be chosen
3. Must be possible to choose every combination

**Specific causes**:

- **Geographic bias**: Test data from US only, production serves globally
- **Temporal bias**: Random train/test split on time-series data (violates temporal structure)
- **Cherry-picking**: Test set curated to avoid edge cases
- **Convenience sampling**: Test data from easily accessible sources, not representative of production

**Consequence**: Test set doesn't capture the variability in production, leading to overly optimistic performance estimates.

**3. Test Set Too Small (Sample Error)**

**Hypothesis**: Test set has high sample error due to insufficient size, giving unreliable performance estimates.

**From the notes**: "Sample error is due to randomness. You can reduce sample error by increasing your sample size."

**Specific issues**:

- High variance in test metrics (especially for rare cases)
- "If little data is available, then your validation and test sets may contain too few samples to be statistically representative of the data at hand"
- Bootstrap can measure this uncertainty: "The bootstrap allows you to estimate the standard error of a sample statistic"

**Connection to cross-validation**: K-fold is "helpful when the performance of your model shows significant variance based on your train-test split"—indicating sample size or representativeness issues.

**4. Validation Set Leakage / Information Leakage**

**Hypothesis**: Test performance is artificially inflated because information leaked from test set into model development.

**From the notes**: "Remember though, that every time you get feedback from the validation set and use it to tweak hyperparameters, you leak information."

**Specific causes**:

- **Hyperparameter tuning on test set**: Used test set for model selection, contaminating it
- **Data leakage**: Test examples or near-duplicates in training data
- **Feature leakage**: Features using future information or target proxies
- **Temporal leakage**: Using future data to predict past events

**Violation of validation protocol**: "Leave the test set alone until you have your final model." If this principle is violated, test set no longer provides unbiased generalization estimate.

**5. Train/Test Split Methodology Flawed**

**Hypothesis**: Used inappropriate splitting strategy that doesn't respect data structure.

**Specific examples**:

- Random split on grouped data (e.g., multiple samples per patient—test "patients" seen in training)
- Random split on time-series (violates temporal causality)
- Stratification on wrong variable (stratified by class but not by important covariate)

**6. Training/Serving Skew**

**Hypothesis**: Model or preprocessing differs between test environment and production.

**Specific causes**:

- Different feature computation logic
- Different preprocessing statistics (normalization using train vs. production stats)
- Model version mismatch
- Missing features at serving time

**Diagnostic Approach:**

From the validation workflow (see notes):

1. **Decide on evaluation protocol**: Hold-out vs. K-fold vs. other
2. **Check stationarity**: Does distribution change over time?
3. **Verify randomness**: Does test set meet random sampling criteria?
4. **Estimate uncertainty**: Use bootstrap or cross-validation to measure variance
5. **Audit for leakage**: Ensure strict train/test separation

---

## Extracts from my notes

### 202104170817 Stationarity Assumption.txt

```
From Russell and Norvig [@russell2010artificial, p. 708]:

> There is a probability distribution over examples that remains stationary over time.
```

### 201908031553 The two major types of error in sampling are sample bias and sample error.txt

```
There are two major types of error in sampling: [@watt2002research, p. 62-81]

1. Sample error is due to randomness. You can reduce sample error by increasing your sample size.
2. Sample bias. Sample bias has two sub-components: Selection bias and response bias.  You introduce selection bias by not having a truly random sample.  Response bias is introduced when people opt-out of your survey.
```

### 201908031541 Three criteria are necessary for selecting random samples.txt

```
Three criteria are necessary for selecting random samples: [@watt2002research, p. 62-81]

1. Equal likelihood principle must be met. Every unit must have an equal probability of being chosen.
2. The observer shouldn't be able to predict who will be chosen.
3. It must be possible to choose a sample of every possible combination of people.
```

### 202101241752 Chollet's Machine Learning Workflow.txt

```
Chollet outlines his 'universal workflow of machine learning' as follows [@chollet2018deep, p. 111]:

1. Define the problem
2. Choose a measure of success
3. Decide on an evaluation protocol
    - Hold-out validation set (see [[202101241506 Simple Hold-Out Validation]])
    - K-fold cross validation (see [[202101080742 Cross Validation (K-Fold)]])
4. Prepare your data
5. Develop a model that does better than a baseline
6. Develop a model that overfits
    - ```Remember that the universal tension in machine learning is between optimization and generalization; the ideal model is one that stands right at the border between underfitting and overfitting; between undercapacity and overcapacity.  To figure out where this border lies, first you need to cross it.```
7. Regularize your model and tune hyperparameters
    - Remember though, that every time you get feedback from the validation set and use it to tweak hyperparameters, you leak information.
```

### 202101241506 Simple Hold-Out Validation.txt

```
This is the simplest validation technique.  Train on the training set.  Evaluate your performance on the validation set.  At this point you can tune your model, retrain it on the training set, and re-evaluate performance on the validation set.  Only once you have a final model do you evaluate performance on the test set.

From François Chollet [@chollet2018deep, p. 99]:

> This is the simplest evaluation protocol, and it suffers from one flaw; if little data is available, then your validation and test sets may contain too few samples to be statistically representative of the data at hand.
```

### 202101080707 The Bootstrap.txt

```
The bootstrap is a resampling technique that allows you to estimate the standard error of a sample statistic [@wilcox2010fundamentals, ch. 6].  As an example, say you sample 100 people and calculate the median height.  You could use bootstrapping to measure the standard error of that median (e.g. how much variation does that median exhibit? or how much uncertainty is there in this measurement of the median?).  The bootstrap works particularly well on non-normal distributions.  It is a robust method.  It is also a very general method.  As an example, you could use it to estimate the standard error of a regression coefficient.
```

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

After evaluating the performance of a model, you can tweak the hyperparameters, and follow the same process again.  Only after you have chosen a final model do you evaluate on

**Note**:  These models are thrown away when you are done.  Usually you would then train your final model over **all** the training data.  Then do your final evaluation of the model on the test set, only using the test set once.


K-Fold Cross validation works particularly well when you have a small dataset because it minimizes the impact of a single split.  From François Chollet [@chollet2018deep, p. 99]:

> This method is helpful when the performance of your model shows significant variance based on your train-test split.
```

### 202106191014 Statistical Learning.txt

```
From _An Introduction to Statistical Learning_ [@james2013introduction, p. 16]:

> More generally, supposed that we observe a quantitative response $Y$ and $p$ different predictors, $X_1, X_2, \dots, X_p$. We assume that there is some relationship between $Y$ and $X = (X_1, X_2, \dots, X_p), which can be written in the very general form
>
> $$Y = f(X) + \epsilon$$
>
> Here $f$ is some fixed but unknown function of $X_1, \dots , X_p$, and $\epsilon$ is a random error term, which is independent of $X$ and has mean zero. In this formulation, $f$ represents the systematic information that $X$ provides about $Y$.

Note $f$ is the best that we can do _given only_ $X$. If we were to have more predictor variables in $X$ that provided information, we would be able to produce a better $f$ and reduce $\epsilon$. In this sense, the irreducible error $\epsilon$ cannot be reduced given $X$. But if you augment $X$, it _can_ be reduced.

From _An Introduction to Statistical Learning_ [@james2013introduction, p. 17:

> In essence, statistical learning refers to a set of approaches for estimating $f$.
```

## Gaps filled by me (not from notes)

The specific production scenarios (geographic bias, temporal drift, training/serving skew, cherry-picking test data) and the diagnostic approach were synthesized from ML engineering best practices. My notes provided the foundational statistical concepts (stationarity assumption, sample bias vs. sample error, random sampling criteria, validation leakage, bootstrap for uncertainty) that explain WHY test/production mismatch occurs, which I connected to concrete production debugging scenarios.
