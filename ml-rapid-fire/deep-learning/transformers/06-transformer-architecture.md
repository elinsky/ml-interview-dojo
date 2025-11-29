# Transformer Architecture

**Q:** What are the key components of the Transformer architecture?

**A:**

- Encoder: self-attention + feed-forward (×N layers)
- Decoder: masked self-attention + cross-attention + FF
- Layer norm and residual connections throughout
- No recurrence → fully parallelizable (unlike RNNs)
- O(n²) complexity for sequence length n

**See also:** [[202105270800 Transformers]]

---
