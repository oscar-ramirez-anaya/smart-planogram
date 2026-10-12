# Smart Planogram

Verificación automática del cumplimiento de planograma en retail mediante visión computacional.

Proyecto Integrador (TC5035.10, Grupo 10) — Maestría en Inteligencia Artificial Aplicada,
Tecnológico de Monterrey. Trimestre septiembre – diciembre 2026.

---

## Problema

El planograma especifica qué producto debe ocupar cada posición de un anaquel. Su verificación se
hace hoy de forma manual, recorriendo la tienda y comparando el acomodo observado contra el
diagrama de referencia: un proceso lento, costoso y propenso a errores, que se degrada conforme
crecen el catálogo, las variantes regionales y la rotación de empaques.

## Propósito general

Desarrollar una solución de inteligencia artificial que evalúe automáticamente el cumplimiento de
planograma a partir de fotografías o video de la exhibición.

## Objetivos específicos

1. Definir una representación digital del planograma que sirva como referencia comparable de forma automática.
2. Preparar un conjunto de imágenes y video de productos de ejemplo, con su esquema de anotación.
3. Detectar e identificar los productos presentes en la exhibición.
4. Comparar la distribución observada contra la distribución de referencia.
5. Clasificar cada posición en tres estados: correcto, faltante e incorrecto.
6. Evaluar la precisión del prototipo y analizar los retos de escalabilidad de la solución.

## Dominio de aplicación

Visión computacional. La entrada primaria del sistema es exclusivamente visual, la tarea central es
detección y localización de objetos con reconocimiento de grano fino, y la salida se deriva de
conciliar la distribución espacial detectada contra la prescrita por el planograma.

---

## Equipo 48 — Smart Planogram

| Integrante | Matrícula |
|---|---|
| Oscar Alberto Ramírez Anaya | A01795438 |
| Germán Eduardo Rodríguez Vázquez | A01796325 |
| Jesús Soto Medrano | A01794746 |

**Patrocinador:** Dr. Juan Arturo Nolazco Flores — Director del Hub de Ciencia de Datos y
Ciberseguridad, Tecnológico de Monterrey — jnolazco@tec.mx

**Organización beneficiaria:** Bnext, mediante el Programa de Vinculación Tecnológica BNext.

---

## Estructura del repositorio

```
.
├── data/                 Datos del proyecto (contenido no versionado; ver data/README.md)
│   ├── raw/              Imágenes y video de anaquel, tal como se reciben
│   ├── planogram/        Representación digital del planograma de referencia
│   └── processed/        Anotaciones, particiones y derivados listos para modelar
├── notebooks/            Cuadernos de análisis, experimentación y desarrollo
├── docs/                 Entregables y documentación por semana
│   ├── semana01_planteamiento/
│   ├── semana02_avance0/
│   ├── semana03_avance1/
│   ├── semana04_avance2/
│   └── POLITICA_DATOS.md Acuerdo de manejo de datos con Bnext
├── scripts/              Utilidades: verificación de publicación y generación de libretas
├── .githooks/            Hook pre-commit que aplica la política de datos
├── src/                  Código del pipeline de detección y conciliación
└── README.md
```

| Elemento | Descripción |
|---|---|
| `README.md` | Este archivo: descripción, objetivo, integrantes y estructura. |
| `data/` | Datos utilizados en el proyecto. El material provisto por la organización beneficiaria es confidencial y no se publica; `data/README.md` documenta su origen, estructura y forma de acceso. |
| `notebooks/` | Cuadernos numerados que fijan el orden de ejecución del análisis. |
| `docs/` | Documentos y materiales relevantes para el desarrollo y seguimiento, incluyendo los entregables de las semanas 1, 2, 8 y 9. |
| `scripts/` | `verificar_publicacion.py` (revisión previa a cada commit) y generadores de libretas. |
| `src/` | Código del pipeline. |

---

## Metodología y plan de entregables

El proyecto sigue CRISP-ML(Q) (Visengeriyeva et al., 2023). Los entregables de las semanas 1, 2, 8, 9 y 10–11 son los obligatorios
del curso; los de las semanas 3 a 7 conservan la nomenclatura y el propósito metodológico de
referencia, adaptados al dominio de detección de objetos.

| Semana | Entregable comprometido |
|---|---|
| 1 | Planteamiento del proyecto |
| 2 | Avance 0. Propuesta de proyecto y firma de convenios |
| 3 | Avance 1. Análisis exploratorio de datos |
| 4 | Avance 2. Ingeniería de características |
| 5 | Avance 3. Línea base con detector preentrenado y conciliación geométrica |
| 6 | Avance 4. Comparativa de arquitecturas de detección con ajuste fino |
| 7 | Avance 5. Pipeline integrado y evaluado |
| 8 | Avance 6. Producto de difusión |
| 9 | Avance 7. Resumen ejecutivo |
| 10 – 11 | Presentación final |

Condiciones de rigor aplicadas a todos los avances: partición agrupada por exhibición, semilla fija
en todo componente estocástico, versionado del conjunto de evaluación y registro de cada
experimento en una tabla comparativa única.

El planteamiento completo está en
[`docs/semana01_planteamiento/`](docs/semana01_planteamiento/).

---

## Confidencialidad

El material provisto por la organización beneficiaria está marcado como información confidencial y
su uso queda sujeto al convenio de confidencialidad (NDA) que el equipo firma en el Avance 0.

Este repositorio no contiene credenciales, contraseñas, tokens, información confidencial ni datos
que no puedan compartirse. Las imágenes de anaquel, los planogramas y cualquier identificador
comercial de la organización quedan fuera del control de versiones por reglas explícitas en
`.gitignore`.

El código se versiona aquí, pero se ejecuta sobre los datos dentro de la infraestructura de Bnext;
los resultados se publican solo cuando el Tec los requiere y como agregados. Las reglas completas y
la lista de verificación están en [`docs/POLITICA_DATOS.md`](docs/POLITICA_DATOS.md). Para activar
la verificación automática en cada commit:

```bash
git config core.hooksPath .githooks
```
