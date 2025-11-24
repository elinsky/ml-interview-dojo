# Question

What's the difference between parametric and non-parametric methods? Give examples of each.

# Answer

The fundamental difference between parametric and non-parametric models lies in whether they make assumptions about the functional form of the underlying function being learned.

**Parametric Models:**
- Have a fixed number of parameters determined before training (independent of training set size)
- Make explicit assumptions about the functional form of the function being learned
- Reduce the learning problem to estimating a fixed set of parameters
- **Advantage**: Require fewer training examples; simpler and faster to train; easier to interpret
- **Disadvantage**: Risk choosing wrong functional form; may not approximate true function well; limited flexibility

**Non-Parametric Models:**
- Number of parameters grows with the training data (unbounded parameter set)
- Make no explicit assumptions about the functional form
- Often retain training examples as part of the model (instance-based/memory-based learning)
- **Advantage**: More flexible; can fit wider range of functions; don't risk wrong functional form assumption
- **Disadvantage**: Require many more training examples; prone to overfitting; computationally expensive

**Key Distinction:** Parametric models summarize data into a fixed set of parameters, while non-parametric models grow in complexity with the data.

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

### 202106150747 Linear Regression Model.txt

```
Linear models can be expressed mathematically as [@chatterjee2012regression, p. xiii]:

$$Y = \beta_0 + \beta_1X_1 + \dots + \beta_pX_p + \epsilon$$

Where $\epsilon$ is assumed to be a random error representing the discrepancy in the approximation. And $\beta_0, \beta_1, \dots, \beta_p$ are the regression parameters or coefficients. And $Y$ is the response variable. And $p$ denotes the number of predictor variables.

Linear regression is popular because it is very _simple_ and easily understood.

Linear regression is an example of a parametric model (see [[202104170948 Parametric Models]]).
```

### 202104151745 Decision Trees.txt

```
Decision trees can be used for classification and regression tasks.  The model's **representation** takes the form of a binary tree.  Each internal node in the tree represents a test of the value of one of the attributes/features.  Each branch from the node is labelled with possible values of the splitting attribute.  Each leaf specifies a value to be returned by the function.

Decision trees are non-parametric models.  That means that the number of parameters is not known or set before model training begins.  This means that the decision tree is free to split the data as many or few times as it wants.  This makes decision trees prone to **overfitting**.
```

## Gaps filled by me (not from notes)

The comparison of advantages/disadvantages and the summary were synthesized from the core definitions in my notes to directly answer the question.
