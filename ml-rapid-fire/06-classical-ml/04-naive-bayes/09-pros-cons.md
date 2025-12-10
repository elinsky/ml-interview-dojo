# Naive Bayes Pros and Cons

**Q:** What are the pros and cons of Naive Bayes?

**A:**

- **Pros**:
  - Very fast training and prediction: O(n·d)
  - Works well with high-dimensional data (text)
  - **Needs less data** than most algorithms, less prone to overfit
  - Handles missing data naturally (just omit from product)
  - Provides probability estimates
  - Simple, interpretable, **parallelizable**
  - **Incremental**: easy to update with new data
  - Can be used as **generative model** to create synthetic data
- **Cons**:
  - Naive independence assumption often violated
  - **Correlated features hurt** (get "voted twice")
  - Probability estimates can be poorly calibrated
  - Cannot learn feature interactions
- **Best for**: categorical inputs; for continuous, ensure near-Gaussian

---
