# Semana 3 — Avance 1. Análisis exploratorio de datos

Entregable de la semana 3 del Proyecto Integrador, fase de *Entendimiento de los datos* de la
metodología CRISP-ML(Q).

| Archivo | Descripción |
|---|---|
| `Avance1.48.ipynb` | Libreta del EDA, ejecutada de principio a fin |
| `Avance1.48.pdf` | Reporte del EDA entregado en Canvas |
| `Avance1.48.docx` | Fuente editable del reporte |

## Datos utilizados

El EDA de este avance se construyó sobre un **conjunto de datos sintético** de anaqueles de tienda
pequeña (360 imágenes, 12 570 cajas, 8 tiendas, 2 muebles por tienda), generado dentro de la propia
libreta con semilla fija (`SEED = 48`). Las cifras ilustran el método de análisis y no son hallazgos
sobre los datos de la organización beneficiaria. **Este avance no contiene imágenes ni datos de
Bnext**: todas las figuras de la libreta muestran anaqueles sintéticos o gráficas agregadas.

## Regenerar

```bash
pip install numpy pandas opencv-python-headless matplotlib seaborn pillow scikit-learn
jupyter nbconvert --to notebook --execute --inplace Avance1.48.ipynb
```

El dataset sintético se escribe en `~/week3/data` (configurable con la variable de entorno
`AVANCE1_DATA_DIR`) y no se versiona.

## Notas de consistencia

El reporte y la libreta se redactaron en paralelo y difieren en algunas cifras; la libreta es la
fuente reproducible:

| Concepto | Reporte | Libreta |
|---|---|---|
| Detección de duplicados | dHash 256 bits, P 1.00 / R 0.40 (12 pares) | aHash 64 bits, P 0.93 / R 0.43 (14 pares) |
| Exactitud del clasificador de color | 0.95 | 0.97 |
| Imágenes con al menos un problema de calidad | 38.9 % | 37.5 % |
| Contraste medio | 41.9 | 44.26 |

## Continuidad

El Avance 2 (`../semana04_avance2/`) aplica la ingeniería de características sobre la muestra real
proporcionada por Bnext, ejecutada dentro de su infraestructura conforme a
[`../POLITICA_DATOS.md`](../POLITICA_DATOS.md).
