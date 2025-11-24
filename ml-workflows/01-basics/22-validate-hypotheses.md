# Question

How do you validate whether your hypotheses are correct?

# Answer

Validating hypotheses about production model failures requires systematic measurement, model criticism, and iterative refinement. The validation process follows principles from statistical model validation, exploratory data analysis, and measurement theory: observe data → diagnose problems → test assumptions → refine hypotheses.

**Core Validation Principles:**

**1. Measurement as Uncertainty Reduction**

Validation is fundamentally about measurement. "Measurement is a quantified reduction in uncertainty based on your observations." You can never achieve complete certainty, but systematic observation reduces uncertainty about which hypothesis is correct.

Key insight: "Uncertainty is a feature of the observer, not the thing being measured." We have uncertainty about whether our hypothesis is correct. Observations (comparing distributions, analyzing residuals, measuring performance) reduce that uncertainty.

**2. Iterative Model Criticism**

Model validation is an iterative process. We have inputs (hypotheses, data, statistical techniques, assumptions) and outputs (test statistics, performance metrics, graphical displays). We "diagnose, validate, and criticize" the outputs, then modify inputs and repeat until reaching a satisfactory result.

The goal is to answer three questions:

1. What are the required assumptions for each hypothesis?
2. For each assumption, how do we determine whether it's valid?
3. What can we do if assumptions don't hold?

**Validation Methods by Hypothesis Type:**

**1. Validating Distribution Shift (Stationarity Violation)**

**Tests:**

- **Visual comparison**: Plot feature distributions over time
  - Look for gradual drift or sudden shifts
- **Statistical tests**: Compare P(X)_test vs P(X)_production
  - Two-sample tests for continuous features
  - Chi-square tests for categorical features
- **Performance over time**: Plot accuracy/precision/recall vs. deployment date
  - Pattern: Monotonic or stepped degradation indicates drift

**From model criticism**: Use exploratory data analysis to "discover patterns in the data." Visualize distributions before and after the shift to understand "what is going on here?"

**2. Validating Sample Bias**

**Tests:**

- **Representativeness check**: Verify test set satisfies random sampling criteria
  - Equal likelihood principle met?
  - Observer can't predict selection?
  - All combinations possible?
- **Stratification analysis**: Compare subgroup distributions
- **Bootstrap confidence intervals**: Estimate uncertainty in test metrics
  - "The bootstrap allows you to estimate the standard error of a sample statistic"
  - Wide intervals indicate high sample error

**Connection to measurement**: Before validating, take three measurements:

1. Uncertainty: Measure 90% confidence interval on the variable
2. Risk: What's the downside?
3. Value of information: How much can we justify spending to reduce uncertainty?

**3. Validating Model Assumptions Through Residual Analysis**

**Tests:**

- **Residual plots**: Primary diagnostic for validating model assumptions
  - Look for outliers on x and y axes
  - Check for curved patterns (indicates wrong functional form)
  - Check for heteroskedasticity (changing variance)
  - Check normality of residuals

**From the notes**: "We are usually happier about asserting a regression relation if the relation is still apparent after a few observations (any ones) have been deleted." Removing outliers shouldn't destroy the relationship.

**Key insight**: "Errors vs Residuals" - Residuals are estimates of true errors. We use residuals to diagnose problems because true errors are unobservable. Residuals = observed - predicted.

**Iterative process**: "The exploratory data analyst conducts an iterative process of suggesting a tentative model, examining the residuals from the model to assess model adequacy, and modifying the model in view of the residual analysis."

**4. Validating Classification Performance**

**Tests:**

- **ROC curves**: Assess tradeoff between sensitivity and specificity
  - Random classifier = diagonal line
  - Better models push curve up and left
  - Measure area under curve (AUC)
- **Confusion matrix analysis**: Break down errors by type
  - True positives, false positives, true negatives, false negatives
- **Performance by subgroup**: Segment data and measure metrics separately

**5. Validating Cross-Validation Reliability**

**Tests:**

