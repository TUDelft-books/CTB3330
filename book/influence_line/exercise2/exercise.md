# Workshop virtuele arbeid

In deze workshop ga je de mechanismes die nodig zijn om virtuele arbeid toe te passen. Dat ga je doen met MOLA.

## Onderdelen
We maken gebruik van de volgende componenten
| MOLA    | Model |
| :--------: | :------: |
| ![](./parts/fix.webp)  | ![](./parts/fixed.svg)|
| ![](./parts/hinged_support.webp)| ![](./parts/hinged_support.svg)  |
| ![](./parts/sliding_support.webp)| ![](./parts/sliding_support.svg)  |
| ![](./parts/sliding_hinged_support.webp) | ![](./parts/sliding_hinged_support.svg)|
| ![](./parts/beam.webp) | ![](parts/beam.svg)|
| ![](./parts/hinge.webp) | ![](parts/hinge.svg)|

## Ligger op twee steunpunten
Laten we beginnen met een heel simpel model

```{figure} ./simply_supported/structure.svg
:width: 80%
:name: simply_supported
:align: center
Ligger op twee steunpunten
```

```{exercise} Ligger op twee steunpunten
:label: ss
:nonumber: true

Maak de ligger op twee steunpunten met MOLA
```

````{solution} ss
:class: dropdown

```{figure} ./simply_supported/structure.webp
:align: center
```

````

```{exercise} Linker verticale oplegging
:label: ss_A
:nonumber: true

Toon het mechanisme waarmee de oplegreactie in de linker verticale oplegging bepaald kan worden
```

````{solution} ss_A
:class: dropdown

```{figure} ./simply_supported/Oefening1_verticalereactielinks.webp
:align: center
```

```{exercise} Linker horizontale oplegging
:label: ss_Ah
:nonumber: true

Toon het mechanisme waarmee de oplegreactie in de linker horizontale oplegging bepaald kan worden
```

````{solution} ss_Ah
:class: dropdown

```{figure} ./simply_supported/Oefening1_horizontalereactielinks.webp
:align: center
```

```{exercise} Rechter verticale oplegging
:label: ss_B
:nonumber: true

Toon het mechanisme waarmee de oplegreactie in de rechter verticale oplegging bepaald kan worden
```

````{solution} ss_B
:class: dropdown

```{figure} ./simply_supported/Oefening1_verticalereactierechts.webp
:align: center
```

```{exercise} Moment
:label: ss_M
:nonumber: true

Toon het mechanisme het moment halverwege de balk bepaald kan worden
```

````{solution} ss_M
:class: dropdown

```{figure} ./simply_supported/Oefening1_momenthalverwege.webp
:align: center
```

## Scharnierligger
Laten we de complexiteit een beetje vergroten met de volgende scharnierligger:

```{figure} ./scharnierligger/scharnierligger.svg
:width: 80%
:name: scharnierligegr
:align: center
Scharnierligger
```

```{exercise} Scharnierligger steunpunten
:label: sl
:nonumber: true

Maak de ligger op drie steunpunten met MOLA
```

````{solution} sl
:class: dropdown

```{figure} ./simply_supported/Oefening2_ligger.webp
:align: center
Ligger op drie steunpunten
```

```{exercise} Linker verticale oplegging
:label: sl_A
:nonumber: true

Toon het mechanisme waarmee de oplegreactie in de linker verticale oplegging bepaald kan worden
```

````{solution} sl_A
:class: dropdown

```{figure} ./simply_supported/Oefening2_verticalereactielinks.webp
:align: center
Mechanisme voor bepaling van de linker verticale oplegreactie. De oplegging links kan vrij verticaal bewegen en is dus eigenlijk een verticale roloplegging. 
```

```{exercise} Middelste verticale oplegging
:label: sl_B
:nonumber: true

Toon het mechanisme waarmee de oplegreactie in de middelste verticale oplegging bepaald kan worden
```

````{solution} sl_B
:class: dropdown

```{figure} ./simply_supported/Oefening2_verticalereactiemidden.webp
:align: center
```

