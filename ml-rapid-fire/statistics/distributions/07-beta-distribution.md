# Beta Distribution

**Q:** What is the beta distribution and why is it useful?
- Support (range)
- Parameters and their interpretation
- Key use case in Bayesian inference

**A:**

- **Support**: bounded on [0, 1] — perfect for modeling probabilities
- **Parameters**: Beta(α, β) — α-1 = "pseudo-count" of successes, β-1 = "pseudo-count" of failures
- **Mean**: E[X] = α / (α + β)
- **Bayesian use**: conjugate prior for binomial likelihood; Beta prior + binomial data → Beta posterior
- **Example**: modeling uncertainty about a strategy's true win rate

---
