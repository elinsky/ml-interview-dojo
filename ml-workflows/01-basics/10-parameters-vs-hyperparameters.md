# Question

What are the differences between parameters and hyperparameters?

# Answer

**Parameters** are the internal variables that the model learns from data during training. They are updated automatically by the optimization algorithm (gradient descent, Adam, etc.) to minimize the loss function. In neural networks, parameters include weights and biases.

**Hyperparameters** are configuration settings that control the learning process itself. They must be set before training begins and are not learned from the data. Hyperparameters define the model architecture and training strategy.

**Key differences:**

| Aspect | Parameters | Hyperparameters |
|--------|-----------|-----------------|
| **Learned or set?** | Learned automatically from data during training | Set manually before training begins |
| **Updated how?** | Updated via backpropagation and optimization algorithms | Fixed during training (though can be changed between training runs) |
| **What they control** | The model's ability to make predictions | The learning process and model structure |
| **Optimization** | Optimized by gradient descent | Optimized by hyperparameter tuning (grid search, random search, Bayesian optimization) |

**Examples of parameters:**

- **Weights** (W): Connection strengths between neurons in neural networks
- **Biases** (b): Offset terms added to weighted sums
- Coefficients in linear regression
- Cluster centers in k-means

**Examples of hyperparameters:**
From the neural network training workflow, hyperparameters include:

1. **Architecture choices:**
   - Number of layers
   - Number of neurons per layer
   - Type of activation functions (ReLU, sigmoid, tanh)

2. **Training configuration:**
   - Learning rate
   - Batch size
   - Number of epochs
   - Optimizer choice (SGD, Adam, RMSProp)

3. **Regularization settings:**
   - Dropout rate
   - L1/L2 regularization strength (λ)
   - Weight initialization strategy

4. **Cost function selection:**
   - Mean squared error, cross-entropy, etc.

**Why the distinction matters:** Parameters determine what the model predicts, while hyperparameters determine how well the model learns to make those predictions. Poor hyperparameter choices can prevent a model from learning effectively, even if it has sufficient capacity.

---

## Extracts from my notes

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

### 202012261442 Cost Functions.txt

```
A cost function measures how poorly a model does at predicting the right answer.  The output of a cost function can also be thought of as a 'distance score' [@chollet2018deep, p. 10].  The score is a measure of the distance between the desired model output (or ground truth) and the actual model output.

Why are cost functions important?  The inputs to a cost function are your model parameters.  So if you have an optimization algorithm (e.g. gradient descent), then you can use it to find the set of parameters that minimize your cost function.  A cost function plus an optimization algorithm essentially enables you to fit your model.
```

### 202106191115 Bias-Variance Trade-Off.txt

```
From _An Introduction to Statistical Learning_ [@james2013introduction, p. 33]:

> It is possible to show that the expected test MSE, for a given value $x_0$, can always be decomposed into the sum off three fundamental quantities: the variance of $\hat f (x_0)$, the squared bias of $\hat f (x_0)$ and the variance of the error terms $\epsilon$. That is,
> $$E(y_0 - \hat f (x_0))^2 = Var(\hat f(x_0)) + [Bias(\hat f (x_0))]^2 + Var(\epsilon)$$

Variance refers to the amount by which $\hat f$ would change if we estimated it using a different training data set. In general, more flexible statistical models have higher variance.

Bias refers to the error that is introduced by approximating a real-life problem, which may be extremely complicated, by a much simpler model.

The goal is to find a learning method that has both low variance and low bias. But generally, as you increase the flexibility of a learning method, the bias will decrease and the variance will increase.

As an example, a linear regression model will tend to have high bias but low variance. As for a random forest, it will tend to have high variance and low bias.
```

### 202101171833 Hyperparameter Tuning for Learning Rate in Neural Networks.txt

```
With true gradient descent, small learning rates are more prone to get stuck in local minima.  Large learning rates are prone to overshooting.

I think you want to start with the largest learning rate for which your loss starts decreasing.  Then step down the learning rate over time, using a learning schedule.
```

## Gaps filled by me (not from notes)

The formal comparison table of parameters vs hyperparameters was synthesized to directly answer the question, as my notes focused on specific training workflows rather than explicitly defining the distinction between these terms.
