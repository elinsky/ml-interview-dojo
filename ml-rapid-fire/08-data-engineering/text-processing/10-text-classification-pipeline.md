# Text Classification Pipeline

**Q:** What's a typical pipeline for text classification?
- Classical approach
- Deep learning approach
- Choosing between them

**A:**

- **Classical approach**:
  1. Preprocess (lowercase, remove stopwords, stem/lemmatize)
  2. Vectorize (TF-IDF with n-grams)
  3. Train classifier (logistic regression, SVM, Naive Bayes)
  - Fast, interpretable, works well with small data
- **Deep learning approach**:
  1. Tokenize (minimal preprocessing)
  2. Embed (pre-trained or learned embeddings)
  3. Encode (LSTM, CNN, or Transformer)
  4. Classify (dense layers)
  - Better with lots of data, captures more nuance
- **Choosing**:
  - Small data, need interpretability → classical
  - Lots of data, complex patterns → deep learning
  - Modern: fine-tune pre-trained transformer (BERT)
- **Finance example**: sentiment classification of news headlines

---
