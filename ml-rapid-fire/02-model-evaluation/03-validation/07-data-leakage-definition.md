# Data Leakage

**Q:** What is data leakage?

**A:**
- Information that wouldn't be available at inference time leaks into training
- Target leakage: future info in features (e.g., full OHLC bar at start of minute)
- Preprocessing leakage: fitting scaler on full data before split (test stats leak into training)

---
