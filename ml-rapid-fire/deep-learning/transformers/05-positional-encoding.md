# Positional Encoding

**Q:** How do Transformers handle sequential order without recurrence?

**A:**

- Add positional encodings to input embeddings
- Original paper: sinusoidal functions (sin/cos)
- Alternative: learned position embeddings
- **Relative position embeddings** (XLNet) generalize better than absolute
- Without this, Transformer is permutation invariant

**See also:** [[202105270800 Transformers]], [[202201260710 Summary - XLNet]]

---
