# Dropout

**Q:** How does dropout work?

**A:**

- Randomly **"drops"** neurons during training (set to 0)
- Each neuron dropped with probability p (typically 0.2-0.5)
- Forces network to learn redundant representations
- At inference: use all neurons, scale outputs by (1-p)
- Effectively trains ensemble of sub-networks

---
