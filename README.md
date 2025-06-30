# File `1 Calculating the previous approximation ratios.py`. 

We use $\epsilon$ to denote a small positive constant.

Given $\epsilon$, the function `f(epsilon)` corresponds to the function $f$ described in [1]. Specifically, we define:

$$
f(\epsilon)=\min_{\substack{0<\theta\leq1-\tau, \\ 0<\tau,\rho\leq 1/6}} \\{\frac{1+\zeta}{\theta}+\frac{1-\tau-\theta}{\theta\cdot(1-\tau)}+\frac{3\epsilon}{1-\theta}+\frac{3\rho}{(1-\rho)\cdot(1-\tau)}\\}-1,
$$

where in [1], $\theta$ was set to $1 - \tau$, but we obtain slightly better results by setting:

$$
\theta=\min\\{\frac{1}{\sqrt{\frac{3\varepsilon}{2+\zeta}}+1}, 1-\tau\\},
$$

and

$$
\zeta=\frac{3\rho+\tau-4\tau\cdot\rho}{1-\rho}+\frac{\epsilon}{\tau\cdot\rho}\cdot(1-\tau\cdot\rho-\frac{3\rho+\tau-4\tau\cdot\rho}{1-\rho}).
$$

Since $f$ is defined via an optimization, we compute its value using a grid-based brute-force search, which may introduce a small numerical error.

The file includes two cases: `splittable` and `unsplittable`.

For the `splittable` case, we aim to find the optimal value $\epsilon^\*$ such that:

$$
\epsilon^* = \arg\min_{\epsilon > 0} \max\\{ \alpha+1 - 2\epsilon, 2 + f(\epsilon) \\}.
$$

By default, the file sets $\epsilon = 1.005/3000 - 0.000000005$. The output is `epsilon should be smaller`, implying that $\epsilon^\* < 1.005/3000 - 0.000000005$.

However, note that $\epsilon^\*$ is very close to $1.005/3000$, since setting $\epsilon = 1.005/3000 - 0.000000006$ yields `epsilon can be bigger`, indicating $\epsilon^\* > 1.005/3000 - 0.000000006$.

The `unsplittable` case follows a similar pattern.

[1] J. Blauth, V. Traub, J. Vygen, *Improving the approximation ratio for capacitated vehicle routing*, *Mathematical Programming*, 197(2) (2023) 451–497.

# File `2 Approximation ratio tables.py`. 

We compute and present known approximation ratios in tabular form (see the image below):

<p align="center">
  <img src="https://github.com/user-attachments/assets/984cead9-1057-45b8-a1f5-28f0a47d3124" alt="Approximation Ratio Table">
</p>
