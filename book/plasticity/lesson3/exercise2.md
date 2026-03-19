# Guided exercise 2

Given is the following cross-section:

```{figure-start} ./exercise2_data/constructie.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/plasticity_4
:number:
```

$$
\begin{align*}
EI &= 50 \, \rm{MNm^2} \\
M_{\rm{p}} &= 300 \, \rm{kNm} \\
\alpha &= 1 \\
\end{align*}
$$

Horizontal plastic regime

```{figure-end}
```

For which we're interested in the $q-w_{\rm{C}}$ curve.

::::{hint-start}
::::
You can make use of the following forget-me-nots:

:::::{grid} 2
:class-container: center-grid

::::{grid-item}
:columns: auto

```{figure-start} ./exercise2_data/FBD_q.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/vergeet-me-nietjes
:number:
```

$$
\begin{align*}
\varphi _{\rm{A}} = \varphi _{\rm{B}} &= \cfrac{1}{24}\cfrac{q \, L^3}{EI} \\ 
w_{\rm{C}} &= \cfrac{5}{384}\cfrac{q \, L^4}{EI} \\
\end{align*}
$$

```{figure-end}
```

::::

::::{grid-item}
:columns: auto

```{figure-start} ./exercise2_data/FBD_T.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/vergeet-me-nietjes
:number:
```

$$
\begin{align*}
\varphi _{\rm{A}} &= \cfrac{1}{6}\cfrac{T \, L}{EI} \\
\varphi _{\rm{B}} &= \cfrac{1}{3}\cfrac{T \, L}{EI} \\
w_{\rm{C}} &= \cfrac{1}{16}\cfrac{T \, L^2}{EI} \\
\end{align*}
$$

```{figure-end}
```

:::::

::::{hint-end}
::::

::::{question} Opgave
:type: short-answer
:variant: blocks
:admonition:
:class: exercise
:nocaption:
:showanswer:

What is the degree of statical indeterminacy of this structure if you only consider the bending behaviour?
---
M[2]
---

::::

::::{question} Opgave
:type: short-answer
:variant: blocks
:admonition:
:class: exercise
:nocaption:
:showanswer:

What are the bending moments at $\rm{A}$, $\rm{B}$ and $\rm{C}$ in $\rm{kNm}$ expressed as a multiple of $q \left[\rm{kN/m}\right]$? Assume ◡ is a positive bending moment
---
MRP[-4/3;0.025] The bending moment at $\rm{A}$
MRP[2/3;0.025] The bending moment at $\rm{B}$
MRP[-4/3;0.025] The bending moment at $\rm{C}$
---

::::

::::{question} Opgave
:variant: multiple-select
:admonition:
:class: exercise
:columns: 1 3 3 3
:nocaption:
:showanswer:

Which point/points will yield first?
---
[x] Point $\rm{A}$
[ ] Point $\rm{B}$
[x] Point $\rm{C}$
---

::::

::::{question} Opgave
:type: short-answer
:variant: blocks
:admonition:
:class: exercise
:nocaption:
:showanswer:

What is the load $q$ in $\rm{kN/m}$ at which the first point(s) yield(s)?
---
M[225]
---

::::

::::{question} Opgave
:type: short-answer
:variant: blocks
:admonition:
:class: exercise
:nocaption:
:showanswer:

What is the displacement $w_{\rm{C}}$ in $\rm{mm}$ at which the first point(s) yield(s)?
---
M[3]
---

::::

::::{question} Opgave
:type: short-answer
:variant: blocks
:admonition:
:class: exercise
:nocaption:
:showanswer:

What is the degree of statical indeterminacy of this structure now that the first point(s) is/are yielding if you only consider the bending behaviour?
---
M[0]
---

::::

::::{question} Opgave
:variant: multiple-select
:admonition:
:class: exercise
:columns: 1 3 3 3
:nocaption:
:showanswer:

Which point/points will yield next?
---
[ ] Point $\rm{A}$
[x] Point $\rm{B}$
[ ] Point $\rm{C}$
---

::::


::::{question} Opgave
:type: short-answer
:variant: blocks
:admonition:
:class: exercise
:nocaption:
:showanswer:

What is the load $q$ in $\rm{kN/m}$ at which the next the point(s) yield(s)?
---
M[300]
---

::::

::::{question} Opgave
:type: short-answer
:variant: blocks
:admonition:
:class: exercise
:nocaption:
:showanswer:

What is the displacement $w_{\rm{C}}$ in $\rm{mm}$ at which the next point(s) yield(s)?
---
M[8]
---

::::

:::::{exercise}
:nonumber: true

Draw the $q-w_{\rm{C}}$ curve for this structure.

:::::

::::{admonition} Solution
:class: solution, dropdown

```{figure} ./exercise2_data/q-w.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/plasticity_4
:number:
```

::::