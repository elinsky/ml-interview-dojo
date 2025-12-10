# Maximum Likelihood Estimation (Intuition)

**Q:** What is the intuition behind Maximum Likelihood Estimation?
- Core idea
- Likelihood function
- What MLE finds

**A:**

- **Core idea**: find parameter values that make the observed data most probable
- **Likelihood function**: L(θ) = P(data | θ) — probability of observed data as function of parameters
- **MLE**: θ̂_MLE = argmax L(θ) = argmax P(data | θ)
- **Key insight**: we're not finding P(θ | data); we're finding θ that maximizes P(data | θ)
- **Why it works**: intuitively, if we observed this data, parameters that make it likely are probably close to truth

---
