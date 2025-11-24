# Question

Why does L1 regularization tend to lead to sparsity while L2 regularization pushes weights closer to 0?

# Answer

Both L1 and L2 regularization add penalty terms to the cost function that discourage large weights, but they differ fundamentally in how they penalize weights, leading to different behaviors.

**Core Mechanism:**

Regularization minimizes: `Cost(h) = EmpLoss(h) + λ * Complexity(h)`, where the complexity term differs between L1 and L2.

**L1 Regularization (Lasso):**

- **Penalty term**: λ * Σ|w| (sum of absolute values of weights)
- **Effect**: Tends to produce sparse models where many weights are exactly zero, while a few weights remain large
- **Why sparsity occurs**: The absolute value function has a non-differentiable point at zero with a constant gradient everywhere else. During optimization, this creates a penalty that doesn't decrease as weights approach zero, making it energetically favorable to push weights all the way to exactly zero rather than keeping them small but non-zero. Geometrically, L1's constraint region forms a diamond shape in 2D (or hypercube corners in higher dimensions), where the corners lie on the coordinate axes—exactly where some coefficients are zero.

**L2 Regularization (Ridge / Weight Decay):**

- **Penalty term**: λ * Σw² (sum of squared weights)
- **Effect**: Pushes all weights toward zero but rarely makes them exactly zero. Produces models where parameters are small but non-sparse
- **Why weights approach (but don't reach) zero**: The squared penalty creates a gradient proportional to the weight value itself. As weights get smaller, the penalty's gradient also decreases, making it less energetically favorable to push weights all the way to zero. The optimization settles on small but non-zero values. Geometrically, L2's constraint region is circular (or spherical in higher dimensions), with no corners, so the optimal solution typically has all weights small but non-zero.

**Key Differences:**

| Aspect | L1 (Lasso) | L2 (Ridge) |
|--------|------------|------------|
| **Mathematical form** | λ * Σ\|w\| | λ * Σw² |
| **Gradient** | Constant magnitude (±λ) except at 0 | Proportional to weight (2λw) |
| **Sparsity** | Many weights exactly = 0 | Weights approach but rarely = 0 |
| **Use case** | Feature selection, interpretability | Preventing overfitting without feature selection |
| **Geometry** | Diamond/hypercube corners | Circle/sphere |

**Practical Implications:**

- **L1 is preferred when**: You want automatic feature selection, need an interpretable model with fewer features, or believe many features are irrelevant
- **L2 is preferred when**: All features are potentially useful, you want to prevent overfitting without eliminating features, or you need to prevent weight saturation in neural networks
- **Weight decay interpretation (L2 in neural networks)**: L2 creates a gradient that always points toward zero weights, creating "inertia" that prevents weights from growing large and helps prevent saturation during training

---

## Extracts from my notes

### 202101171802 L1 Regularization.txt

> ## Neural Networks
>
> In neural networks, the L1 regularization term can be mathematically expressed as [@nielsen2015neural, p. 87]:

$$
\frac{\lambda}{n} \sum_{w} \left| w \right|
$$
> Where $w$ represents the weights in the neural network, $n$ represents the number of training examples, and $\lambda$ is the \emph{regularization parameter}.

> Similarly to in linear regression, L1 regularization tends to produce a neural network where many weights are close to zero (and thus not doing much) while a few weights are large and do most of the work.

## Linear Regression

In linear regression, L1 can be expressed mathematically as [@james2013introduction, p. 219]:

$$
\lambda \sum_{j=1}^{p} \left| \beta_{j} \right|
$$
Where $\lambda \geq 0$ is a \emph{tuning parameter}, $\beta$ is a model coefficient, and $p$ represents the number of model parameters.

### 202101171731 L2 Regularization.txt

> The regularization term is added to the cost function.  Regardless of the type of model that L2 regularization is applied to, L2 regularization tends to produce models that prefer smaller model parameters over larger ones.  Thus larger model parameters are only learned if their benefit outweighs their cost.
>
> ## Neural Networks
>
> For neural networks, L2 regularization is typically applied to the model's weights, and can also be known as 'weight decay'.  The regularization term can be expressed mathematically as [@nielsen2015neural, p. 79]:

$$
\frac{\lambda}{2n} \sum_{w} w^{2}
$$
> Where $w$ represents the weights in the neural network, $n$ represents the number of training examples, and $\lambda$ is the \emph{regularization parameter}.  Note that the 2 in the denominator is only there to simplify the calculation of the derivative.

> It is called weight decay because when you compute the partial derivative of the cost function with the regularization term, the regularization term always creates a little gradient that leads downhill to a point where all the weights are 0.

> Regularization in neural networks does seem to have some benefits other than just reducing overfitting.  Empirically regularization seems to help prevent weights from getting 'saturated' [@nielsen2015neural, p. 83].  When weights get saturated, learning tends to slow down because the gradient is close to flat.

> Another way to think of L2 regularization in neural networks is to view weight decay as preventing small changes in input data from changing the weights by too much.  It is as if there is some inertia preventing the model from making the weights bigger.

## Linear Regression

In a linear regression (see [[202106150747 Linear Regression Model]]), L2 regularization is applied to the model coefficients and is expressed mathematically as [@james2013introduction, p. 215]:

$$
\lambda \sum_{j=1}^{p} \beta_{j}^{2}
$$
Where $\lambda \geq 0$ is a \emph{tuning parameter}, $\beta$ is a model coefficient, and $p$ represents the number of model parameters.

### 202104170846 Regularization.txt

> Regularization is the process of selecting a hypothesis that minimizes both the empirical loss and the complexity of the hypothesis [@russell2010artificial, p. 713].  Mathematically, it can be described as:

$$
Cost(h) = EmpLoss(h) + \lambda Complexity(h) \nonumber
$$

$$
\hat h^* = \argminA_{h \in \mathcal{H}} Cost(h) \nonumber
$$

> Where $h$ is a hypothesis, $\hat h^*$ is the estimated best hypothesis, $\mathcal{H}$ is your hypothesis space, and $\lambda$ is a positive number that serves as a conversion rate between loss and hypothesis complexity.

### 202107210839 Shrinkage (Statistics).txt

> From Harrell [@harrell2015regression, p.75]:
>
> > Shrinkage is a statistical estimation method that preshrinks regression coefficients towards zero so that the calibration plot for new data will not need shrinkage as its calibration plot will be one.
>
> We know that if you meet the required least squares regression assumptions (see [[202107041109 Least Squares Normality Assumption]]), then you can confidently say that your regression coefficients and intercept will be **unbiased** estimates of the true parameters.
>
> This interpretation holds if you choose to highlight coefficients at random. But if you highlight a coefficient not chosen at random (say you focus on small and large coefficients) the interpretation no longer holds [@harrell2015regression, p.76].

## Gaps filled by me (not from notes)

The geometric explanation of why L1 creates sparsity (diamond-shaped constraint region with corners on axes) versus why L2 doesn't (circular constraint region without corners), the gradient behavior comparison showing why L1 has constant gradient while L2 has proportional gradient, and the practical decision criteria for choosing between L1 and L2 were synthesized from ML optimization theory. My notes provided the mathematical formulations and high-level effects but didn't explain the underlying geometric/calculus reasons for the different behaviors.
