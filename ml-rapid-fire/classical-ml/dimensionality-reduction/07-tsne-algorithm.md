# t-SNE Algorithm

**Q:** How does t-SNE work?

**A:**

1. Compute pairwise similarities in **high-D** using Gaussian
   - p(i|j) = probability j is neighbor of i
2. Initialize points randomly in **low-D** space
3. Compute pairwise similarities in low-D using **t-distribution**
   - t-distribution has heavier tails → allows dissimilar points to be far apart
4. Minimize **KL divergence** between high-D and low-D distributions
5. Use gradient descent to move points

**Key insight**: t-distribution prevents "crowding problem" where all points collapse to center

**Perplexity**: roughly how many neighbors to consider (balance local vs global)

---
