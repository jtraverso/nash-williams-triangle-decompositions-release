# Auditoría interna — Paper III, preprint 1.0

**Veredicto: PASS.** Se revisaron los manuscritos y suplementos de formalización
en inglés y español: cuatro documentos, doce archivos MD/TeX/PDF y 66 páginas.
El formato de evidencia sigue las auditorías coordinadas de Papers I y II:
protocolo, identidad inicial, integridad semántica, bibliografía, concordancia
formal, regresiones, enlaces, certificado visual y manifiesto final.

## Resultado por control

| Control | Evidencia | Resultado |
|---|---|---|
| Enunciados y ecuaciones | PROTECTED_ELEMENT_INDEX.json, FINAL_EDITORIAL_CHECKS.json | PASS |
| Traducción de 413 pares de párrafos | FINAL_EDITORIAL_CHECKS.json | PASS |
| Correcciones de interfaces matemáticas | SEMANTIC_INTEGRITY_REPORT.md, REVIEW_DISPOSITIONS.md | PASS |
| Referencias reales a Lean y cierres de importación | MODULE_MAP_CERTIFICATE.json | PASS |
| Fuentes, objetos y seis consultas de axiomas | FROZEN_EVIDENCE.json | PASS |
| Cálculos exactos y certificado de treinta triángulos | check_written_identities.json | PASS |
| Bibliografía y atribución | BIBLIOGRAPHIC_REVIEW.md | PASS dentro del alcance declarado |
| Estilo, estructura y alcance de la prueba | STYLE_AND_SCOPE_REPORT.md | PASS |
| Referencias PDF y enlaces | LINK_CERTIFICATE.json | PASS |
| Cuatro PDF y seis figuras | VISUAL_CERTIFICATE.json, FIGURE_RENDER_CERTIFICATE.json | PASS |
| Edición pública inicial sin estados de borrador | FINAL_EDITORIAL_CHECKS.json | PASS |

## Hallazgos resueltos

Se corrigieron las atribuciones del criterio y la bisagra; la comparación
explicita la distinta potencia impresa. La búsqueda del manuscrito separado
tiene la misma fecha en ambos idiomas. Se sustituyó una cita Lean inexistente
por el lema de envolvente con signo realmente usado y se incluyeron sus
condiciones. Las versiones explícitas ya no se presentan como los lemas del
cierre de T. Se explicitaron la persistencia por aristas, el dominio real de la
inversa, la preparación con parámetros fijos, la contracción, el orden de las
constantes y las dos mitades del presupuesto de Pasch. La respuesta completa a
cada observación está en REVIEW_DISPOSITIONS.md.

El defecto de trazos PDF se reprodujo en la bisagra y en el perfil. Las figuras
se regeneraron y pasan dos motores de lectura; el modo b es visible. Los
agradecimientos familiares y la nota de herramientas conservan su texto exacto.
Los cuatro documentos se presentan como preprint 1.0, sin historia de ediciones.

La afirmación universal de un objetivo de Pasch de orden cuadrático con cota
inferior positiva no se incorporó: H1–H4 permiten una familia vacía. Tampoco se
añadieron declaraciones de prioridad exhaustiva ni de distancia de corte.

## Evidencia formal y límites

El registro completo cubre 1.141 módulos. Se corrigieron solo comentarios en
quince fuentes, se comprobó la igualdad exacta del texto restante y se
recompilaron esos quince módulos. Se reutilizaron 1.126 módulos con validación de
hashes y se ejecutaron nuevamente las seis consultas de axiomas. Solo aparecen
`propext`, `Classical.choice` y `Quot.sound`. Se conserva el registro original,
incluidos los intentos fallidos. La identidad del archivo actual es
`a5fbd7af2d13594a894d61bde81126353bd7d186f335ad9f302a5fd7ba942d95`.

Esto no se describe como una compilación desde un caché vacío. No se
recompilaron las dependencias externas. Las regresiones finitas no sustituyen
los argumentos universales. Las pruebas generales completas residen en Lean;
el artículo explica su construcción y demuestra las aplicaciones. Los lemas
locales de inserción de Pasch no se presentan como una prueba impresa
autocontenida. Este PASS es interno y asistido por IA, no revisión humana
independiente ni certificación de prioridad histórica.

**Observaciones internas sin resolver: ninguna dentro de este alcance.** La
preparación del release y el cambio de visibilidad del repositorio son una etapa
posterior; esta auditoría no los ejecuta.

## Precisiones finales en §2.2 y D.4

PASS. La comparación distingue el enunciado impreso de la Definición 13.15 y el conteo de ocho vértices de la prueba del Lema 14.4. La incompatibilidad asintótica se limita expresamente a un par raíz existente y un orden acotado; no se atribuye una corrección confirmada por los autores. D.4 identifica la capa exterior con familia previa vacía como origen de la cota inicial 67 y explica su paso a la inicialización interior. Se revisaron de nuevo los cuatro PDF y sus 66 páginas, la concordancia bilingüe y los elementos protegidos. El suplemento formal y el archivo del freeze son idénticos byte a byte; no se ejecutó una nueva compilación Lean por estas correcciones de exposición. MINOR_CORRECTIONS.json registra las fuentes, las operaciones autorizadas y sus hashes.
