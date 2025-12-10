# Log Probabilities

**Q:** Why use log probabilities in Naive Bayes?

**A:**

- **Problem**: multiplying many small probabilities → numerical underflow
- **Solution**: work in log space — convert products to sums
- log P(class|x) ∝ log P(class) + Σ log P(xᵢ|class)
- Numerically stable for high-dimensional data (many features)
- argmax is preserved under log (monotonic) transformation
- Standard practice in all Naive Bayes implementations
- Also called **log-likelihood**

---
