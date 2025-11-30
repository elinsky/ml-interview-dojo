# Word2Vec

**Q:** How does Word2Vec work?
- Two architectures
- Training objective
- Key hyperparameters

**A:**

- **Two architectures**:
  - **CBOW** (Continuous Bag of Words): predict center word from context
  - **Skip-gram**: predict context words from center word
  - Skip-gram better for rare words, CBOW faster
- **Training objective**:
  - Maximize probability of context words given target (or vice versa)
  - Use negative sampling: contrast true pairs with random negatives
- **Key hyperparameters**:
  - Window size: how many context words (typically 5-10)
  - Embedding dimension (typically 100-300)
  - Number of negative samples
- **Output**: word → vector lookup table
- **Pre-trained**: Google News Word2Vec (3M words, 300 dims)

---
