# CNN Architecture

**Q:** What is the typical CNN architecture pattern?

**A:**

- **Conv → ReLU → Pool** repeated multiple times
- Early layers: detect edges, textures (low-level features)
- Deeper layers: detect parts, objects (high-level features)
- End with **flatten → fully connected → softmax**
- Depth increases, spatial size decreases through network

---
