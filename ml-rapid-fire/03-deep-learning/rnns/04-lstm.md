# LSTM

**Q:** What is an LSTM and why was it invented?

**A:**

- **Long Short-Term Memory**: solves vanishing gradient problem
- Has **cell state** with self-edge of fixed weight=1 (constant error carousel)
- Three gates control information flow: forget, input, output
- Can learn dependencies over 100+ time steps
- Default choice for sequence tasks before Transformers

---
