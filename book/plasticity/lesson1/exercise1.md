# Guided exercise 1

Given is the following structure:

```{figure-start} ./exercise1_data/constructie.svg
:sticky-margin:
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/plasticity
:number:
```

$$
\begin{align*}
E &= 200 \, \rm{GPa}\\
A &= 100 \, \rm{mm^2} \\
EI_{zz} &\gg EA \\
f_{y} &= 275 \, \rm{MPa} \\
\rm{horizontal} &\, \rm{plastic} \, \rm{regime}
\end{align*}
$$

```{figure-end}
```

For which we're interested in the vertical displacement $w$ as a function of the applied load $F$.

:::::{exercise}
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292845781909485337/embed
```

:::::

We're going to solve this structure using the displacement method with two degrees of freedom: the vertical displacement of $\rm{A}$ and $\rm{C}$.

```{figure} ./exercise1_data/dof.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/plasticity
:number:
```

:::::{exercise}
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292845813302464487/embed
```

:::::

:::::{exercise}
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292847618700830827/embed
```

:::::

:::::{exercise}
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292845823731398307/embed
```

:::::

:::::{exercise}
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292846901050335887/embed
```

:::::

:::::{exercise}
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292847525652666537/embed
```

:::::

:::::{exercise}
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292847514948165647/embed
```

:::::

:::::{exercise}
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292847523345425137/embed
```

:::::

:::::{exercise}
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292847528589890207/embed
```

:::::

Now that we're entering the elasto-plastic regime. As we don't know which element will yield next, we need to solve the system of equations again. Therefore we assume the forces from the elastic regime as given, and we solve for additional forces:

```{figure} ./exercise1_data/FBD.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/plasticity
:number:
```

:::::{exercise}
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292847530629884917/embed
```

:::::

:::::{exercise}
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292847536325456177/embed
```

:::::

:::::{exercise}
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292847674996551927/embed
```

:::::

:::::{exercise}
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292847675827914207/embed
```

:::::

:::::{exercise}
:nonumber: true

Draw the $F-w$ curve for this structure and indicate which parts are yielding in which regime.

:::::

::::{admonition} Solution
:class: solution, dropdown

```{figure} ./exercise1_data/FW.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/plasticity
:number:
```

::::