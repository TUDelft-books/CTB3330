# Guided exercise 2

Given is the following structure:

```{figure-start} ./exercise2_data/constructie.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/plasticity_2
:number:
```

$$
\begin{align*}
A &= 100 \, \rm{mm^2} \\
EI_{zz} &\gg EA \\
f_{y} &= 500 \, \rm{MPa} \\
\end{align*}
$$

Horizontal plastic regime

```{figure-end}
```

Which is the same one as covered in the [previous lesson](../lesson1/exercise2.md).

Now, we're interested in the collapse load.

::::{question} Opgave
:type: short-answer
:variant: blocks
:admonition:
:class: exercise
:nocaption:
:showanswer:

What is the degree of staticaly indeterminacy of this structure?
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

How many telescope hinges are required to make this structure a mechanism?
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

How many potential locations are there for telescope hinges to be placed such that the structure becomes a mechanism?
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

How many different collapse mechanisms are there for this structure?
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

What is the collapse load in $\rm{N}$?
---
M[8750] For the mechanism with the highest collapse load?
M[5625] For the mechanism with the smallest collapse load?
---

::::

% solution_start

::::{admonition} Solution
:class: solution, dropdown

```{figure} ./exercise2_data/mechanism1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/plasticity_2
:number:
```

This collapse mechanism has a collapse load of $8750 \, \rm{N}$.

```{figure} ./exercise2_data/mechanism2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/plasticity_2
:number:
```

This collapse mechanism has a collapse load of $5625 \, \rm{N}$.

::::

% solution_end