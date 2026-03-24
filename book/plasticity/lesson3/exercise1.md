# Guided exercise 1

Given is the following cross-section:

```{figure-start} ./exercise1_data/cirkel.svg
:class: sticky-margin
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/plasticity_5
:number:
```

$$
\begin{align*}
A &= \pi \, R^2 \\
I_{zz} &= \cfrac{\pi \, R^4}{4}
\end{align*}
$$

```{figure-end}
```

For which we're interested in the shape factor.

::::{hint-start}
::::
You can make use of the following additional formulas:

```{figure-start} ./exercise1_data/halvecirkel.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/plasticity_5
:number:
```

$$
\begin{align*}
A_{\rm{half}} &= \cfrac{\pi \, R^2}{2} \\
z_{\rm{N.C.}} &= \cfrac{4 \, R}{3 \, \pi}
\end{align*}
$$




```{figure-end}
```

::::{hint-end}
::::

::::{question} Opgave
:type: short-answer
:variant: blocks
:admonition:
:class: exercise
:nocaption:
:showanswer:

What is the plastic moment capacity in $\rm{Nm}$, expressed as a multiple of $R^3 \left[\rm{m^3}\right]$ and $f_y \left[\rm{Pa}\right]$?
---
MRP[4/3;0.025]
---

::::

::::{question} Opgave
:type: short-answer
:variant: blocks
:admonition:
:class: exercise
:nocaption:
:showanswer:

What is the elastic moment capacity in $\rm{Nm}$, expressed as a multiple of $R^3 \left[\rm{m^3}\right]$ and $f_y \left[\rm{Pa}\right]$? Submit your answer as decimal number.
---
MRP[0.785398;0.025]
---

::::

::::{question} Opgave
:type: short-answer
:variant: blocks
:admonition:
:class: exercise
:nocaption:
:showanswer:

What is the shape factor? Submit your answer as decimal number.
---
MRP[1.697653;0.025]
---

::::
