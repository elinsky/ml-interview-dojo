# Question

Derive the key intuition behind Black-Scholes. What assumptions does it make?

# Answer

**Black-Scholes call option formula:**

$C = S_0 N(d_1) - K e^{-rT} N(d_2)$

where:
- $d_1 = \frac{\ln(S_0/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}}$
- $d_2 = d_1 - \sigma\sqrt{T}$
- $N(\cdot)$ = standard normal CDF

**Intuition breakdown:**

- $N(d_2)$ = Risk-neutral probability option expires ITM
- $S_0 N(d_1)$ = Expected stock value if exercised (adjusted)
- $K e^{-rT} N(d_2)$ = PV of strike payment if exercised

**Key assumptions:**

1. **GBM for stock:** $dS = \mu S dt + \sigma S dW$
2. **Constant volatility** $\sigma$
3. **Constant risk-free rate** $r$
4. **No dividends** (or continuous dividend yield $q$)
5. **No transaction costs or taxes**
6. **Continuous trading** possible
7. **No arbitrage**

**Derivation approaches:**

1. **PDE approach:** Delta-hedge eliminates risk → risk-free return
   $\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} = rV$

2. **Risk-neutral pricing:** $C = e^{-rT} E^{\mathbb{Q}}[(S_T - K)^+]$

**What fails in practice:**
- Vol is not constant (smile/skew)
- Jumps in prices
- Discrete hedging creates slippage
