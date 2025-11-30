# Word Embeddings Introduction

**Q:** What are word embeddings and why are they better than sparse representations?
- What they are
- Key properties
- Why better than BoW/TF-IDF

**A:**

- **What they are**: dense, low-dimensional vectors (typically 50-300 dims) representing words
- **Key properties**:
  - Learned from data (not hand-crafted)
  - Semantic similarity → vector similarity
  - Famous example: king - man + woman ≈ queen
- **Why better than BoW/TF-IDF**:
  - Dense (not sparse) — more efficient
  - Captures semantic relationships
  - Generalizes to unseen words with similar contexts
  - Lower dimensional (50-300 vs vocabulary size)
- **Key insight**: "you shall know a word by the company it keeps" — words in similar contexts have similar meanings
- **Limitation**: one vector per word (no context sensitivity) — addressed by contextual embeddings (BERT)

---
