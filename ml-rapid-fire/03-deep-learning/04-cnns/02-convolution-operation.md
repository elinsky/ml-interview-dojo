# Convolution Operation

**Q:** What is the convolution operation in CNNs?

**A:**

- Slide a **filter/kernel** across input, compute dot products
- Output is a **feature map** (activation map)
- Detects local patterns (edges, textures, shapes)
- Same filter applied everywhere = **translation invariance**
- Output size: (W - F + 2P) / S + 1

---
