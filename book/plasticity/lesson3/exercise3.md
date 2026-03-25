# Guided exercise 3

Given is the following structure:

```{figure-start} ./exercise3_data/constructie.svg
:class: sticky-margin
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

::::{admonition} Worked-out solution
:class: solution, dropdown

```{figure} ./exercise3_data/constructie.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/plasticity_6
:number:
```

The structure has 4 unknown reactions forces and 3 equilibrium equations, which gives us a degree of statical indeterminacy of 1.

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

::::{admonition} Worked-out solution
:class: solution, dropdown

We'll apply the force method to find $C_{\rm{v}}$:

```{figure} ./exercise3_data/Cv.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/plasticity_6
:number:
```

Applying the forget-me-nots gives:

$$
\begin{align*}
w_C &= 0 \\
w-\cfrac{C_v \cdot 6^3}{3 \cdot EI} + \cfrac{F \cdot 3^3}{3 \cdot EI} + \cfrac{F \cdot 3^2}{2 \cdot EI} \cdot 3 + \cfrac{ \cfrac{5}{24} \cdot F \cdot 6 ^3 }{3 \cdot EI} + \cfrac{ \cfrac{5}{24} \cdot F \cdot 3 \cdot 6^2}{2\cdot EI} &= 0 \\
C_v &= \cfrac{65}{96} \cdot F
\end{align*}
$$

This allows us to calculate the bending moments at $\rm{A}$, $\rm{B}$ and $\rm{C}$:

```{figure} ./exercise3_data/M_A.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/plasticity_6
:number:
```

$$
\begin{align*}
\sum{{{\left. {\mathop{T}}\, \right|}_{\rm{A}}^\rm{AD}}}&=0\\
{{M}_{\rm{A}}}&= \cfrac{26}{32} \cdot F
\end{align*}
$$

```{figure} ./exercise3_data/M_B.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/plasticity_6
:number:
```

$$
\begin{align*}
\sum{{{\left. {\mathop{T}}\, \right|}_{\rm{B}}^\rm{BD}}}&=0\\
{{M}_{\rm{B}}}&= -\cfrac{25}{32}\cdot F
\end{align*}
$$

```{figure} ./exercise3_data/M_C.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/plasticity_6
:number:
```

$$
\begin{align*}
\sum{{{\left. {\mathop{T}}\, \right|}_{\rm{C}}^\rm{CD}}}&=0 \\
{{M}_{\rm{C}}}&= \cfrac{20}{32} \cdot F
\end{align*}
$$

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

::::{admonition} Worked-out solution
:class: solution, dropdown

$M_\rm{A}$ is the biggest, so the first moment to reach $M_{\rm{p}}$.

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

::::{admonition} Worked-out solution
:class: solution, dropdown

$$
\begin{align*}
741 &= \cfrac{26}{32}\, F \\
F_{y,1} &= 912 \cdot \rm{ kN}
\end{align*}
$$

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

::::{admonition} Worked-out solution
:class: solution, dropdown

Applying forget-me-nots gives:

$$w_B = -\cfrac{ \cfrac{65}{96} \cdot 912 \cdot 3^3}{3 \cdot 1215000} -\cfrac{ \cfrac{65}{96} \cdot 912 \cdot 3^2}{2 \cdot 1215000} + \cfrac{912 \cdot 3^3}{3 \cdot 121500} + \cfrac{ \cfrac{5}{24}\cdot 912 \cdot 3 ^3}{3 \cdot 121500} + \cfrac{ \cfrac{5}{24}\cdot 912 \cdot 6 \cdot 3^2}{2\cdot 121500} = 0.0095 \, \rm{ m}$$


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

::::{admonition} Worked-out solution
:class: solution, dropdown

The yielding cross-section is replaced by a plastic hinge, which leads to one less unknown. This means that the structure is now statically determinate.

```{figure} ./exercise3_data/yield_1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/plasticity_6
:number:
```

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

::::{admonition} Worked-out solution
:class: solution, dropdown

First $C_{\rm{v}}$ is calculated for the new structure:

```{figure} ./exercise3_data/Cv_2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/plasticity_6
:number:
```

$$
\begin{align*}
\sum{{{\left. {\mathop{T}}\, \right|}_{\rm{A}}}}&=0 \\
{{C}_{\rm{v}}}&= \cfrac{13}{16} \cdot F - \cfrac{247}{2}
\end{align*}
$$

Now, the bending moments at $\rm{A}$, $\rm{B}$ and $\rm{C}$:

```{figure} ./exercise3_data/M_B_2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/plasticity_6
:number:
```

$$
\begin{align*}
\sum{{{\left. {\mathop{T}}\, \right|}_{\rm{B}}^\rm{BD}}}&=0 \\
{{M}_{\rm{B}}}&= -\cfrac{741}{2}+\cfrac{38}{32}\cdot F
\end{align*}
$$


```{figure} ./exercise3_data/M_C.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/plasticity_6
:number:
```

Unchanged, so:

$$
{{M}_{\rm{C}}}= \cfrac{20}{32} \cdot F
$$

So $M_{\rm{B}}$ is the second moment to reach $M_{\rm{p}}$

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

::::{admonition} Worked-out solution
:class: solution, dropdown

$$
\begin{align*}
741 &= -\cfrac{741}{2}+\cfrac{38}{32}\cdot F \\
F_{y,2} &= 936 \, \rm{ kN}
\end{align*}
$$

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

::::{admonition} Worked-out solution
:class: solution, dropdown


Applying forget-me-knots gives:

$$w_B = -\cfrac{741 \cdot 6 ^2}{16 \cdot 121500} + \cfrac{96 \cdot 6 ^3}{48 \cdot EI} - \cfrac{ \cfrac{5}{24} \cdot 936 \cdot 3 \cdot 6 ^2}{16 \cdot 121500} = \cfrac{91}{9000} \approx 0.01011 \, \rm{ m}$$
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

