# Transfer Learning in CNNs

**Q:** How is transfer learning used with CNNs?

**A:**

- Use pretrained model (ImageNet) as starting point
- **Feature extraction**: freeze conv layers, train new classifier
- **Fine-tuning**: unfreeze top 1-3 layers, train with very low LR
- Works because early layers learn generic features (edges, textures)
- Especially useful with limited training data

---
