# Document Embeddings

**Q:** How do you get embeddings for entire documents?
- Simple methods
- Doc2Vec
- Modern approaches

**A:**

- **Simple methods**:
  - Average word vectors (surprisingly effective baseline)
  - TF-IDF weighted average
  - Max pooling over word vectors
- **Doc2Vec** (Paragraph Vectors):
  - Extension of Word2Vec
  - Learn document vector alongside word vectors
  - PV-DM: predict word from context + document vector
  - PV-DBOW: predict words from document vector alone
- **Modern approaches**:
  - BERT [CLS] token embedding
  - Sentence transformers (fine-tuned for sentence similarity)
  - Mean pooling over BERT outputs
- **Finance example**: represent SEC 10-K filings as vectors for similarity search or clustering

---
