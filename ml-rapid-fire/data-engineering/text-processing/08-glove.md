# GloVe

**Q:** How does GloVe differ from Word2Vec?
- Key idea
- Training method
- Comparison

**A:**

- **GloVe**: Global Vectors for Word Representation
- **Key idea**: combine count-based and prediction-based methods
  - Word2Vec uses local context windows
  - GloVe uses global co-occurrence statistics
- **Training method**:
  1. Build word-word co-occurrence matrix from corpus
  2. Learn vectors such that: w_i · w_j ≈ log(X_ij) (co-occurrence count)
  3. Weighted least squares objective (down-weight very frequent pairs)
- **Comparison with Word2Vec**:
  - GloVe: explicit use of global statistics, deterministic
  - Word2Vec: implicit, stochastic training
  - Similar performance in practice
- **Pre-trained**: Stanford GloVe (6B tokens, 50-300 dims)

---
