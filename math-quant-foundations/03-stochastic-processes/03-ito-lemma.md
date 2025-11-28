# Question

State Ito's lemma and explain why the extra term appears.

# Answer

**Ito's Lemma:** For $dX_t = \mu_t \, dt + \sigma_t \, dW_t$ and smooth function $f(t, x)$:

$df(t, X_t) = \frac{\partial f}{\partial t} dt + \frac{\partial f}{\partial x} dX_t + \frac{1}{2}\frac{\partial^2 f}{\partial x^2} (dX_t)^2$

Using $(dW_t)^2 = dt$, $dt \cdot dW_t = 0$, $(dt)^2 = 0$:

$df = \left(\frac{\partial f}{\partial t} + \mu_t \frac{\partial f}{\partial x} + \frac{1}{2}\sigma_t^2 \frac{\partial f}{\partial x^2}\right) dt + \sigma_t \frac{\partial f}{\partial x} dW_t$

**Why the extra $\frac{1}{2}\sigma^2 f''$ term?**

In ordinary calculus: $(dx)^2 \to 0$ as $dx \to 0$

In stochastic calculus: $(dW)^2 = dt \neq 0$ (quadratic variation of BM)

The second-order term survives because Brownian motion is "rougher" than smooth paths.

**Classic application - deriving GBM solution:**

Let $f(S) = \log S$, then $f' = 1/S$, $f'' = -1/S^2$

$d(\log S) = \frac{1}{S}dS - \frac{1}{2}\frac{1}{S^2}\sigma^2 S^2 dt = (\mu - \frac{\sigma^2}{2})dt + \sigma dW$

Integrate: $\log S_T - \log S_0 = (\mu - \frac{\sigma^2}{2})T + \sigma W_T$

**Finance applications:**
- Deriving Black-Scholes PDE
- Finding dynamics of portfolio value
- Change of numeraire calculations
