# Bias of an Estimator

**Q:** What is bias in an estimator?
- Definition and formula
- Unbiased estimator
- Examples of biased vs unbiased

**A:**

- **Definition**: Bias(θ̂) = E[θ̂] - θ — expected difference from true value
- **Unbiased**: E[θ̂] = θ (on average, hits the true value)
- **Examples**:
  - Sample mean x̄ is unbiased for μ
  - Sample variance with 1/n is biased; with 1/(n-1) is unbiased
  - MLE can be biased in small samples
- **Note**: unbiased ≠ good; a biased estimator with lower variance may have lower MSE

---
