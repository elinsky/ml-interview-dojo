# RMSprop

**Q:** How does RMSprop work?

**A:**

- Adapts learning rate **per parameter**
- Divides by running average of squared gradients
- Parameters with large gradients get smaller updates
- Helps with sparse gradients and non-stationary objectives
- Proposed by Hinton (unpublished, Coursera lecture)

---
