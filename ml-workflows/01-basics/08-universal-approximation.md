# Question

"The Universal Approximation Theorem states that a neural network with 1 hidden layer can approximate any continuous function for inputs within a specific range." Then why can't a simple neural network reach an arbitrarily small positive error?

# Answer

While the Universal Approximation Theorem guarantees that a neural network *can* approximate any continuous function, it doesn't guarantee we can actually *find* that approximation or that it will generalize well. There are several fundamental barriers:

**1. Irreducible Error (Bayes Error)**: The data itself contains noise that no model can eliminate. The expected test error can be decomposed into three components: $E(y_0 - \hat f(x_0))^2 = Var(\hat f(x_0)) + [Bias(\hat f(x_0))]^2 + Var(\epsilon)$. The irreducible error $Var(\epsilon)$ sets a floor on achievable performance - we cannot reduce it no matter how good our model is.

**2. The Theorem Says Nothing About Trainability**: The Universal Approximation Theorem is an existence proof - it guarantees that some configuration of weights exists that can approximate the target function. But it provides no guidance on how to actually find those weights through training. Optimization via gradient descent may get stuck in local minima, saddle points, or simply fail to converge to the global optimum.

**3. Practical Network Size May Be Intractable**: The theorem doesn't specify how many hidden units are needed. For complex functions, the required network width might be exponentially large, making training computationally infeasible with finite resources. A network with billions of parameters may theoretically approximate the function, but we can't train it in practice.

**4. Finite Training Data**: Even if we could find the perfect approximation of the true function on our training data, we only have access to a finite sample. With limited data, we face the bias-variance tradeoff. More flexible models (with many parameters) will have low bias but high variance - they'll fit the training data perfectly but generalize poorly to new data, resulting in high test error.

**5. Overfitting vs. Generalization**: A network with enough capacity can memorize the training data and achieve near-zero training error. But this doesn't mean it has learned the true underlying function $f$. The model may have learned the noise in the training data rather than the signal, leading to poor performance on test data. The goal is to minimize expected test error, not training error.

**6. The Bias-Variance Tradeoff**: As we increase model flexibility to reduce bias (approximation error), we increase variance (sensitivity to training data). Generally, more flexible methods have higher variance. We must find the sweet spot that minimizes total expected test error, which typically occurs before achieving arbitrarily small training error.

In summary: The Universal Approximation Theorem guarantees representational capacity in theory, but practical constraints (irreducible noise, optimization difficulties, finite data, computational limits, and the need to generalize) prevent achieving arbitrarily small error in practice.

---

## Extracts from my notes

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
```

### 202106191014 Statistical Learning.txt

```
From _An Introduction to Statistical Learning_ [@james2013introduction, p. 16]:

> More generally, supposed that we observe a quantitative response $Y$ and $p$ different predictors, $X_1, X_2, \dots, X_p$. We assume that there is some relationship between $Y$ and $X = (X_1, X_2, \dots, X_p), which can be written in the very general form
>
> $$Y = f(X) + \epsilon$$
>
> Here $f$ is some fixed but unknown function of $X_1, \dots , X_p$, and $\epsilon$ is a random error term, which is independent of $X$ and has mean zero. In this formulation, $f$ represents the systematic information that $X$ provides about $Y$.

Note $f$ is the best that we can do _given only_ $X$. If we were to have more predictor variables in $X$ that provided additional information, we would be able to produce a better $f$ and reduce $\epsilon$. In this sense, the irreducible error $\epsilon$ cannot be reduced given $X$. But if you augment $X$, it _can_ be reduced.

From _An Introduction to Statistical Learning_ [@james2013introduction, p. 17:

> In essence, statistical learning refers to a set of approaches for estimating $f$.
```

### 202101241721 Preventing Overfitting in Neural Networks.txt

```
Preventing overfitting is important because it reduces your generalization error.  Said another way, models that aren't overfit generalize better than overfit models.

One common method of measuring overfitting is to compare the spread between your training error and your test/validation error (see [[202101080742 Cross Validation (K-Fold)]]).

The single best method to prevent overfitting is to get more training data [@chollet2018deep, p. 104].  The next best solution is to figure out how to constrain the model.  E.g. dropout, regularization (see [[202104170846 Regularization]]), or reducing the number of model parameters).

* Get more training data
* Reduce the capacity of the network
* Add weight regularization
* Add dropout
* Data augmentation (primarily for CNNs) (see [[202101260751 Data Augmentation]])

## When to Worry About Overfitting

Overfitting is something to think about when:

* You have a small dataset
```

## Gaps filled by me (not from notes)

The Universal Approximation Theorem is an existence proof, optimization challenges, and exponentially large network requirements are concepts I synthesized to directly answer the question, as these specific details weren't explicitly in my notes.