- **Variance across folds**: High variance indicates problems
  - "Helpful when the performance of your model shows significant variance based on your train-test split"
  - Suggests either sample size issues or distribution heterogeneity
- **Calibrated confidence intervals**: Provide ranges, not point estimates
  - "Calibrated estimates tell you how much you know and take the form of a confidence interval"
  - Example: "4-8 weeks with 90% confidence"

**Calibration improvement techniques**:

1. Equivalent Bet Test (single best method)
2. Repetition and feedback
3. Consider potential problems (list 2 reasons to doubt estimate)
4. Avoid anchoring
5. Reverse anchoring (start wide, narrow with "absurdity test")

**General Validation Framework:**

**From EDA principles**:

- Emphasis on understanding "what is going on here?"
- Graphic representations of data
- Iterative model specification and hypothesis generation
- Skepticism and flexibility about which methods to apply

**From model criticism**:

- Validate assumptions systematically
- Use residuals as diagnostic tool
- Modify model when assumptions violated
- Iterate until satisfactory

**From measurement theory**:

- Quantify uncertainty reduction
- Use confidence intervals, not point estimates
- Recognize observer's role in uncertainty
- Measure value of information before collecting it

---

## Extracts from my notes

### 201806080942 Concept of measurement - Measurement is a quantified reduction in uncertainty based on your observations.txt

```
Concept of Measurement

- Measurement is a quantified reduction in uncertainty based on your observations
- When you measure, you can never get complete certainty
```

### 201806080958 Uncertainty is a feature of the observer, not the thing being measured.txt

```
Bayesian measurement implies uncertainty is a feature of the observer, not the thing being measured [@hubbard2014measure, p. 34]:

P1) The observer has some level of uncertainty they would like to reduce.

P2) Observations by the observer reduces uncertainty

C1) Therefore, the uncertainty of the object is a characteristic of the observer, not the object.
```

### 201806081256 Calibration tells you what you know and is a skill that can be improved.txt

```
- Calibrated estimates tell you how much you know and take the form of a confidence interval [@hubbard2014measure, p. 106]
- ex: How many weeks will project X take? 4-8 weeks with 90% confidence
- You need to know what you know now in order to determine if its necessary to get more information in order to reduce uncertainty.
- People aren't naturally good at giving calibrated estimates.
- Luckily, it is a skill that can be improved.

There are a few ways to get better at calibrating your estimates.

1. Equivalent Bet Test [@hubbard2014measure, p. 101]
	- This is THE SINGLE BEST way to improve your estimates
2. Repetition and feedback
	- The cycle can be tightened by giving people calibration tests on trivia
	- This practice seems to be highly transferrable
3. Consider potential problems
	- List out 2 reasons why you should doubt your estimate
4. Avoid Anchoring
	- Turn a 90% confidence interval into a binary question
	- Ex: "Are you 95% sure the real value isn't above the upper bound?"
5. Reverse the anchoring effect
	- Start with extremely wide ranges and narrow them with the "absurdity test" as you eliminate highly unlikely values.
```

### 201809071013 There are three measurements you take before measuring.txt

```
1. Uncertainty.  Measure a 90% confidence interval on the variable you are interested in. [@hubbard2014measure, p. 171]
2. Risk.  What is our downside?
3. Value of information.  How much can we justify spending to reduce this uncertainty?
```

### 202106150906 Regression Model Criticism and Selection.txt

```
We want a regression model that is _valid_. Our analysis usually depends on assumptions made about the data and the model (see [[202107041023 Least Squares Estimator Assumptions]]). Before we can draw any conclusions, we need to address the following questions [@chatterjee2012regression, p. 20]:

> 1. What are the required assumptions
> 2. For each of these assumptions, how do we determine whether or not the assumption is valid?
> 3. What can be done in cases where one or more of the assumptions does not hold?

View regression analysis as an _iterative_ process [@chatterjee2012regression, p. 20]. We have inputs: subject matter theories, model, data, statistical techniques, and auxiliary assumptions. And we have outputs: parameter estimates, confidence regions, test statistics, and graphical displays. Use your inputs to calculate your outputs. Then 'diagnose, validate, and criticize' the outputs. Then possibly modify your inputs, and repeat the process until you reach a satisfactory result.

## Methods used to criticize regression models:

* Residual plots help you validate a regression model - [[202106160654 Validate Regression Models with Residual Plots]]
```

