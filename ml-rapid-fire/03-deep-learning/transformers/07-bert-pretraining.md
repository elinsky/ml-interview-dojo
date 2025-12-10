# BERT Pre-training

**Q:** How does BERT's pre-training work?

**A:**

- **Masked Language Model**: mask 15% of tokens, predict them
- **Next Sentence Prediction**: is sentence B the actual next?
- Bidirectional: sees context from both directions
- Three input embeddings: token + position + segment
- Pre-trained model = bigger is better, even on small fine-tune datasets

**See also:** [[202201231144 Summary - BERT]], [[202201260609 Summary - RoBERTa]]

---
