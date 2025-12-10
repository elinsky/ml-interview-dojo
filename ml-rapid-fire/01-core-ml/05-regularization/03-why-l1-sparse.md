# Why L1 Produces Sparsity

**Q:** Why does L1 regularization produce sparse weights (zeros)?

**A:**

- L1 gradient is **constant** (±λ) regardless of weight magnitude
- Small weights get pushed **all the way to zero**
- Geometric: diamond constraint, solutions hit **corners** (where weights = 0)
- Result: **automatic feature selection** (irrelevant features get zero weight)

---
