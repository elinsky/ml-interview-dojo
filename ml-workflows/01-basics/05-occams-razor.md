# Question

"Occam's razor states that when the simple explanation and complex explanation both work equally well, the simple explanation is usually correct." How do we apply this principle in ML?

# Answer

We apply Occam's razor in ML by preferring simpler models over complex ones when they achieve similar performance. This principle manifests in several key ways:

**Regularization** is the primary mechanism: We explicitly add a complexity penalty to the loss function, optimizing Cost(h) = EmpiricalLoss(h) + λ·Complexity(h). This forces the model to balance accuracy against simplicity. L2 regularization (weight decay) prefers smaller parameter values, while L1 regularization drives many parameters to exactly zero, producing sparse models.

**Model selection criteria** like AIC and BIC formalize this tradeoff by penalizing models with more parameters. BIC applies a heavier penalty than AIC, tending to select simpler models. These metrics adjust training error to account for overfitting, effectively implementing Occam's razor mathematically.

**Early stopping** prevents models from becoming overly complex by halting training when validation performance stops improving, automatically preventing overfitting.

**Parametric models** embody simplicity by making assumptions about functional form (e.g., assuming f is linear). This reduces the problem from estimating an arbitrary function to estimating a fixed number of parameters, though at the risk of being too simple if the assumption is wrong.

**The smoothness prior** provides theoretical justification: it assumes that real-world functions change gradually, not abruptly. This prior underlies regularization techniques and explains why simpler, smoother functions often generalize better.

**Interpretability tradeoff**: Simpler models (linear regression, decision trees) are easier to interpret and understand, making them preferable for inference tasks even if complex models (deep neural networks) might achieve slightly higher accuracy.

The key insight is that simpler models generalize better to unseen data. While a complex model might fit training data perfectly, it's more likely to have learned noise rather than signal. Occam's razor protects against overfitting by favoring hypotheses that explain the data without unnecessary complexity.

---

## Extracts from my notes

### 202104170846 Regularization.txt

```
Regularization is the process of selecting a hypothesis that minimizes both the empirical loss and the complexity of the hypothesis [@russell2010artificial, p. 713].  Mathematically, it can be described as:

```{=latex}
\begin{equation}
Cost(h) = EmpLoss(h) + \lambda Complexity(h) \nonumber
\end{equation}

\begin{equation}
\hat h^* = \argminA_{h \in \mathcal{H}} Cost(h) \nonumber
\end{equation}
```

Where $h$ is a hypothesis, $\hat h^*$ is the estimated best hypothesis, $\mathcal{H}$ is your hypothesis space, and $\lambda$ is a positive number that serves as a conversion rate between loss and hypothesis complexity.
```

### 202101171731 L2 Regularization.txt

```
The regularization term is added to the cost function.  Regardless of the type of model that L2 regularization is applied to, L2 regularization tends to produce models that prefer smaller model parameters over larger ones.  Thus larger model parameters are only learned if their benefit outweighs their cost.

For neural networks, L2 regularization is typically applied to the model's weights, and can also be known as 'weight decay'.  The regularization term can be expressed mathematically as [@nielsen2015neural, p. 79]:

```{=latex}
\begin{equation}
\frac{\lambda}{2n} \sum_{w} w^{2}
\end{equation}
Where $w$ represents the weights in the neural network, $n$ represents the number of training examples, and $\lambda$ is the \emph{regularization parameter}.  Note that the 2 in the denominator is only there to simplify the calculation of the derivative.
```

It is called weight decay because when you compute the partial derivative of the cost function with the regularization term, the regularization term always creates a little gradient that leads downhill to a point where all the weights are 0.

Another way to think of L2 regularization in neural networks is to view weight decay as preventing small changes in input data from changing the weights by too much.  It is as if there is some inertia preventing the model from making the weights bigger.
```

### 202101171802 L1 Regularization.txt

