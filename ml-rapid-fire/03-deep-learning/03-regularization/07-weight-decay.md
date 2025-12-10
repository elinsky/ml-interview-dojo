# Weight Decay

**Q:** What is weight decay?

**A:**

- L2 regularization applied to neural network weights
- Adds lambda*||w||^2 to loss, penalizing large weights
- Gradient always pushes weights toward zero
- **AdamW**: decoupled weight decay (better than L2 with Adam)
- Typical values: 0.01, 0.001, 0.0001

---
