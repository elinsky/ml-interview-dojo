# RNN Limitations

**Q:** What are the main limitations of vanilla RNNs?

**A:**

- **Vanishing gradients**: can't learn long-range dependencies
- **Exploding gradients**: use gradient clipping
- Sigmoid → vanishing more likely; ReLU → exploding more likely
- Sequential processing = slow (can't parallelize)

---
