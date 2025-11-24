# Question

Can a classification problem be turned into a regression problem and vice versa?

# Answer

Yes, classification and regression problems can often be converted between one another, though this conversion comes with trade-offs.

## Classification → Regression

**How:** Treat discrete class labels as numerical values.

**Examples:**

- **Ordinal regression**: When classes have a natural ordering (e.g., movie ratings 1-5 stars, disease severity low/medium/high), you can treat labels as continuous numerical targets
- **Probability regression**: Instead of predicting discrete classes, predict class probabilities as continuous values between 0 and 1

**Trade-offs:**

- **Advantage:** Can leverage regression techniques and loss functions (MSE); may provide finer-grained predictions
- **Disadvantage:** Loses categorical structure; implies ordering/distance between classes that may not exist; may predict invalid intermediate values

## Regression → Classification (Dichotomization)

**How:** Discretize continuous outputs into categorical bins or apply threshold boundaries.

**Examples:**

- **Binning**: Convert house prices into categories (budget/mid-range/luxury) or temperature into ranges (cold/mild/warm/hot)
- **Thresholding**: Convert continuous predictions to binary classes (e.g., income > $50K → "high income" class)

**Trade-offs:**

- **Advantage:** Simplifies problem; can be more robust to outliers; may align better with business needs
- **Disadvantage:** Loses information and precision; reduces statistical power; introduces arbitrary boundaries; cutpoints don't replicate across studies; assumes discontinuities at boundaries that rarely exist; residual confounding

## Models That Handle Both

Some algorithms can naturally handle both classification and regression with minimal modification:

**Decision Trees / CART Algorithm**: The same tree-based algorithm can do both:

- **Classification**: Uses Gini impurity or cross-entropy to split; leaf nodes return most common class
- **Regression**: Uses MSE to split; leaf nodes return average of training examples

**Neural Networks**: Can switch between tasks by changing the final layer:

- **Classification**: Softmax/sigmoid activation + cross-entropy loss
- **Regression**: Linear activation + MSE loss

**Notable Misnomers:**

- **Logistic Regression**: Despite the name "regression," it's actually a binary **classification** model that outputs probabilities

---

## Extracts from my notes

### 202107301904 Dichotomizing Continuous Variables.txt

```
Dichotomizing continuous variables is the process of taking a continuous variable and cutting it up into categorical groups. E.g. taking a data set of test scores expressed as percentages, dropping the percentage variable, and replacing it with a grade variable (A, B, C, ...).

While dichotomizing variables simplifies the analysis, most statisticians are opposed to the idea [@AltmanDouglasG2006Tcod, p. 1080] [@harrell2015regression, p.19]. Harrell lists quite a few problems with dichotomization [@harrell2015regression, p.19]:

> 1. Estimated values will have reduced precision, and associated tests will have reduced power.
> 2. Categorization assumes that the relationship between the predictor and the response is flat within intervals; this assumption is far less reasonable than a linearity assumption in most cases.
> 3. To make a continuous predictor be more accurately modeled when categorization is used, multiple intervals are required. The needed indicator variables will spend more degrees of freedom than will fitting a smooth relationship, hence power and precision will suffer.
> 4. Categorization assumes that there is a discontinuity in response as interval boundaries are crossed. Other than the effect of time (e.g., an instant stock price drop after bad news), there are very few examples in which such discontinuities have been shown to exist.
> 5. Categorization only seems to yield interpretable estimates such as odds ratios. [...] The interpretation of the resulting odds ratio will depend on the exact distribution of blood pressures in the sample.
> 6. Categorization does not condition on full information. When, for example, the risk of stroke is being assessed for a new subject with a known blood pressure (say 162 mmHg), the subject does not report to her physician "my blood pressure exceeds 160" but rather reports 162 mmHg. The risk for this subject will be much lower than that of a subject with a blood pressure of 200 mmHg.
> 9. "Optimal" cutpoints do not replicate over studies. [...] Disagreements in cutpoints (which are bound to happen whenever one searches for things that do not exist) cause severe interpretation problems.
> 10. Cutpoints are arbitrary and manipulatable; cutpoints can be found that can result in both positive and negative associations.
> 11. If a confounder is adjusted for by categorization, there will be residual confounding that can be explained away by inclusion of the continuous form of the predictor in the model in addition to the categories.

A brief summary by me:

* Cutpoints reduce precision and power.
* Cutpoints require you to spend more degrees of freedom on the model than necessary.
* Comparisons across studies are difficult when cutpoints are introduced.
```

