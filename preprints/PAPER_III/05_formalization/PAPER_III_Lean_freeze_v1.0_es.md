---
title: 'Paper III: Suplemento de la prueba formal'
lang: es
version: '1.0'
---

# Paper III: Suplemento de la prueba formal

**Juan Pablo Traverso Gianini**

**Preprint 1.0 — 1 de noviembre de 2026. Verificación formal: PASS.**

## 1. Alcance de la prueba

Las pruebas generales completas son las declaraciones Lean de la tabla siguiente. El manuscrito explica su construcción, sus condiciones cuantitativas y su ensamblaje, y demuestra las aplicaciones. Los lemas locales de bancos, empaquetamiento e inserción de Pasch se proporcionan en el suplemento formal; el artículo no pretende reproducirlos todos como una prueba autocontenida en prosa.

La aplicación latina de dos escalas incluye las condiciones simultáneas sobre bloques gruesos y el corolario de separación de conteos. Su prueba formal usa la cota diagonal (8.24); la identidad finita exacta (8.23) es un cálculo escrito separado. El programa de altura tiene 312 definiciones aritméticas y una igualdad auditada con la altura utilizada en el Teorema 7.2.

## 2. Declaraciones auditadas

| Resultado | Declaración |
|---|---|
| T | `TypedTriangle.Vortex.main_theorem_T` |
| T+ | `TypedTriangle.Vortex.main_theorem_T_with_triangle_monitors_and_pasch` |
| 7.2 | `TypedTriangle.Vortex.Explicit.main_theorem_T_with_triangle_monitors_at_tower_order` |
| 8.1 | `TypedTriangle.Applications.Latin.latin_square_with_profile_statistics` |
| 8.2 | `TypedTriangle.Applications.Latin.uniform_with_intercalates` |
| 8.3 | `TypedTriangle.Applications.Latin.signed_profile_with_intercalates` |
| 8.4 | `TypedTriangle.Applications.Latin.TwoScale.latin_two_scale_with_blocks` |
| 8.4 | `TypedTriangle.Applications.Latin.TwoScale.intercalate_gap_of_targets` |
| 8.5 | `TypedTriangle.Applications.FivePartite.main_theorem` |
| H | `TypedTriangle.PrintedHeight.height_agrees` |

## 3. Identidad de las fuentes y axiomas

El suplemento de fuentes contiene 1.141 módulos del proyecto. La reconstrucción completada registra la compilación satisfactoria de todos ellos. Después se corrigió documentación dentro de comentarios en quince archivos: se comprobó la igualdad exacta del texto fuera de comentarios y se recompilaron esos módulos. Los otros 1.126 módulos compilados se reutilizaron tras validar sus hashes. Las seis consultas de axiomas de los resultados finales se ejecutaron de nuevo satisfactoriamente sobre esta colección de objetos. H1–H4 y el código matemático Lean no cambiaron.

Solo aparecen los siguientes axiomas fundamentales: `propext`, `Classical.choice`, `Quot.sound`. Las consultas usan `pp.fullNames=true`; la lista permitida no contiene axiomas propios del proyecto ni `sorryAx`.

**Archivo de fuentes:** `PAPER_III_LEAN_SOURCE_v1.0.zip`.

**SHA-256:** `a5fbd7af2d13594a894d61bde81126353bd7d186f335ad9f302a5fd7ba942d95`.

**SHA-256 del manifiesto de fuentes:**  
`16e579200583065b7f5ba46db2c4f8af84608c551f5c736834abcc044286dc37`.

## 4. Reproducción

Use Lean 4.35.0-rc3 y la revisión de Mathlib `c55e6e786f49471c72fbddbec5415808896aec1e`. Verifique el archivo y su manifiesto interno, y compile los ocho objetivos explícitos:

```
lake build RequestProject.TypedTriangle.MainPaperIII
lake build RequestProject.TypedTriangle.MainPaperIIIPasch
lake build RequestProject.TypedTriangle.MainPaperIIITriangleTower
lake build RequestProject.TypedTriangle.ApplicationsLatinMain
lake build RequestProject.TypedTriangle.ApplicationsLatinCorollaries
lake build RequestProject.TypedTriangle.ApplicationsFivePartiteMain
lake build RequestProject.TypedTriangle.ApplicationsTwoScaleFinal
lake build RequestProject.TypedTriangle.PaperIIIHeightProgram
```

