# Why L2 Only Shrinks Weights

**Q:** Why does L2 regularization only shrink weights but not zero them out?

**A:**

- L2 gradient is **proportional to weight** (2λw)
- As weight → 0, gradient → 0 (shrinking **slows down**)
- Weights shrink but **never reach exactly zero**
- Result: **less sparse** than L1, keeps all features with small weights

---
