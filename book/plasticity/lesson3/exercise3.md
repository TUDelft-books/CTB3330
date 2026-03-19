# Guided exercise 3

Given is the following structure:

```{figure-start} ./exercise3_data/constructie.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/plasticity_6
:number:
```

$$
\begin{align*}
EI &= 121.5 \, \rm{MNm^2} \\
M_{\rm{p}} &= 741 \, \rm{kNm} \\
\alpha &= 1 \\
\end{align*}
$$

Horizontal plastic regime

```{figure-end}
```

::::{hint-start}
::::
You can make use of the following forget-me-nots:

:::::{grid} 2
:class-container: center-grid

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
::::

::::{grid-item}
:columns: auto

```{figure-start} ./exercise3_data/VMN_F2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/vergeet-me-nietjes
:number:
```

$$
\begin{align*}
\varphi _{\rm{A}} = \varphi _{\rm{B}} &= \cfrac{1}{16}\cfrac{F \, L^2}{EI} \\
w_{\rm{C}} &= \cfrac{1}{48}\cfrac{F \, L^3}{EI} \\
\end{align*}
$$

```{figure-end}
```

::::

::::{grid-item}
:columns: auto

```{figure-start} ./exercise3_data/VMN_F.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/vergeet-me-nietjes
:number:
```

$$
\begin{align*}
\varphi_{\rm{B}} &= \cfrac{1}{2}\cfrac{F \, L^2}{EI} \\
w_{\rm{C}} &= \cfrac{1}{3}\cfrac{F \, L^3}{EI}
\end{align*}
$$

```{figure-end}
```

::::

::::{grid-item}
:columns: auto

```{figure-start} ./exercise3_data/VMN_T.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/vergeet-me-nietjes
:number:
```

$$
\begin{align*}
\varphi_{\rm{B}} &= \cfrac{T \, L}{EI} \\
w_{\rm{C}} &= \cfrac{1}{2}\cfrac{T \, L^2}{EI}
\end{align*}
$$


```{figure-end}
```

::::

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

What is the degree of statical indeterminacy of this structure?
---
M[1]
---

::::

::::{question} Opgave
:type: short-answer
:variant: blocks
:admonition:
:class: exercise
:nocaption:
:showanswer:

What are the bending moments at $\rm{A}$, $\rm{B}$ and $\rm{C}$ in $\rm{kNm}$ expressed as a multiple of $F \left[\rm{kN}\right]$? Assume ◡ is a positive bending moment
---
MRP[-26/32;0.025] The bending moment at $\rm{A}$
MRP[25/32;0.025] The bending moment at $\rm{B}$
MRP[-20/32;0.025] The bending moment at $\rm{C}$
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

What is the load $F$ in $\rm{kN}$ at which the first point(s) yield(s)?
---
M[912]
---

::::

::::{question} Opgave
:type: short-answer
:variant: blocks
:admonition:
:class: exercise
:nocaption:
:showanswer:

What is the displacement $w_{\rm{B}}$ in $\rm{mm}$ at which the first point(s) yield(s)?
---
M[9.5]
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

Which point/points will yield first?
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

What is the load $F$ in $\rm{kN}$ at which the next the point(s) yield(s)?
---
M[936]
---

::::

::::{question} Opgave
:type: short-answer
:variant: blocks
:admonition:
:class: exercise
:nocaption:
:showanswer:

What is the displacement $w_{\rm{B}}$ in $\rm{mm}$ at which the next point(s) yield(s)?
---
MRP[91/9;0.025]
---

::::

:::::{exercise}
:nonumber: true

Draw the $F-w_{\rm{B}}$ curve for this structure.

:::::

::::{admonition} Solution
:class: solution, dropdown

```{figure} ./exercise3_data/F-w.svg
:align: center
:source: https://github.com/TUDelft-books/CTB3330/tree/2025/book/plasticity/lesson3/exercise3_data
:number:
```

::::

% https://ans.app/repo_questions/32289101/criteria