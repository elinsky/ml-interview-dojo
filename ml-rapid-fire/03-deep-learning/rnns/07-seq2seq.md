# Sequence-to-Sequence

**Q:** What is a sequence-to-sequence (seq2seq) model?

**A:**

- **Encoder**: processes input sequence → fixed-size context vector
- **Decoder**: generates output sequence from context
- Used for variable-length input → variable-length output
- Trick: feeding input **backwards** improves translation
- Bottleneck: fixed-size context vector limits performance

---