### 202106160654 Validate Regression Models with Residual Plots.txt

```
After you fit a regression model, it is important to criticize it and verify its assumptions (see [[202107041023 Least Squares Estimator Assumptions]]) and [[202106150906 Regression Model Criticism and Selection]]). Analyzing residual plots are one method of doing so.

When analyzing a residual plot, look for the following [@AnscombeF.J1973GiSA, p.18]:

1. Outliers both on the x-axis and y-axis. The absence of outliers should give you more confidence in your model. From Anscombe [@AnscombeF.J1973GiSA, p.18]:

> We are usually happier about asserting a regression relation if the relation is still apparent after a few observations (any ones) have been deleted--that is, we are happier if the regression relation seems to permeate all the observations and does not derive largely from one or two.

2. Make sure that the residuals do not follow a curved pattern. This may indicate that the data does follow a pattern, but not the pattern of your model.
3. Check for heteroskedasticity. Does the variance of the residuals appear to change across the x-values? Many models assume homoskedasticity.
4. Do the residuals exhibit skew? Or do they appear to be roughly normally distributed?

Issues 2, 3, and 4 may be able to be resolved by transforming one of the independent variables, or adding a new term to the model, then re-fitting [@AnscombeF.J1973GiSA, p.18].

Behrens provides additional context [@BehrensJohnT1997PaPo, p. 140]:

> To create quantitative descriptions of data, the exploratory data analyst conducts an iterative process of suggesting a tentative model, examining the residuals from the model to assess model adequacy, and modifying the model in view of the residual analysis. This occurs in a cyclical process that should lead the analyst, bu successive approximation, toward a good description.
```

### 202107090833 Errors vs Residuals.txt

```
Say we want to estimate the mean of a distribution. We collect observations in order to estimate that mean $\mu$.

Errors are the difference between the observation ($Y_1$) and true population mean ($\mu$).

$$\delta_1 = Y_1 - \mu$$

Residuals are the difference between the observations (Y_i) and our estimate of the population mean ($\bar Y$):

$$\bar Y = \frac{1}{n} \sum_i^n Y_i$$

Typically $\mu$ is unobservable. Thus, we often use residuals as _estimates_ of the true errors.

## In Regression

In regression, we aren't trying to estimate a population mean. We are trying to estimate a function. It is this function that is unobservable.

Our residuals (see [[202107090851 Ordinary Least Squares Residuals]]) are the deviations between the observed values and the _fitted_ values.:

$$e_i = y_i - \hat y_i, i = i, 1, \dots , n$$

Where $n$ is the number of data points, $y$ is the observed value, and $\hat y$ is the predicted value.

And since our function is an estimate of the true unobservable function, the residual is an estimate for the true error. The true error would be:

$$Y_i - Y$$

Where $Y_i$ is the observed value from our dataset. And $Y$ is the value that the true (unobservable) regression function would predict.
```

### 202107041023 Least Squares Estimator Assumptions.txt

```
Least squares estimators (see [[202106160834 Method of Least Squares]]) have the following assumptions [@chatterjee2012regression, p.94].

From Chatterjee [@chatterjee2012regression, p.94]:

> A feature of the method of least squares is that small or minor violations of the underlying assumptions do not invalidate the inferences or conclusions drawn from the analysis in a major way. Gross violations of the model assumptions can, however, seriously distort conclusions.

## Assumptions about the form of the model

- Linearity Assumption (see [[202107041108 Least Squares Linearity Assumption]])

## Assumptions about the errors

Note that when we talk about errors, we mean errors, not residuals. See [[202107090833 Errors vs Residuals]].

- Normality Assumption (see [[202107041109 Least Squares Normality Assumption]])
- Errors have a mean of 0 [@chatterjee2012regression, p.94].
    - Note that the residuals have a mean of 0, by definition. But that isn't necessarily the case for errors.
    - I think this assumption means that the systematic errors are zero. See [[202107090901 Statistical Errors]].
- Constant Variance (of errors) Assumption (see [[202107041112 Least Squares Constant Variance Assumption]]).
- Independent Errors Assumption [[202107041115 Least Squares Independent Errors Assumption]]

## Assumptions about the predictors

- The predictors are non-random
- The predictors are measured without error.
- Independent Predictors Assumption (see [[202107041121 Least Squares Independent Predictors Assumption]])
```

