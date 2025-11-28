# Question

State Bayes' theorem and explain its role in updating beliefs with new information.

# Answer

**Bayes' Theorem:**

$P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$

Or in terms of parameters and data:

$P(\theta | \text{data}) = \frac{P(\text{data} | \theta) \cdot P(\theta)}{P(\text{data})}$

**Components:**
- $P(\theta)$: **Prior** - belief before seeing data
- $P(\text{data}|\theta)$: **Likelihood** - probability of data given parameters
- $P(\theta|\text{data})$: **Posterior** - updated belief after seeing data
- $P(\text{data})$: **Evidence** - normalizing constant (often ignored)

**Key insight:** Posterior $\propto$ Likelihood $\times$ Prior

**Conjugate priors (posterior same family as prior):**

| Likelihood | Conjugate Prior | Posterior |
|------------|-----------------|-----------|
| Binomial   | Beta            | Beta      |
| Normal (known var) | Normal   | Normal    |
| Poisson    | Gamma           | Gamma     |

**Finance applications:**

1. **Black-Litterman model:** Combine market equilibrium (prior) with investor views (likelihood)
2. **Bayesian VaR:** Incorporate parameter uncertainty into risk estimates
3. **Signal processing:** Update beliefs about true price from noisy observations
4. **Model selection:** Posterior model probabilities

**vs. Frequentist:** Bayesian treats parameters as random; frequentist treats them as fixed unknowns.
