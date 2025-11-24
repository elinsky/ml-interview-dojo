# Question

What makes a classification problem different from a regression problem?

# Answer

The fundamental difference between classification and regression lies in the type of output they predict:

**Classification** predicts discrete categorical labels or classes. The output is qualitative - it assigns inputs to one of a finite set of categories. Examples: spam vs not spam, cat vs dog vs bird, benign vs malignant tumor.

**Regression** predicts continuous numerical values. The output is quantitative - it estimates a real-valued number. Examples: house prices, temperature, stock prices, age estimation.

**Key differences:**

| Aspect | Classification | Regression |
|--------|---------------|------------|
| **Output type** | Discrete categories/labels | Continuous numerical values |
| **Output space** | Finite set of classes | Infinite real numbers (or bounded range) |
| **Evaluation metrics** | Accuracy, Precision, Recall, F1, AUC-ROC | MSE, RMSE, MAE, R² |
| **Loss functions** | Cross-entropy, hinge loss, log-likelihood | Mean squared error, absolute error |
| **Final layer activation** | Softmax (multi-class), Sigmoid (binary) | Linear (no activation) or Sigmoid (0-1 range) |
| **Decision** | Hard boundaries between classes | Smooth function over continuous space |

---

## Extracts from my notes

### 202106150747 Linear Regression Model.txt

```
Linear models can be expressed mathematically as [@chatterjee2012regression, p. xiii]:

$$Y = \beta_0 + \beta_1X_1 + \dots + \beta_pX_p + \epsilon$$

Where $\epsilon$ is assumed to be a random error representing the discrepancy in the approximation. And $\beta_0, \beta_1, \dots, \beta_p$ are the regression parameters or coefficients. And $Y$ is the response variable. And $p$ denotes the number of predictor variables.

Linear models can be expressed mathematically as [@geron2017hands, p112]:

$$\hat y = \theta_{0} + \theta_{1} x_{1} + \theta_{2} x_{2} + \dots + \theta_{n} x_{n}$$

Where $\hat y$ is your prediction, $\theta_{0}$ is your bias term, $(\theta_{1}, \theta_{2}, ..., \theta_{n})$ are your feature weights, $n$ is the number of features, and $x_{i}$ is the i-th feature.

Linear regression is popular because it is very _simple_ and easily understood.

Linear models are well suited for inference problems [[202106191007 Prediction vs Inference]].
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
| Multiclass, multilabel classification   | Sigmoid               | binary_crossentropy        |
| Regression to arbitrary values          | None                  | mse                        |
| Regression to values between 0 and 1    | Sigmoid               | mse or binary_crossentropy |
```

### 202012261442 Cost Functions.txt

```
François Chollet recommends the following cost functions for these problems [@chollet2018deep, p. 60]:

| Problem                   | Cost Function                                    |
|---------------------------|--------------------------------------------------|
| Regression                | Mean Squared Error                               |
| Binary Classification     | Binary Cross-Entropy Cost                        |
| Multiclass Classification | Categorical Cross-Entropy Cost                   |
| Sequence-Learning         | Connectionist Temporal Classification (CTC) Cost |
```

### 202101050745 Mean Squared Error Cost Function.txt

```
The mean squared error cost function (AKA quadratic cost) is one of the most commonly used cost functions in neural networks.  Informally, it penalizes large errors way more than it penalizes small errors.

Algebraically, it is defined as [@nielsen2015neural, p. 16]:

```{=latex}
\begin{equation}
    J(\theta) = \frac{1}{2n} \sum_{x} \| h_{\theta}(x) - y \|^{2}
 \end{equation}
```

$J$ is typically used to denote a cost function.  $\theta$ often represents the model parameters, which are the weights and biases in our case.
```

### 202101120828 Cross-Entropy Cost.txt

```
Cross-entropy cost is a cost function used in machine learning models to measure the quality of the model's predictions.

The primary benefit of cross-entropy cost over quadratic cost (see [[202101050745 Mean Squared Error Cost Function]]) is that cross-entropy cost does not suffer from a learning slowdown when the sigmoid neuron (see [[202012261450 Sigmoid Neuron]]) is saturated [@nielsen2015neural, p. 63].

From François Chollet [@chollet2018deep, p. 73]:

> Crossentropy is usually the best choice when you're dealing with models that output probabilities.

From Michael Nielsen [@nielsen2015neural, p. 66]

> When should we use the cross-entropy instead of the quadratic cost?  In fact, the cross-entropy is nearly always the better choice, provided the output neurons are sigmoid neurons.
```

### 202012261450 Sigmoid Neuron.txt

```
The sigmoid neuron is an artificial neuron used in neural networks.  Specifically, the sigmoid function is used as the **activation function** for the neuron.

The sigmoid function is defined as [@nielsen2015neural, p. 8]:

```{=latex}
\begin{equation}
\sigma(x)= \frac{1}{1 + e^{-z}}
\end{equation}
```

Additionally, the output of a sigmoid neuron can be interpreted as a probability [@chollet2018deep, p. 71].
```

### 202101171354 Softmax Activation Function.txt

```
The softmax activation function is primarily used in the output layer of neural networks.  The desirable property of the softmax function is that it ensures the outputs in the final layer of a neural network sum to 1.  This is useful when you have a multi-class classification problem and you want to build a model that predicts the probability that a training example is a part of each class.

The softmax function is defined mathematically as [@nielsen2015neural, p. 70]:

```{=latex}
\begin{equation}
a_{j}^{L} = \frac{e^{x^{L}_j}}{\sum_{k} e^{z^{l}_{k}}}
\end{equation}
Where $a_{j}^{L}$ is the activation of the $j$-th neuron in the last layer.
```
```

### 202101011346 Perceptron.txt

```
The perceptron is an artificial neuron that uses a Heaviside step function as its activation function.  A perceptron is one of the simplest and earliest artificial neurons.  You can also think of a perceptron as a linear binary classifier.

To put it in precise algebraic terms, the perceptron output is defined as [@nielsen2015neural, p. 4]:

```{=latex}
\begin{equation}
  \text{output}=\begin{cases}
    0 & \text{if $w \cdot x + b \leq 0$}\\
    1 & \text{$w \cdot x + b > 0$}
  \end{cases}
  \nonumber
\end{equation}
```
```

## Gaps filled by me (not from notes)

The comparison table and specific examples were synthesized based on ML fundamentals. My notes provided comprehensive coverage of the mathematical foundations for both regression (linear regression with MSE) and classification (logistic regression, perceptron, sigmoid/softmax activations with cross-entropy).