### 202104160853 Classification and Regression Tree (CART) Algorithm.txt

```
Classification and Regression Tree (CART) is a training algorithm used to train decision trees.

For **classification** problems, CART attempts to minimize the following cost function [@geron2017hands, p. 179]:

$$J(k, t_k) = \frac{m_{\text{left}}}{m}G_{\text{left}} + \frac{m_{\text{right}}}{m}G_{\text{right}}$$

$$\text{Where}
    \begin{cases}
      G_{\text{left/right}} \text{ measures the impurity of the left/right subset,} \\
      m_{\text{left/right}} \text{ is the number of instances in the left/right subset.}
    \end{cases}$$

For **regression** problems, the following cost function is used [@geron2017hands, p. 184]:

$$J(k, t_k) = \frac{m_{\text{left}}}{m}\text{MSE}_{\text{left}} + \frac{m_{\text{right}}}{m}\text{MSE}_{\text{right}}$$

$$\text{Where}
    \begin{cases}
      \text{MSE}_{\text{node}} = \sum_{i \in \text{node}}(\hat y_{\text{node}} - y^{(i)})^2 \\
      \hat y_{\text{node}} = \frac{1 }{m_{\text{node}}} \sum_{i \in \text{node}}(y^{(i)})
    \end{cases}$$
```

### 202104151745 Decision Trees.txt

```
Decision trees can be used for classification and regression tasks.  The model's **representation** takes the form of a binary tree.  Each internal node in the tree represents a test of the value of one of the attributes/features.  Each branch from the node is labelled with possible values of the splitting attribute.  Each leaf specifies a value to be returned by the function.

At inference time, you take the features of the sample, then traverse the decision tree until you reach a root.  For classification, the probability of each class is determined by the probability of each class in your leaf node.  For regression tasks, the output value is the average of all the training examples in your leaf node.
```

### 202107200915 Logistic Regression.txt

```
Logistic regression is a binary classification model. It is a direct probability model, which means it directly estimates the probability of an event occurring.

For classification, logistic regression is preferred over linear regression because use of the logistic function allows us to bound the probability between 0 and 1 (see [[202107290829 Logistic Function]]).

A logistic regression model takes the following functional form [@james2013introduction, p. 135]:

$$p(X) = \frac{{\mathrm e}^{\beta_0 + \beta_1 X_1 + \dots + \beta_p X_p}}{1 + {\mathrm e}^{\beta_0 + \beta_1 X_1 + \dots + \beta_p X_p}}$$

You can think of logistic regression as a linear regression model in the log odds [@harrell2015regression, p.221].
```

### 202101120811 Activation Functions.txt

```
Chollet recommends the following activation functions for the final layer [@chollet2018deep, p. 114]:

| Problem Type                            | Last-Layer Activation | Loss Function              |
| --------------------------------------- | --------------------- | -------------------------- |
| Binary classification                   | Sigmoid               | binary_crossentropy        |
| Multiclass, single-label classification | Softmax               | categorical_crossentropy   |
| Regression to arbitrary values          | None                  | mse                        |
| Regression to values between 0 and 1    | Sigmoid               | mse or binary_crossentropy |
```

## Gaps filled by me (not from notes)

The specific examples of ordinal regression and probability regression for classification→regression conversion were synthesized from ML best practices, though the dichotomization note provides comprehensive coverage of the regression→classification direction with exact citations.
