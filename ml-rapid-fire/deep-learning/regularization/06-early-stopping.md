# Early Stopping

**Q:** How does early stopping work?

**A:**

- Monitor **validation loss** during training
- Stop when validation loss stops improving
- Use **patience**: wait N epochs before stopping
- Save best model checkpoint, restore at end
- Simple, effective, no hyperparameter in loss function

---
