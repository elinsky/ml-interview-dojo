# Question

How do we minimize that risk?

# Answer

We minimize empirical risk through **optimization algorithms** that adjust model parameters to reduce the cost/loss function. The dominant approach is **gradient-based optimization**, which iteratively updates parameters in the direction that decreases the loss.

The core method is **gradient descent**: compute the gradient (partial derivatives) of the cost function with respect to each parameter, then update parameters by moving in the opposite direction of the gradient. The update rule is: θ' = θ - η∇C(θ), where η is the learning rate.

In practice, we use **variants** for efficiency:

- **Stochastic Gradient Descent (SGD)**: Updates parameters using one training example at a time, faster but noisier
- **Mini-batch Gradient Descent**: Updates using small batches (typically 8-256 examples), balancing speed and stability

**Backpropagation** is the algorithm that efficiently computes gradients in neural networks by applying the chain rule to propagate errors backward through layers.

**Advanced optimizers** improve upon vanilla gradient descent:

- **Adam** (Adaptive Moment Estimation): Adapts learning rates per parameter using momentum and RMSprop, most commonly used in deep learning
- **Momentum**: Accumulates past gradients to accelerate convergence and escape local minima
- Others: Adagrad, RMSprop, Adadelta

**Training workflow**:

1. Choose architecture (layers, neurons, activation functions)
2. Initialize weights
3. Select cost function (MSE for regression, cross-entropy for classification)
4. Choose optimizer
5. Iterate through training data (epochs) until convergence or stopping criterion

For linear models, **ordinary least squares** provides a closed-form solution by minimizing squared errors directly, though gradient descent is still used when datasets are large.

The key challenges include selecting learning rates, avoiding local minima/saddle points, and preventing slow convergence on plateaus.

---

## Extracts from my notes

### 202101050843 Gradient Descent.txt

```
Gradient descent is an **optimization algorithm** that **modifies model parameters** in order to **minimize** a **cost function**.  This article primarily deals with **batch** gradient descent, aka vanilla gradient descent.

The simplest mathematical description of gradient descent is as follows [@nielsen2015neural, p. 22]:

```{=latex}
$\theta' = \theta - \eta \frac{\partial C}{\partial \theta}$ \\

Where theta is a model parameter, eta is the learning rate, and C represents the cost function.
```

Probably the simplest way to express batch gradient descent mathematically is as follows [@DBLP:journals/corr/Ruder16, p. 2]:

```{=latex}
\begin{equation}
\theta = \theta - \eta \cdot \nabla_\theta J( \theta)
\end{equation}
```

Where $\theta$ represents the model parameters, $\nabla_\theta J( \theta)$ is the gradient of the objective function with respect to the parameters, and $\eta$ is the learning rate.
```

### 202012261442 Cost Functions.txt

```
Why are cost functions important?  The inputs to a cost function are your model parameters.  So if you have an optimization algorithm (e.g. gradient descent), then you can use it to find the set of parameters that minimize your cost function.  A cost function plus an optimization algorithm essentially enables you to fit your model.
```

### 202101070827 Stochastic Gradient Descent.txt

```
True gradient descent ([[202101050843 Gradient Descent]]) is computationally expensive.  In order to update the set of all model parameters once, gradient descent requires you to compute $N\times P$ gradients where $N$ is the number of training examples and $P$ is the number of model parameters.

The big idea behind stochastic gradient descent (SGD) is that we are willing to get faster compute times for gradients in return for slightly less accurate gradients.  SGD achieves this by computing gradients for all model parameters for a single training example.  Then it updates the model parameters.  In "true" SGD, we only use one data point for each iteration.  Thus the model parameters are updated $N$ times in a single epoch, compared to $1$ time in gradient descent.

In gradient descent, the gradient for a single parameter is an _average_ of the gradient for that parameter over all training examples.  In SGD, there is no averaging.
```

### 202101071932 Mini-Batch Gradient Descent.txt

```
Mini-batch gradient descent is a hybrid between gradient descent ([[202101050843 Gradient Descent]]) and stochastic gradient descent ([[202101070827 Stochastic Gradient Descent]]).  In mini-batch gradient descent, we calculate the gradients a subset of the training examples (compared to a single training example or all training examples).  This comes close to offering the best of both worlds.  Model parameters are updated multiple times per epoch.  And often mini-batch gradient descent is computationally faster than stochastic gradient descent because some of the calculations can be run in parallel.

Convergence is more stable than SGD because the process of averaging gradients for an update reduces the variance of parameter updates [@DBLP:journals/corr/Ruder16, p. 3].
```

### 202101130721 Mathematics of Backpropagation.txt

```
An equation for the error in the output layer [@nielsen2015neural, p. 44]:

```{=latex}
$$\updelta^{L}_{j} = \frac{\partial C}{\partial a^{L}_{j}} \sigma'(z^{L}_{j})$$

