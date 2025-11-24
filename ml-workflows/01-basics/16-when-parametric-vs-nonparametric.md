# Question

When should we use parametric versus non-parametric methods?

# Answer

The choice between parametric and non-parametric methods depends on several factors: amount of training data available, interpretability requirements, prior knowledge about the problem, and the bias-variance trade-off you're willing to accept.

**Use Parametric Methods When:**

1. **Limited training data**: Parametric models require fewer training examples because they summarize data into a fixed set of parameters. They can perform well even with small datasets.

2. **Interpretability matters**: When you need to understand the relationship between features and output (inference), parametric models like linear regression are easier to interpret. There's often a trade-off between interpretable but lower accuracy models vs uninterpretable but higher accuracy models.

3. **Domain knowledge exists**: If you have strong prior knowledge about the functional form of the relationship (e.g., you know it's roughly linear), parametric models let you encode this assumption.

4. **Computational efficiency required**: Parametric models are simpler and faster to train, with fewer parameters to estimate.

5. **You can accept higher bias**: Parametric models tend to have high bias but low variance. They may undersimplify the true function, but they won't change dramatically with different training sets.

**Use Non-Parametric Methods When:**

1. **Large amounts of training data**: Non-parametric models require many more training examples than parametric models to obtain accurate estimates. With sufficient data, they can fit complex patterns.

2. **Unknown functional form**: When you don't know the shape of the underlying function and don't want to risk choosing the wrong form, non-parametric models make no explicit assumptions about functional form.

3. **Flexibility is priority**: Non-parametric models can fit a wider range of functions. They have a bigger hypothesis space and can approximate complex, non-linear relationships.

4. **You can accept higher variance**: Non-parametric models tend to have high variance but low bias. They're flexible enough to fit the true function, but may change significantly with different training data and are prone to overfitting.

5. **Prediction over interpretation**: When you only care about predictive accuracy and can treat the model as a black box.

**Key Trade-Off:**

As you increase model flexibility (moving from parametric to non-parametric), bias decreases but variance increases. Initially, test error decreases as bias reduction outpaces variance increase. But eventually, test error increases again as you begin overfitting. The optimal choice balances these factors based on your specific constraints and requirements.

**Concrete Examples:**

- **Linear Regression (Parametric)**: High bias, low variance. Likely oversimplifies the true function, but stable across different training sets. Good for inference and small datasets.

- **Random Forest (Non-Parametric)**: Low bias, high variance. Flexible enough to fit complex functions with enough data, but needs many examples and changes significantly with different datasets. Good for pure prediction with large datasets.

---

## Extracts from my notes

### 202104170948 Parametric Models.txt

```
From Russell and Norvig [@russell2010artificial, p. 737]:

> A learning model that summarizes data with a set of parameters of fixed size (independent of the number of training examples) is called a parametric model.

From _An Introduction to Statistical Learning_ [@james2013introduction, p. 21]:

> Parametric Methods involve a two-step model-based approach.
>
> 1. First, we make an assumption about the functional form, or shape, of $f$. For example, on very simple assumption is that $f$ is linear in $X$:
>
> $$f(X) = \beta_0 + \beta_1X_1 + \beta_2X_2 + \dots + \beta_pX_p$$
> ...
>
> 2. After a model has been selected, we need a procedure that uses the training data to fit or train the model.

Parametric modeling approaches essentially have the analyst choose a functional form. This then reduces the problem of estimating $f$ down to estimating a set of parameters for that model.

The disadvantage of parametric models is that you might have chosen the wrong functional form. In this scenario, no matter how well you choose the model parameters, your function is too far off from the true $f$ to provide a good approximation. You can overcome this problem by giving your model more parameters (or degrees of freedom), but then you have to start worrying about overfitting.

A few examples of parametric models are:

* Linear regression (see [[202106150747 Linear Regression Model]])
* Neural networks
```

### 202104170946 Nonparametric Models.txt

```
From Russell and Norvig [@russell2010artificial, p. 737]:

> A nonparametric model is one that cannot be characterized by a bounded set of parameters.  For example, suppose that each hypothesis we generate simply retains within itself all of the training examples and uses all of them to predict the next example.  Such a hypothesis family would be nonparametric because the effective number of parameters is unbounded--it grows with the number of examples.  This approach is called instance-based learning or memory-based learning.

From _An Introduction to Statistical Learning_ [@james2013introduction, p. 23]:

> Non-parameteric methods do not make explicit assumptions about the functional form of $f$.

Since non-parametric models do not assume a specific functional form, they often have a bigger hypothesis space than parametric models. They can fit a wider range of $f$. However, non-parametric models typically require a large number of observations (many more than parametric models) to obtain an accurate estimate of $f$.

Examples of nonparametric models include:

* Decision trees [[202104151745 Decision Trees]]
* K-nearest neighbors
```

### 202106191115 Bias-Variance Trade-Off.txt

```
From _An Introduction to Statistical Learning_ [@james2013introduction, p. 33]:

> It is possible to show that the expected test MSE, for a given value $x_0$, can always be decomposed into the sum off three fundamental quantities: the variance of $\hat f (x_0)$, the squared bias of $\hat f (x_0)$ and the variance of the error terms $\epsilon$. That is,
> $$E(y_0 - \hat f (x_0))^2 = Var(\hat f(x_0)) + [Bias(\hat f (x_0))]^2 + Var(\epsilon)$$
>
> Here the notation $E(y_0 - \hat f (x_0))^2$ defines the expected test MSE, and refers to the average test MSE that we would obtain if we repeatedly estimated $f$ using a large number of training sets, and tested each at $x_0$. The overall expected test MSE can be computed by averaging $E(y_0 - \hat f (x_0))^2$ over all possible values of $x_0$ in the test set.

Our goal is to develop a function $\hat f$ that closely approximates the true function $f$ (see [[202106191014 Statistical Learning]]). We cannot reduce the irreducible error $\epsilon$. But we can reduce the bias and variance.

From _An Introduction to Statistical Learning_ [@james2013introduction, p. 34]:

> Variance refers to the amount by which $\hat f$ would change if we estimated it using a different training data set. Since the training data are used to fit the statistical learning method, different training data sets will result in a different $\hat f$. But ideally the estimate for $f$ should not vary too much between training sets. However, if a method has high variance then small changes in the training data can result in large changes in $\hat f$. In general, more flexible statistical models have higher variance.

From _An Introduction to Statistical Learning_ [@james2013introduction, p. 35]:

> On the other hand, bias refers to the error that is introduced by approximating a real-life problem, which may be extremely complicated, by a much simpler model.

The goal is to find a learning method that has both low variance and low bias. But generally, as you increase the flexibility of a learning method, the bias will decrease and the variance will increase. Usually, the bias will decrease at a faster rate than the variance increases. This produces a net reduction in test error. But eventually, test error will start to increase again as you start to overfit the dataset.

### Example - Linear Regression

As an example, a linear regression model will tend to have high bias but low variance. It will be high bias because $\hat f$ likely doesn't have the same functional form of $f$. $\\hat f$ is probably an oversimplification. No matter how much data you have, you likely won't produce a model that truly approximates $f$. However, a linear model will likely have low variance. If you add or remove a single data point, your model parameters likely won't change by much.


### Example - Random Forest

As for a random forest, it will tend to have high variance and low bias. A random forest is non-linear, and with enough data it is flexible enough to fit just about any function $f$. However, a random forest is low-bias. It needs a lot of data to perform well. And if the dataset changes, the model is likely to change as well.
```

### 202106191007 Prediction vs Inference.txt

```
In the field of statistical learning (see [[202106191014 Statistical Learning]]), we wish to estimate or approximate $f$. There are two main reasons to estimate $f$, prediction and inference [@james2013introduction, p. 17].

### Prediction

In prediction, the primary objective is to build a model that correctly predicts $Y$, given $X$. Our model can be written mathematically as [@james2013introduction, p. 17]:

$$\hat Y = \hat f (X)$$

As long as our model makes good predictions, we are OK treating the model as a black box.

### Inference

When we want to build a model, but also understand the relationship between $X$ and $Y$, then our goal is inference. We can no longer treat our model as a black box.


### Choice of Model

Simpler models (e.g. [[202106150747 Linear Regression Model]]) are easier to understand, and are thus well-suited to inference problems. However, they tend to have lower accuracies than more complicated models well suited to prediction.

**Hence, there is often a tradeoff between interpretable but lower accuracy models vs uninterpretable but higher accuracy models.**
```

## Gaps filled by me (not from notes)

The structured comparison of when to use each method type (the two bulleted lists) and the synthesis of how these factors interact were created to directly answer the question. My notes provided the foundational concepts (bias-variance trade-off, interpretability vs accuracy, data requirements, functional form assumptions) but didn't explicitly enumerate decision criteria for choosing between the two approaches.
