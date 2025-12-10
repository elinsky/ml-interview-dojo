# LSTM Gates

**Q:** What do the three LSTM gates do?

**A:**

- **Forget gate**: decides what to remove from cell state
- **Input gate**: decides what new info to add to cell state
- **Output gate**: decides what to output based on cell state
- All gates use sigmoid (0-1) to control flow
- Allows gradients to flow unchanged through cell state

---
