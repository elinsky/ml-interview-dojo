# Teacher Forcing

**Q:** What is teacher forcing in RNN training?

**A:**

- During training: feed **ground truth** as next input (not prediction)
- Speeds up training, improves convergence
- Risk: exposure bias (train/test mismatch)
- Model never learns to recover from its own mistakes
- Mitigation: scheduled sampling (gradually use predictions)

---
