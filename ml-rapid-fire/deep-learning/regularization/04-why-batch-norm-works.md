# Why Batch Norm Works

**Q:** Why does batch normalization help training?

**A:**

- Reduces **internal covariate shift** (original claim, debated)
- Smooths loss landscape, enabling higher learning rates
- Has mild regularization effect (noise from batch statistics)
- Allows less careful weight initialization
- Consider removing dropout when using batch norm

---
