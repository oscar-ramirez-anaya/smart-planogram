# Semana 4 — Avance 2. Ingeniería de características

Entregable de la semana 4 del Proyecto Integrador, fase de *Preparación de los datos* de la
metodología CRISP-ML(Q).

| Archivo | Descripción |
|---|---|
| `Avance2.48.ipynb` | Libreta ejecutada de principio a fin dentro del servidor de Bnext |
| `Avance2.48.pdf` | Reporte del avance |
| `Avance2.48.docx` | Reporte en formato editable |
| `Avance2.48.html` | Fuente del PDF |
| `assets/` | Hoja de estilo de impresión y logotipo institucional |

## Contenido

- **A. Ingeniería de características:** extracción base (geometría, exposición, color, LBP, HOG),
  construcción de variables de dominio, discretización, codificación, partición por bloques
  temporales, transformaciones Box-Cox / Yeo-Johnson y comparación de escaladores.
- **B. Selección y extracción:** umbral de varianza, correlación, ANOVA, chi-cuadrado, información
  mutua, PCA y análisis factorial, con una comparativa de siete configuraciones.
- **C. Conclusiones** de la fase de Preparación de los datos.

## Regenerar

La libreta y el reporte se generan desde `scripts/`:

```bash
python3 scripts/construir_avance2.py          # escribe la libreta sin ejecutar
# en el servidor de Bnext, con PLANOGRAMA_DATA_DIR y PLANOGRAMA_OUT_DIR definidos:
jupyter nbconvert --to notebook --execute --inplace docs/semana04_avance2/Avance2.48.ipynb
python3 scripts/generar_documento_avance2.py  # HTML, PDF y DOCX con las figuras de la libreta
```

## Datos

Conforme a [`../POLITICA_DATOS.md`](../POLITICA_DATOS.md), las imágenes, las tablas de
características y el pipeline ajustado permanecen en el servidor de Bnext. La libreta y el reporte
contienen solo gráficas y tablas agregadas; los SKU están anonimizados.