Where $z_{j}^{L} \equiv \mathbf{w}^{L}_{j} \cdot \mathbf{a}^{L-1}_{j}  + b^{L}_{j}$ and is interpreted as the ``summed activation'' of the $j$-th neuron in the last layer.  And $\updelta^{L}_{j} \equiv \frac{\partial C}{\partial z^{L}_{j}}$, aka the ``error''.  And $\sigma'$ is the derivative of the activation function with respect to $z$.  And $C$ is the cost function.  And $a^{L}_{j}$ is the activation of the $j$-th neuron in the last layer.
```

An equation for the error in layer $L$ in terms of the error in the next layer $L+1$ [@nielsen2015neural, p. 45]:

```{=latex}
$$\updelta^{l} = ((w^{l+1})^{T} \updelta^{l+1}) \odot  \sigma'(z^{l})$$

Where $(w^{l+1})^{T}$ is the transpose of the weight matrix $w^{l+1}$ for the (l+1)-th layer.
```

This equation allows us to take the error term from the final layer, and pass it backwards to any layer we want.
```

### 202101050719 How to Build and Train Neural Network.txt

```
The following steps describe how to build and train a simple vanilla feedforward neural network [@nielsen2015neural, Ch. 1].  This is a high level overview of all of the components.

1. Choose your architecture.
    1. Choose the type(s) of neurons and their associated **activation function** (e.g. Perceptron, Sigmoid, ReLU). [[202101120811 Activation Functions]]
    2. Choose the number of **layers** (see [[202101120654 Neural Network Layers]]).
    3. Choose the number of neurons in your input layer, hidden layers, and output layer.
2. **Initialize the weights**.  There are many different initialization strategies.  Often the strategy depends on the activation function that you choose.  Two common strategies are random initialization over a Gaussian distribution, and initializing all weights at 0.
3. Choose a **cost function** (e.g. mean squared error or cross entropy) (see [[202012261442 Cost Functions]])
4. Choose an **optimizer** (e.g. gradient descent, stochastic gradient descent, mini-batch gradient descent, Adagrad, Adam...).
5. Train your model, one epoch at a time, until some criteria.  As an example, you could train the model until the error on the test set doesn't go down for 5 straight epochs.
```

### 202103160829 Adam (Adaptive Moment Estimation).txt

```
Like other methods, Adam also computes adaptive learning rates for each parameter.

You can think of Adam as RMSprop + momentum [@DBLP:journals/corr/Ruder16, p. 8].

From Ruder [@DBLP:journals/corr/Ruder16, p. 7]:

```{=latex}
In addition to storing an exponentially decaying average of past squared gradients $v_t$ like Adadelta and RMSprop, Adam also keeps an exponentially decaying average of past gradients $m_t$, similar to momentum:

\begin{align}
\begin{split}
m_t &= \beta_1 m_{t-1} + (1 - \beta_1) g_t\\
v_t &= \beta_2 v_{t-1} + (1 - \beta_2) g_t^2
\end{split}
\end{align}

$m_t$ and $v_t$ are estimates of the first moment (the mean) and the second moment (the uncentered variance) of the gradients respectively, hence the name of the method.
```
```

### 202101110722 Main Challenges of Gradient Descent.txt

```
There exist two main challenges to learning with gradient descent [@geron2017hands, p118] [@chollet2018deep, p. 50]:

1. Slow convergence speed / plateaus
2. Getting stuck in local minima

Plateaus mean that training can stall for epochs on end.  It can be difficult to determine if you found the global maximum, or if the model will continue to improve if only you train longer.  Similarly, a model can get stuck in a local minimum.

Sebastian Ruder lists four challenges with vanilla mini-batch gradient descent [@DBLP:journals/corr/Ruder16, p. 3]:

1. It is difficult to know what the optimal learning rate is.  It's another hyperparameter you need to set.
2. Learning rate schedules attempt to solve this problem, but they need to be set ahead of time.  They don't adapt to the data.
3. The learning rate applies to all parameters equally.  Some parameters may not need to be updated very frequently.  E.g. your model inputs could be sparse, and you might not need to update the weights for a rarely occurring feature very frequently.
4. Mini-batch gradient descent is susceptible to getting stuck in local minima or saddle points.
```

### 202101201802 Three Factors Led to the Adoption of Gradient Descent for ML.txt

```
According to Yann LeCun, three factors led to the widespread adoption of gradient descent (see [[202101050843 Gradient Descent]]) within the machine learning community [@lecun1998gradient, p. 3]:

1. The first was the realization that getting stuck in a local minima wasn't a problem in practice.  This was noticed when attempting to train Boltzmann machines with gradient-based learning-techniques.
2. Second, Rumelhart, Hinton, and Williams [@RumelhartDavidE1987LIRb] showed that it was possible to efficiently compute gradients via backpropagation.
3. Third, it was shown that multi-layer neural networks could be trained efficiently with the sigmoid activation function (see [[202012261450 Sigmoid Neuron]]) and backpropagation (see [[202101130721 Mathematics of Backpropagation]]).
```

### 202106160834 Method of Least Squares.txt

```
Ordinary Least Squares is an estimator [[202106160905 Estimator]].

The properties of least squares estimators are based on the assumptions here [[202107041023 Least Squares Estimator Assumptions]] [@chatterjee2012regression, p.94].

If the assumptions are met, least squares estimators have the following properties [@chatterjee2012regression, p.67]:

1. The estimator is an unbiased estimate of the model coefficients.
2. The sampling distribution of the model coefficients are normally distributed with a mean of our estimate, and we can calculate the variance of the sampling distribution.
```

