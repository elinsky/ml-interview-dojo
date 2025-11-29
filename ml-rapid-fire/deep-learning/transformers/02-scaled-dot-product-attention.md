# Scaled Dot-Product Attention

**Q:** How does scaled dot-product attention work?

**A:**

- Attention(Q,K,V) = softmax(QK^T / √d_k) V
- Q = queries, K = keys, V = values
- Dot product measures query-key similarity
- Scale by √d_k prevents softmax saturation for large d_k
- Two variants: **Bahdanau (additive)** vs **Luong (multiplicative)**

**See also:** [[202105270808 Attention]], [[202101171354 Softmax Activation Function]]

---
