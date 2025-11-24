# Question

What's the risk in empirical risk minimization?

# Answer

The "risk" refers to the expected loss or error of a model. In statistics and ML, risk represents the potential for a negative outcome - specifically, the expected cost of prediction errors over the true data distribution.

Empirical risk minimization (ERM) estimates this true risk using only the training data available. The empirical risk is the average loss computed over the training dataset, which serves as an approximation of the true expected loss. The key distinction is:

- **True risk**: Expected loss over the entire population/true distribution (unknown)
- **Empirical risk**: Average loss over the finite training sample (computable)

The goal in ERM is to find model parameters that minimize the empirical risk (training error), with the hope that this also minimizes the true risk (generalization error). However, minimizing empirical risk can lead to overfitting if the model fits noise in the training data rather than the underlying pattern. This is managed through regularization, cross-validation, and other techniques that balance fitting the training data with generalizing to unseen data.

---

## Extracts from my notes

### 201806081123 Uncertainty means we don't know what's going to happen.  Risk means we have the potential to have a negative outcome.txt

> Uncertainty - "we don't know what is going to happen" [@hubbard2014measure, p. 84]
> Risk - In scenario X, we could lose $
>
> Implication - measuring reduces uncertainty, not risk.

### 202012261442 Cost Functions.txt

> A cost function measures how poorly a model does at predicting the right answer.  The output of a cost function can also be thought of as a 'distance score' [@chollet2018deep, p. 10].  The score is a measure of the distance between the desired model output (or ground truth) and the actual model output.
>
> Russell and Norvig define loss/cost functions as follows [@russell2010artificial, p. 710]:
>
> > The loss function $L(x, y, \hat y)$ is defined as the amount of utility lost by predicting $h(x) = \hat y$ when the correct answer is $f(x) = y$.
>
> Why are cost functions important?  The inputs to a cost function are your model parameters.  So if you have an optimization algorithm (e.g. gradient descent), then you can use it to find the set of parameters that minimize your cost function.  A cost function plus an optimization algorithm essentially enables you to fit your model.

### 202101050745 Mean Squared Error Cost Function.txt

> The mean squared error cost function (AKA quadratic cost) is one of the most commonly used cost functions in neural networks.  Informally, it penalizes large errors way more than it penalizes small errors.
>
> Algebraically, it is defined as [@nielsen2015neural, p. 16]:

$$
J(\theta) = \frac{1}{2n} \sum_{x} \| h_{\theta}(x) - y \|^{2}
$$
$J$ is typically used to denote a cost function.  $\theta$ often represents the model parameters, which are the weights and biases in our case.  The 2 in the denominator is only there to make the derivative of the cost function cleaner.  $h_{\theta}$ denotes the 'hypothesis function', which is essentially your model.  $x$ denotes a single training example, which is likely represented as a vector, or an n-dimensional matrix.  $y$ denotes the 'actual' value for the training example, or the 'ground truth'.  Note that $y$ may be a single value, or it could be a vector.  We calculate the norm of the error vector because the norm is a good method to measure the magnitude of a vector.

### 202106191115 Bias-Variance Trade-Off.txt

From _An Introduction to Statistical Learning_ [@james2013introduction, p. 33]:

> It is possible to show that the expected test MSE, for a given value $x_0$, can always be decomposed into the sum off three fundamental quantities: the variance of $\hat f (x_0)$, the squared bias of $\hat f (x_0)$ and the variance of the error terms $\epsilon$. That is,
> $$E(y_0 - \hat f (x_0))^2 = Var(\hat f(x_0)) + [Bias(\hat f (x_0))]^2 + Var(\epsilon)$$
>
> Here the notation $E(y_0 - \hat f (x_0))^2$ defines the expected test MSE, and refers to the average test MSE that we would obtain if we repeatedly estimated $f$ using a large number of training sets, and tested each at $x_0$. The overall expected test MSE can be computed by averaging $E(y_0 - \hat f (x_0))^2$ over all possible values of $x_0$ in the test set.

Our goal is to develop a function $\hat f$ that closely approximates the true function $f$ (see [[202106191014 Statistical Learning]]). We cannot reduce the irreducible error $\epsilon$. But we can reduce the bias and variance.

### 202101050843 Gradient Descent.txt

Gradient descent is an **optimization algorithm** that **modifies model parameters** in order to **minimize** a **cost function**.

The simplest mathematical description of gradient descent is as follows [@nielsen2015neural, p. 22]:

$\theta' = \theta - \eta \frac{\partial C}{\partial \theta}$ \\

Where theta is a model parameter, eta is the learning rate, and C represents the cost function.

### 202101241721 Preventing Overfitting in Neural Networks.txt

Preventing overfitting is important because it reduces your generalization error.  Said another way, models that aren't overfit generalize better than overfit models.

One common method of measuring overfitting is to compare the spread between your training error and your test/validation error (see [[202101080742 Cross Validation (K-Fold)]]).

The single best method to prevent overfitting is to get more training data [@chollet2018deep, p. 104].  The next best solution is to figure out how to constrain the model.  E.g. dropout, regularization (see [[202104170846 Regularization]]), or reducing the number of model parameters).

### 201908031553 The two major types of error in sampling are sample bias and sample error.txt

There are two major types of error in sampling: [@watt2002research, p. 62-81]

1. Sample error is due to randomness. You can reduce sample error by increasing your sample size.
2. Sample bias. Sample bias has two sub-components: Selection bias and response bias.  You introduce selection bias by not having a truly random sample.  Response bias is introduced when people opt-out of your survey.
