# Orejas dobles: suplemento de las pruebas formales

Juan Pablo Traverso Gianini  
Investigador independiente, Santiago, Chile  
ORCID 0009-0003-6068-4096

*Suplemento de Cotas óptimas para absorbedores de orejas dobles por triángulos de tipos prescritos*  
*Preprint 1.0 · 26 de noviembre de 2026*  
DOI [10.5281/zenodo.24555328](https://doi.org/10.5281/zenodo.24555328)

## 1. Enunciados comprobados en Lean

La formalización usa el predicado `IsAbsorber` del artículo II. Este exige que $A$ y $P$ sean disjuntos y que tanto $A$ como $A\cup P$ admitan descomposiciones en triángulos mixtos. La partición en dos etiquetas es independiente de la división de los vértices según sus tres funciones. En la tabla, los nombres de las declaraciones son relativos a `PartitionedTriangleAbsorption.SignedCertificate`.

| Espacio de nombres | Declaración | Conclusión |
|:--|:--|:--|
| DoubledEarEquality | `core_sensitive_bound` | Cota inferior del teorema 1 |
| DoubledEarEquality | `protected_centres_bound` | Cota con centros protegidos |
| DoubledEarEquality | `optimum_iff_routing_modes` | Igualdad en términos de incidencias |
| DoubledEarEquality | `twoMode_of_routing_modes` | Transferencia a los dos modos |
| TriangleFreeCore | `minimum_path_absorber` | Mínimo 18 |
| LabelledPathMinimum | `minimum_labelled_path_absorber` | Mínimo 21 |
| SubdividedClawMinimum | `minimum_subdivided_claw_absorber` | Mínimo 36 |
| SubdividedClawMinimum | `no_connected_triple_partition` | Obstrucción para la garra subdividida |

**Alcance.** La cota inferior formal cuenta las aristas de $A$ cuyos dos extremos son centros. Bajo la hipótesis sobre el subgrafo inducido, estas aristas forman exactamente $A\cap C$. El teorema de igualdad supone que $P$ consta de aristas del grafo ambiente entre centros y orejas, que todas las aristas de ese tipo pertenecen a $P$, que todas las aristas entre centros pertenecen a $C$, que no hay aristas entre orejas y que $|P|=4|C|$. Su conclusión caracteriza la igualdad mediante dos familias de triángulos mixtos de los tipos prescritos, disjuntos en aristas dentro de cada familia, que cubren el mismo conjunto de aristas fuera de la fuente. El lema `spoke_mem_iff` identifica los vecinos auxiliares correspondientes en cada centro. Para las orejas dobles, la sección 2 deduce las permutaciones locales de estas incidencias. El teorema de transferencia requiere además un conjunto de retorno disjunto del grafo ambiente que admita una descomposición en triángulos mixtos. Para la familia de la sección 4, Lean verifica el núcleo de seis aristas, su óptimo y su obstrucción. La prueba para todo $k$ es la de identificación de centros y recuento de esa sección.

## 2. Reproducción de la verificación

La [revisión de las fuentes](https://github.com/jtraverso/typed-triangle-absorption/tree/c7bae66dfd66370138d2f1a6ecc51d3aa29ea8e4) fija Lean 4.35.0-rc3 y la revisión `c55e6e786f49471c72fbddbec5415808896aec1e` de Mathlib. El [archivo ZIP](https://github.com/jtraverso/nash-williams-triangle-decompositions-release/releases/download/doubled-ears-preprint-1.0-r3/Doubled_ears_LEAN_SOURCE_v1.0.zip) contiene los 1.588 archivos bajo control de versiones, incluidos 1.522 archivos fuente de Lean y el manifiesto de dependencias. Lake descarga los paquetes externos en las revisiones indicadas en el manifiesto.

Tras descomprimir el archivo, se ejecutan las siguientes órdenes en la carpeta que contiene `lean-toolchain`. La primera compila los módulos de enunciados y de pruebas de esta nota. La segunda ejecuta Comparator en una instalación de Linux con aislamiento y soporte para Nanoda.

```
lake build +DoubledEarsChallenge +DoubledEarsSolution
lake comparator --config comparator.doubled-ears.json
```

El módulo de enunciados usa un `sorry` para cada uno de los ocho enunciados propuestos. El módulo `DoubledEarsSolution` importa las demostraciones. Al consultar cada declaración desde este módulo se obtienen exactamente los axiomas `propext`, `Classical.choice` y `Quot.sound`. La comparación en Windows utilizó el núcleo predeterminado de Lean, con el aislamiento y Nanoda desactivados. El [registro de verificación](https://github.com/jtraverso/nash-williams-triangle-decompositions-release/tree/doubled-ears-preprint-1.0-r3/series_notes/DOUBLED_EAR_ABSORBERS/preprint-1.0/formalization) recoge la configuración y la salida para las ocho declaraciones.

**SHA-256 del archivo de fuentes**

`f740fb0a8db4003c2dd652d859feab62db259537c866037e0bb70a6906d195a2`
