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

![](./simply_supported/structure.svg)

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