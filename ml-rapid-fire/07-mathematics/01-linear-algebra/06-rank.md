# Matrix Rank

**Q:** What is matrix rank and why does it matter?
- Definition
- How to determine
- Full rank vs rank deficient
- ML relevance

**A:**

- **Definition**: number of linearly independent rows (or columns) — row rank = column rank
- **Determine by**: counting non-zero singular values, or row reduction
- **Full rank**: rank = min(m, n); matrix has maximum possible rank
- **Rank deficient**: some rows/columns are linear combinations of others
- **ML relevance**:
  - Rank deficient → singular (no unique solution to Ax = b)
  - Feature matrix rank → effective number of features (collinearity reduces rank)
  - Low-rank approximation for compression (SVD)

---
