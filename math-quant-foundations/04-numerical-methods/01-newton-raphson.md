# Question

Explain Newton-Raphson root finding and its application to implied volatility.

# Answer

**Newton-Raphson method:** Find root of $f(x) = 0$ iteratively:

$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$

**Intuition:** Approximate $f$ with tangent line, find where it crosses zero.

**Convergence:**
- **Quadratic** near root: errors square each iteration
- Requires good initial guess
- Fails if $f'(x_n) \approx 0$ or at inflection points

**Implied volatility application:**

Given market option price $C_{market}$, find $\sigma$ such that:

$f(\sigma) = C_{BS}(\sigma) - C_{market} = 0$

Newton step:
$\sigma_{n+1} = \sigma_n - \frac{C_{BS}(\sigma_n) - C_{market}}{\text{Vega}(\sigma_n)}$

where Vega $= \frac{\partial C}{\partial \sigma}$

**Why it works well for IV:**
- Black-Scholes is monotonic in $\sigma$
- Vega is always positive for vanilla options
- Smooth function, well-behaved derivatives

**Practical considerations:**
1. Initial guess: ATM vol or historical vol
2. Bounds checking: $\sigma > 0$
3. Convergence tolerance: typically $10^{-6}$
4. Max iterations: 20-50 usually sufficient

**Alternatives:** Bisection (slower but guaranteed), Brent's method, rational approximations (Jaeckel)
