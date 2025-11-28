# Loss Function vs Evaluation Metric

**Q:** What is the difference between a loss function and an evaluation metric?

**A:**

**Loss function**:
- Used during **training** to optimize the model
- Must be **differentiable** for gradient-based methods
- Examples: MSE, cross-entropy

**Evaluation metric**:
- Used to measure **real-world performance** (not during training)
- Doesn't need to be differentiable
- Examples: accuracy, F1, AUC

They can differ (e.g., train with cross-entropy, evaluate with accuracy).

---