```{exercise} Rechter verticale oplegging
:label: sl_C
:nonumber: true

Toon het mechanisme waarmee de oplegreactie in de rechter verticale oplegging bepaald kan worden
```

````{solution} sl_C
:class: dropdown

```{figure} ./simply_supported/Oefening2_verticalereactierechts.webp
:align: center
```

```{exercise} Moment boven middelste oplegging
:label: sl_D
:nonumber: true

Toon het mechanisme waarmee het moment boven de middelste oplegging bepaald kan worden
```

````{solution} sl_D
:class: dropdown

```{figure} ./simply_supported/Oefening2_momentmidden.webp
:align: center
```

```{exercise} Moment halverwege rechter overspanning
:label: sl_E
:nonumber: true

Toon het mechanisme waarmee het moment halverwege de rechter overspanning bepaald kan worden
```

````{solution} sl_E
:class: dropdown

```{figure} ./simply_supported/Oefening2_momentrechts.webp
:align: center
```

```{exercise} Dwarskracht in scharnier
:label: sl_F
:nonumber: true

Toon het mechanisme waarmee de dwarskracht in het scharnier bepaald kan worden
```

## Ingeklemde scharnierligger
Laten we het probleem nog ietsje moeilijker maken, met een ingeklemde scharnierligger

```{figure} ./hinged_SD/structure.svg
:width: 80%
:name: hb_model
:align: center
Ingeklemde scharnierligger
```

```{exercise} Ingeklemde scharnierligger
:label: hb
:nonumber: true

Maak de ingeklemde scharnierligger met MOLA
```

```{solution} hb
:class: dropdown

```{figure} ./hinged_SD/structure.webp
:align: center
```

```{exercise} Verticale oplegging bij A
:label: hb_A
:nonumber: true

Toon het mechanisme waarmee de verticale oplegreactie in A bepaald kan worden
```

````{solution} hb_A
:class: dropdown

```{figure} ./simply_supported/Oefening3_verticalereactieA.webp
:align: center
Mechanisme voor de bepaling van de verticale oplegreactie in A. De oplegging in A is een inklemming die vrij kan bewegen in verticale richting. 
```

```{exercise} Oplegmoment bij A
:label: hb_Am
:nonumber: true

Toon het mechanisme waarmee het oplegmoment in A bepaald kan worden
```

````{solution} hb_Am
:class: dropdown

```{figure} ./simply_supported/Oefening3_momentA.webp
:align: center
```

```{exercise} Verticale oplegging bij B
:label: hb_B
:nonumber: true

Toon het mechanisme waarmee de verticale oplegreactie in B bepaald kan worden
```

````{solution} hb_B
:class: dropdown

```{figure} ./simply_supported/Oefening3_verticalereactieB.webp
:align: center
```

```{exercise} Verticale oplegging bij C
:label: hb_C
:nonumber: true

Toon het mechanisme waarmee de verticale oplegreactie in C bepaald kan worden
```

````{solution} hb_C
:class: dropdown

```{figure} ./simply_supported/Oefening3_verticalereactieC.webp
:align: center
```

```{exercise} Moment in D
:label: hb_MD
:nonumber: true

Toon het mechanisme waarmee het moment in D bepaald kan worden

```

````{solution} hb_MD
:class: dropdown

```{figure} ./simply_supported/Oefening3_momentD.webp
:align: center
```

```{exercise} Moment in B
:label: hb_MB
:nonumber: true

Toon het mechanisme waarmee het moment in B bepaald kan worden

```

````{solution} hb_MB
:class: dropdown

```{figure} ./simply_supported/Oefening3_momentB.webp
:align: center
```

```{exercise} Dwarskracht in D
:label: hb_VD
:nonumber: true

Toon het mechanisme waarmee de dwarskracht in D bepaald kan worden

```

````{solution} hb_VD
:class: dropdown

```{figure} ./simply_supported/Oefening3_dwarskrachtD.webp
:align: center
Mechanisme voor bepaling van de dwarskracht in D, de delen links en rechts van D lopen evenwijdig. 
```
