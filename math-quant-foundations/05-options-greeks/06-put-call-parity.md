# Question

State put-call parity and explain its arbitrage implications.

# Answer

**Put-Call Parity (European options, no dividends):**

$C - P = S_0 - K e^{-rT}$

Or equivalently: $C + K e^{-rT} = P + S_0$

**Intuition:** Two portfolios with identical payoffs at expiration must have same price today.

**Portfolio 1:** Long call + cash $Ke^{-rT}$
**Portfolio 2:** Long put + stock $S_0$

Both worth $\max(S_T, K)$ at expiration.

**With continuous dividend yield $q$:**
$C - P = S_0 e^{-qT} - K e^{-rT}$

**Arbitrage if violated:**

If $C - P > S_0 - Ke^{-rT}$: Sell call, buy put, buy stock, borrow $Ke^{-rT}$

If $C - P < S_0 - Ke^{-rT}$: Buy call, sell put, short stock, lend $Ke^{-rT}$

**Applications:**

1. **Synthetic positions:**
   - Synthetic long stock: Long call + short put
   - Synthetic call: Long put + long stock
   
2. **Implied forward price:** $F = (C - P)e^{rT} + K$

3. **Consistency check:** Market prices should satisfy parity

4. **Implied borrow rate:** Solve for $r$ from parity

**Note:** Only holds for European options. American options have more complex relationships due to early exercise.
