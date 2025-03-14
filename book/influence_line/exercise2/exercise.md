# MOLA exercise

In this exercise, you're going to find influence lines using MOLA. 

## Components
We'll use the following components:
| MOLA    | Model |
| :--------: | :------: |
| ![](./parts/fix.webp)  | ![](./parts/fixed.svg)|
| ![](./parts/hinged_support.webp)| ![](./parts/hinged_support.svg)  |
| ![](./parts/sliding_support.webp)| ![](./parts/sliding_support.svg)  |
| ![](./parts/sliding_hinged_support.webp) | ![](./parts/sliding_hinged_support.svg)|
| ![](./parts/beam.webp) | ![](parts/beam.svg)|
| ![](./parts/stiff.webp) | ![](parts/stiff.svg) |
| ![](./parts/1rad.webp) | ![](parts/1rad.svg) |

## Simply supported beam
Let's start with the most basic model, a simply supported beam:

```{figure} ./simply_supported/structure.svg
:width: 200%
:name: simply_supported
:align: center
Simply supported beam
```

```{exercise} Simply supported beam
:label: ss
:nonumber: true

Make the simply supported beam with MOLA
```

```{solution} ss
:class: dropdown

![](./simply_supported/structure.webp)

```

```{exercise} Influence line vertical support reaction at A for simply supported beam
:label: ss_A
:nonumber: true

Show the influence line of the vertical support reaction at A
```

```{solution} ss_A
:class: dropdown

![](./simply_supported/inf_A.webp)

```

```{exercise} Influence line vertical support reaction at B for simply supported beam
:label: ss_B
:nonumber: true

Show the influence line of the vertical support reaction at B
```

```{solution} ss_B
:class: dropdown

![](./simply_supported/inf_B.webp)

```

```{exercise} Influence line bending moment for simply supported beam
:label: ss_M
:nonumber: true

Show the influence line for the bending moment halfway the beam
```

```{solution} ss_M
:class: dropdown

![](./simply_supported/inf_M.webp)

```

```{exercise} Influence line displacement for simply supported beam
:label: ss_w
:nonumber: true

Show the influence line for the displacement halfway the beam
```

```{solution} ss_w
:class: dropdown

![](./simply_supported/inf_w.webp)

```

```{exercise} Influence line rotation for simply supported beam
:label: ss_phi
:nonumber: true

Show the influence line for the rotation halfway the beam
```

```{solution} ss_phi
:class: dropdown

![](./simply_supported/inf_phi.webp)

```