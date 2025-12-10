# Common Activation Functions

**Q:** What are the most common activation functions?

**A:**

- **ReLU**: max(0, x) — default for hidden layers, avoids vanishing gradient
- **Sigmoid**: 1/(1+e^-x) — outputs 0-1, binary classification output
- **Tanh**: outputs -1 to 1, zero-centered
- **Softmax**: outputs sum to 1, multi-class classification output
- **Leaky ReLU**: allows small negative slope, fixes "dying ReLU"

---