El objetivo predeterminado de Lake alcanza solo T; de él no se infiere la compilación de las otras entradas. Ejecute por separado los seis archivos de `audit/` con `lake env lean -Dpp.fullNames=true`. Sus resultados y las identidades de fuentes acompañan al suplemento. Las dependencias están fijadas y no deben actualizarse durante la reproducción.

La reconstrucción registrada reutilizó objetos compilados validados, incluidas las familias completas de objetos Lean. No es una compilación nueva desde un caché vacío y no recompiló las dependencias externas. El suplemento de fuentes no contiene caché binario. Su README da los comandos completos de reproducción y explica la separación de los cierres de importación compatibles de las auditorías.

Los archivos `HEIGHT_PROGRAM_en.md` y `HEIGHT_PROGRAM_es.md` imprimen código aritmético idéntico. Especifican un umbral para estadísticas de triángulos; no se afirma un umbral explícito conjunto para Pasch.

## 5. Mapa de la construcción

Los siguientes archivos identifican la construcción técnica utilizada en las Secciones 3–6. Pertenecen al cierre de fuentes de T o T+, según corresponda. Las versiones con orden explícito pertenecen al argumento cuantitativo de la Sección 7; su uso no se infiere solo del objetivo predeterminado de compilación.

| Paso del manuscrito | Fuente formal |
|---|---|
| Cociente local y persistencia bajo eliminación de vértices | `VertexFirstEntry.lean`, `PreparedCoreConstruction.lean` |
| Persistencia bajo eliminación dispersa de aristas | `SparseEdgeHost.lean`, `G4ReferenceH2Generic.lean` |
| Inversa suave en el hijo pagado y exactificación | `VortexPaidChildSmooth.lean`, `SmoothExactification.lean` |
| Perfil bruto a través de la cadena preparada | `VortexIntrinsicRawPathsPreparedVortex.lean` |
| Reserva elegida uniformemente antes del residuo | `VortexUniformTerminalReserve.lean` |
| Funciones de prueba con signo y masa inferior de la envolvente | `SignedEnvelopePacking.lean` |
| Presupuesto inicial de Pasch y tasa exterior | `PaschAdaptiveInitialState.lean`, `PaschFinalAssemblyParameters.lean` |
| Cotas de inserción de Pasch y recurrencia interior | `PaschConcreteInnerAdaptiveLayers.lean` |
| Ensamblaje de T y T+ | `MainPaperIII.lean`, `MainPaperIIIPasch.lean` |

El certificado interno del mapa de módulos registra las dependencias de importación y las declaraciones exactas. En particular, la entrada de la exactificación debe pertenecer a la imagen real de incidencia, el teorema de la envolvente con signo requiere una masa inferior lineal y las estimaciones de Pasch usan las cotas de cogrado de la familia disponible. El manuscrito enuncia estas condiciones; los archivos fuente contienen sus construcciones locales completas.

Los números de referencia [16] y [17] de la nota de herramientas que sigue remiten a la bibliografía del manuscrito adjunto.

## Agradecimientos

El autor agradece profundamente a su esposa María Paz y a sus hijos Lucas, Juan Cristóbal, Francisca, Raimundo y Benjamín su amor, paciencia y apoyo.

## Uso de inteligencia artificial y herramientas computacionales

Se utilizaron Claude, de Anthropic, y ChatGPT/Codex, de OpenAI, para explorar y revisar argumentos y preparar el manuscrito. Aristotle, de Harmonic, contribuyó a explorar enfoques, buscar contraejemplos, desarrollar demostraciones y formalizarlas y revisarlas en Lean. Su participación no se limitó a traducir pruebas terminadas.

Certo [16] y Jacobian [17] se utilizaron para explorar casos finitos, comprobar identidades y evaluar construcciones candidatas. Estos cálculos orientaron el desarrollo de los argumentos; las comprobaciones finitas no se trataron como pruebas de enunciados universales.

El autor es responsable de los argumentos, las citas, el código y la presentación. Ningún sistema de inteligencia artificial figura como autor.
