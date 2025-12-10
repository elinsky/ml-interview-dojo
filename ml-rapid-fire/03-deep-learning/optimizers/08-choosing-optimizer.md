# Choosing an Optimizer

**Q:** How do you choose an optimizer?

**A:**

- **Adam**: good default, works well out-of-the-box
- **SGD + momentum**: often better final accuracy (with tuning)
- **AdamW**: Adam with proper weight decay (recommended for transformers)
- Start with Adam, switch to SGD if overfitting or want more accuracy

---
