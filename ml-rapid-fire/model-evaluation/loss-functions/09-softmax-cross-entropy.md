# Softmax Cross-Entropy

**Q:** Why pair softmax with cross-entropy loss?

**A:**

- Softmax converts logits to probabilities (sum to 1)
- Cross-entropy measures prediction quality
- Combined gradient is simple: (p - y)
- Numerically stable when computed together

**See also:** [[202101171354 Softmax Activation Function]], [[202101171406 Log-Likelihood Cost]]

---
