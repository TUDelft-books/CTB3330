# Guided exercise 2

Given is the following structure:

```{figure-start} ./exercise2_data/structure.svg
:class: sticky-margin
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/plasticity_2
:number:
```

$$
\begin{align*}
E &= 200 \, \rm{GPa}\\
A &= 100 \, \rm{mm^2} \\
EI_{zz} &\gg EA \\
f_{y} &= 500 \, \rm{MPa} \\
\end{align*}
$$

Horizontal plastic regime

```{figure-end}
```

For which we're interested in the vertical displacement $w$ as a function of the applied load $F$.

:::{question} Exercise
:admonition:
:columns: 1 3 3 3
:class: exercise
:nocaption:
:showanswer:

Which cable will yield first?
---
[x] Cable $\rm{BE}$
[ ] Cable $\rm{EG}$
[ ] Cable $\rm{CH}$
---
:::

:::{question} Exercise
:admonition:
:columns: 1 3 3 3
:class: exercise
:nocaption:
:variant: multiple-select
:showanswer:

Which cables will yield when the structure collapses?
---
[x] Cable $\rm{BE}$
[ ] Cable $\rm{EG}$
[x] Cable $\rm{CH}$
---
:::

::::{question} Opgave
:type: short-answer
:variant: blocks
:admonition:
:class: exercise
:nocaption:
:showanswer:

What are the values for the final $F-w$ curve?

```{figure} ./exercise2_data/FW.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/plasticity_2
:number:
```

---
M[40] What is the value of $w_1$ in $\rm{mm}$?
M[50] What is the value of $w_2$ in $\rm{mm}$?
M[5125] What is the value of $F_1$ in $\rm{N}$?
M[5625] What is the value of $F_2$ in $\rm{N}$?
---

::::

::::{admonition} Worked-out solution
:class: solution, dropdown

$$
\begin{align*}
N_{y,\rm{CH}} &= A_\rm{CH} \cdot f_y = 5000 \, \rm{N} \\
N_{y,\rm{EG}} &= A_\rm{EG} \cdot f_y = 10000 \, \rm{N} \\
N_{y,\rm{BE}} &= A_\rm{BE} \cdot f_y = 5000 \, \rm{N}
\end{align*}
$$

The force in $\rm{BE}$ and $\rm{EG}$ is the same, so $\rm{BE}$ or $\rm{CH}$ will be the first elements to yield.

$$
\begin{align*}
w_{\rm{C},\rm{yield}\,\rm{in}\, \rm{CH}} &= \cfrac{f_y}{E} \cdot 10 = 0.025 \, \rm{m} \\
w_{\rm{S},\rm{yield}\,\rm{in}\, \rm{CH}} &= w_{\rm{C},\rm{yield}\,\rm{in}\, \rm{CH}} \cdot 2 = 0.05 \, \rm{m} \\
w_{\rm{B},\rm{yield}\,\rm{in}\, \rm{BE}} &= \cfrac{f_y}{E} \cdot 8 + \cfrac{f_y \cdot A_\rm{BE}}{E \cdot A_\rm{EG}} \cdot 4 = 0.025 \, \rm{m} \\
w_{\rm{S},\rm{yield}\,\rm{in}\, \rm{BE}} &= w_{\rm{B},\rm{yield}\,\rm{in}\, \rm{BE}} \cdot \cfrac{8}{5} = 0.04 \, \rm{m}
\end{align*}
$$

So, first $\rm{BE}$ will yield starting at a displacement of $40 \, \rm{mm}$ at $\rm{S}$. Afterwards, $\rm{CH}$ will yield starting at a displacement of $50 \, \rm{mm}$ at $\rm{S}$.
In case of starting yield in $\rm{BE}$:

```{figure} ./exercise2_data/FBD_AS_1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/plasticity_2
:number:
```

$$\sum{{{\left. {\mathop{T}}\, \right|}_{\rm{S}}^\rm{AS}}}=0\to {{A}_{\rm{v}}}=-1875\, \rm{N}$$

$$
\begin{align*}
w_{\rm{C},\rm{yield}\,\rm{in}\, \rm{BE}} &= \cfrac{w_{\rm{S},\rm{yield}\,\rm{in}\, \rm{BE}}}{2} = 0.02 \, \rm{m} \\
N_{\rm{CH},\rm{yield}\,\rm{in}\, \rm{BE}} &= \cfrac{w_{\rm{C},\rm{yield}\,\rm{in}\, \rm{BE}}}{10} \cdot E \cdot A_\rm{CH} = 4000 \, \rm{N}
\end{align*}
$$

```{figure} ./exercise2_data/FBD_SD_1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/plasticity_2
:number:
```

$$\sum{{{\left. {\mathop{T}}\, \right|}_{\rm{S}}^\rm{SD}}}=0\to {{A}_{\rm{v}}}=-2000\, \rm{N}$$

```{figure} ./exercise2_data/FBD_balk_1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/plasticity_2
:number:
```

$${{\sum{{\mathop{F}}\,}}_{v}}=0\to F=5125\, \rm{N}$$


In case of starting yield in both $\rm{BE}$ and $\rm{CH}$:

$${A}_{\rm{v}}=-1875\, \rm{N}$$

```{figure} ./exercise2_data/FBD_SD_2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/plasticity_2
:number:
```

$$\sum{{{\left. {\mathop{T}}\, \right|}_{\rm{S}}^\rm{SD}}}=0\to {{A}_{\rm{v}}}=-2500\, \rm{N}$$

```{figure} ./exercise2_data/FBD_balk_2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/plasticity_2
:number:
```

$${{\sum{{\mathop{F}}\,}}_{v}}=0\to F=5625\, \rm{N}$$

This gives:

```{figure} ./exercise2_data/FW.png
:align: center
:number:
```

::::