# Softmax Cross-Entropy

**Q:** Why pair softmax with cross-entropy loss?

**A:**

- Combined gradient is simple: (p - y)
- Numerically stable when computed together
  - Softmax converts logits to probabilities
  - Cross-entropy measures prediction quality

**See also:** [[202101171354 Softmax Activation Function]]

---
