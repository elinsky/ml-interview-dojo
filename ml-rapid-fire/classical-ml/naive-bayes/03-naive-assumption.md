# The Naive Assumption

**Q:** What is the "naive" assumption in Naive Bayes?

**A:**

- Features are **conditionally independent** given the class label
- P(x₁, x₂, ..., xₙ | class) = P(x₁|class) · P(x₂|class) · ... · P(xₙ|class)
- Allows computing likelihood as product of individual feature probabilities
- **Rarely true** in real data (features often correlated)
- Still works well because we only need correct **ranking**, not exact probabilities
- Dramatically reduces parameters: O(n·k) instead of O(kⁿ)
- **Correlated features hurt**: redundant features get "voted twice" → remove highly correlated

---
