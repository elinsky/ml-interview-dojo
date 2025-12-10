# What is Dimensionality Reduction?

**Q:** What is dimensionality reduction and why is it useful?

**A:**

- Reducing number of features while preserving important information
- **Unsupervised learning** technique — no labels needed
- Why reduce dimensions:
  - **Curse of dimensionality**: distances become meaningless in high-D
  - **Visualization**: project to 2D/3D for plotting
  - **Noise reduction**: remove irrelevant features
  - **Speed**: fewer features = faster training
  - **Storage**: less memory needed
- **Fewer dimensions = simpler model = less overfitting**
- Four main approaches:
  - **Feature selection**: filter (correlation) or wrapper (RFE) methods
  - **Matrix factorization**: PCA, SVD
  - **Manifold learning**: t-SNE, UMAP, MDS
  - **Autoencoders**: neural network bottleneck
- Must apply same reduction to test data and new predictions

---
