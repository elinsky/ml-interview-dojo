# Question

What are saddle points and local minima? Which are thought to cause more problems for training large NNs?

# Answer

**Local minima** are points where the gradient is zero and the function value is lower than all nearby points - essentially valleys in the loss landscape where gradient descent can get stuck, unable to find better solutions.

**Saddle points** are points where the gradient is also zero, but unlike local minima, they are not local minimums in all directions. In some dimensions the point is a minimum, while in other dimensions it's a maximum - like a mountain pass or the center of a saddle. The gradient is flat, which can slow or stall training.

**Saddle points are thought to cause more problems for training large neural networks.** This is somewhat counterintuitive, but there are important reasons:

**Why saddle points are more problematic:**

1. **High-dimensional spaces have more saddle points**: In high-dimensional optimization landscapes (modern neural networks have millions or billions of parameters), saddle points vastly outnumber local minima. As dimensionality increases, the probability of all dimensions simultaneously forming a local minimum decreases exponentially.

2. **Plateaus around saddle points slow training**: Saddle points are often surrounded by plateau regions where gradients are very small. Training can stall for many epochs in these flat regions, making it difficult to determine whether optimization should continue or has converged.

3. **Local minima aren't actually a problem in practice**: Empirical evidence shows that local minima rarely cause issues when training large neural networks. Yann LeCun noted that "getting stuck in a local minima wasn't a problem in practice" - this was observed when training Boltzmann machines with gradient-based techniques.

**Solutions that help escape saddle points:**

- **Momentum-based optimizers** (momentum, Nesterov, Adam) help by accumulating velocity, allowing the optimizer to roll through flat regions and escape saddle points
- **Adaptive learning rate methods** (AdaGrad, RMSProp, Adam) adjust per-parameter learning rates, helping navigate complex landscapes
- **Stochastic gradient descent** introduces noise that can help escape both saddle points and shallow local minima

---

## Extracts from my notes

### 202101110722 Main Challenges of Gradient Descent.txt

```
## Chollet and Geron's List

There exist two main challenges to learning with gradient descent [@geron2017hands, p118] [@chollet2018deep, p. 50]:

1. Slow convergence speed / plateaus
2. Getting stuck in local minima

Plateaus mean that training can stall for epochs on end.  It can be difficult to determine if you found the global maximum, or if the model will continue to improve if only you train longer.  Similarly, a model can get stuck in a local minimum.

The momentum algorithm addresses both of these issues ([[202101110723 Momentum Gradient Descent Optimizer]])

## Ruder's List

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

## Gaps filled by me (not from notes)

The specific distinction between saddle points and local minima, why high-dimensional spaces have more saddle points, and the detailed explanation of why saddle points are more problematic than local minima in large neural networks were synthesized to directly answer the question, as my notes didn't contain these specific mathematical details.