### 202106150917 Exploratory Data Analysis.txt

```
Behrens provides a definition of EDA [@BehrensJohnT1997PaPo, p. 131]:

> EDA refers to a specific tradition of data analysis that stems from the work of John Tukey and his associates, which dates back to the early 1960s. This tradition of EDA can be loosely characterized by (a) an emphasis on the substantive understanding of data that address the broad question of "what is going on here?" (b) an emphasis on graphic representations of data; (c) a focus on tentative model building and hypothesis generation in an iterative process of model specification; (d) use of robust measures, re-expression, and subset analysis; and (e) positions of skepticism, flexibility, and ecumenism regarding which methods to apply.

Behrens [@BehrensJohnT1997PaPo, p. 132]:

> The goal of EDA is to discover patterns in the data.

Really it is to develop and refine hypotheses in a more informal manner, without theoretical grounding. And to develop a good mental model of the dataset.

Behrens [@BehrensJohnT1997PaPo, p. 132]:

> EDA is not simply a set of techniques but an attitude toward the data.

### EDA and Residuals

EDA can be useful after you have built a model. As an example, residual plots can be used to validate the assumptions of a linear regression model [[202106160654 Validate Regression Models with Residual Plots]].
```

### 202107200721 Receiver operating characteristic (ROC) Curve.txt

```
The Receiver operating characteristic (ROC) Curve is a diagnostic graph used for binary classifiers. It is used to assess the tradeoff between sensitivity and specificity as you vary the discrimination threshold. The x-axis measures the false positive rate (AKA 1 - specificity). The y-axis measures the true positive rate (AKA sensitivity).

A random classifier would yield a ROC curve that is a diagonal line from the bottom left to the top right. Better models push the middle of the curve up and to the left. Generally you want the area under this curve to be as large as possible, making the curve look like a lowercase 'r'. This means that your model has very few false positives, while still classifying most of the true positives. A perfect classifier is just a point at (0,1).
```

### 202101080707 The Bootstrap.txt

```
The bootstrap is a resampling technique that allows you to estimate the standard error of a sample statistic [@wilcox2010fundamentals, ch. 6].  As an example, say you sample 100 people and calculate the median height.  You could use bootstrapping to measure the standard error of that median (e.g. how much variation does that median exhibit? or how much uncertainty is there in this measurement of the median?).  The bootstrap works particularly well on non-normal distributions.  It is a robust method.  It is also a very general method.  As an example, you could use it to estimate the standard error of a regression coefficient.
```

### 202101080742 Cross Validation (K-Fold).txt

```
Cross validation is a general technique that estimates how well a model will **generalize** to new data.  K-Fold cross validation is a method that attempts to get the most out of your data.  **The goal is to use all the data for learning while still being able to measure an accurate generalization error** [@russell2010artificial, p. 708].

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
```

## Gaps filled by me (not from notes)

The specific production validation scenarios (KS tests, PSI metrics, A/B testing, pipeline comparison, temporal analysis) and how to organize validation tests by hypothesis type were synthesized from ML engineering practices. My notes provided comprehensive coverage of statistical validation principles (measurement as uncertainty reduction, model criticism, residual analysis, EDA, calibration, bootstrap, ROC curves, assumption checking) which form the theoretical foundation for any hypothesis validation, whether in research statistics or production ML debugging.
