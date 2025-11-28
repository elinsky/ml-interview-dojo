# Question

Explain Maximum Likelihood Estimation (MLE) and when it might fail.

# Answer

**MLE finds parameters that maximize the probability of observing the data:**

$\hat{\theta}_{MLE} = \arg\max_\theta L(\theta) = \arg\max_\theta \prod_{i=1}^n f(x_i | \theta)$

In practice, maximize **log-likelihood** (converts product to sum):

$\ell(\theta) = \sum_{i=1}^n \log f(x_i | \theta)$

**Properties (under regularity conditions):**
- **Consistent:** $\hat{\theta} \to \theta$ as $n \to \infty$
- **Asymptotically normal:** $\sqrt{n}(\hat{\theta} - \theta) \to N(0, I^{-1}(\theta))$
- **Asymptotically efficient:** Achieves Cramér-Rao lower bound

**Common examples:**
- Normal: $\hat{\mu} = \bar{x}$, $\hat{\sigma}^2 = \frac{1}{n}\sum(x_i - \bar{x})^2$
- Exponential: $\hat{\lambda} = 1/\bar{x}$
- Bernoulli: $\hat{p} = \bar{x}$

**When MLE fails or struggles:**

1. **Small samples:** Asymptotic properties don't kick in
2. **Multimodal likelihood:** May find local, not global, maximum
3. **Boundary issues:** Parameter estimate at boundary of space
4. **Heavy tails:** Outliers distort estimates
5. **Misspecified model:** MLE of wrong model is meaningless

**Finance application:** Calibrating volatility models, estimating distribution parameters for VaR
