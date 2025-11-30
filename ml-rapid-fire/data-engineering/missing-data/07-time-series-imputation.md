# Time Series Imputation

**Q:** How is imputing missing values in time series different from cross-sectional data?
- Key difference
- Methods
- Considerations

**A:**

- **Key difference**: temporal order matters — can only use past values for realistic imputation (avoid lookahead bias)
- **Methods**:
  - **Forward fill (LOCF)**: carry last observation forward
  - **Backward fill**: carry next observation back (only for analysis, not prediction)
  - **Linear interpolation**: draw line between known points
  - **Rolling mean**: use rolling window average
  - **Seasonal adjustment**: use same period from previous cycle
- **Finance considerations**:
  - Forward fill common for prices (last known price)
  - Be careful: long gaps shouldn't be forward-filled indefinitely
  - Missing data at market close vs trading halt have different meanings
- **Pandas**: `df.fillna(method='ffill')`, `df.interpolate()`

---
