# Question

Explain delta hedging. Why doesn't it eliminate all risk?

# Answer

**Delta hedging:** Hold $\Delta = \frac{\partial V}{\partial S}$ shares opposite to option position.

**For short call:** Hold $+\Delta$ shares
**For short put:** Hold $-|\Delta|$ shares (i.e., short shares)

**Mechanics:**
1. Sell option, receive premium
2. Buy $\Delta$ shares to hedge
3. As $S$ moves, $\Delta$ changes
4. Rebalance to maintain delta-neutrality

**P&L from delta-hedged position:**

Over small time $dt$, P&L ≈ $\frac{1}{2}\Gamma S^2 (dS/S)^2 - \Theta \, dt$

Or: $\text{P&L} \approx \frac{1}{2}\Gamma S^2 (\sigma_{realized}^2 - \sigma_{implied}^2) dt$

**Why delta hedging doesn't eliminate all risk:**

1. **Gamma risk:** Large moves make delta stale between rebalances
2. **Discrete hedging:** Can't trade continuously
3. **Transaction costs:** Each rebalance costs money
4. **Volatility risk:** Implied vol changes (vega exposure)
5. **Model risk:** True delta may differ from model delta
6. **Jump risk:** Discontinuous moves bypass hedging

**Hedging frequency tradeoff:**
- More frequent → less gamma slippage
- More frequent → higher transaction costs

**Practical insight:** Delta hedging converts directional risk into volatility risk. You're now betting on realized vs. implied volatility.