```
In neural networks, the L1 regularization term can be mathematically expressed as [@nielsen2015neural, p. 87]:

```{=latex}
\begin{equation}
\frac{\lambda}{n} \sum_{w} \left| w \right|
\end{equation}
Where $w$ represents the weights in the neural network, $n$ represents the number of training examples, and $\lambda$ is the \emph{regularization parameter}.
```

Similarly to in linear regression, L1 regularization tends to produce a neural network where many weights are close to zero (and thus not doing much) while a few weights are large and do most of the work.
```

### 202107260847 Akaike information criterion (AIC).txt

```
AIC is an estimator of prediction accuracy that can be used for model selection (see [[202107270653 Model Selection for Linear Regression]]). It uses the sum of squared errors (see [[202107041216 Sum of Squared Errors (SSE)]]) as a measure of accuracy. AIC is almost always uses the training dataset to estimate prediction accuracy. Since clearly accuracy on the training set is biased due to overfitting, AIC is an attempt to adjust for that.

In OLS linear regression, AIC is defined as [@kuhn2013applied, 493]:

$$AIC = n \log \left( \sum_{i=1}^n(y_i - \hat y_i)^2 \right) + 2P$$

Where $P$ is the number of terms in the model.

You can think of this as a penalized version of the sums of squares error. Lower numbers are better than larger numbers.
```

### 202107271816 Bayesian information criterion (BIC).txt

```
in R_ provides an alternative formula for BIC applied to OLS regression [@james2013introduction, p. 212]:

$$BIC = \frac{1}{n\hat\sigma^2}(RSS + \log(n)d\hat\sigma^2)$$

Lower is better. Similar to AIC, it adds a penalty for more parameters. The BIC penalty is larger than AIC.
```

### 202107270653 Model Selection for Linear Regression.txt

```
From [@hastie2013elements, p.235]:

> For model selection purposes, there is no clear choice between AIC and BIC. BIC is asymptotically consistent as a selection criterion. What this means is that given a family of models, including the true model, the prob- ability that BIC will select the correct model approaches one as the sample size N → ∞. This is not the case for AIC, which tends to choose models which are too complex as N → ∞. On the other hand, for finite samples, BIC often chooses models that are too simple, because of its heavy penalty on complexity.
```

### 202101171725 Early Stopping.txt

```
From Michael Nielsen [@nielsen2015neural, p. 113]:

> Early stopping means that at the end of each epoch we should compute the classification accuracy on the validation data. When that stops improving, terminate. This makes setting the number of epochs very simple. In particular, it means that we don't need to worry about explicitly figuring out how the number of epochs depends on the other hyper-parameters. Instead, that's taken care of automatically. Furthermore, early stopping also automatically prevents us from overfitting.
```

### 202012301740 Smoothness Prior.txt

```
The smoothness prior asserts that physical properties exhibit coherence across both space and time [@li2012markov, p. 21].  Abrupt changes do not occur frequently in nature.  As an example, your surroundings have likely changed a little bit over the past minute.  But those changes were likely continuous in nature, not discontinuous.

Mathematically, smoothness is defined as follows [@40d5d7fd62cb44ba934a8a75d4b2b076, p. 7]:

> We mean f to be smooth when the value of f(x) and of its derivative f′(x) are close to the values of f(x + ∆) and f′(x + ∆) respectively when x and x + ∆ are close as defined by a kernel or a distance.

The smoothness prior is the most basic prior present in machine learning [@DBLP:journals/corr/abs-1206-5538, p. 3], and is particularly prevalent in low level vision problems.  The smoothness prior provides the theoretical foundation for regularization, as a general technique [@kitagawa2012smoothness, p. 30].

> A smoothness prior favors functions f such that when x ≈ x′, f(x) ≈ f(x′). [@40d5d7fd62cb44ba934a8a75d4b2b076, p. 16]
```

### 202106191007 Prediction vs Inference.txt

```
Simpler models (e.g. [[202106150747 Linear Regression Model]]) are easier to understand, and are thus well-suited to inference problems. However, they tend to have lower accuracies than more complicated models well suited to prediction.

**Hence, there is often a tradeoff between interpretable but lower accuracy models vs uninterpretable but higher accuracy models.**
```

### 202104170948 Parametric Models.txt

```
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
```

