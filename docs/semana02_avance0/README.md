# Semana 2 — Avance 0. Propuesta de proyecto y firma de convenios

Entregable de la semana 2 del Proyecto Integrador, conforme a la metodología CRISP-ML(Q).

| Archivo | Descripción |
|---|---|
| `Avance0.48.pdf` | Entregable final, subido a Canvas |
| `Avance0.48.html` | Fuente editable del documento |
| `assets/print.css` | Hoja de estilo de impresión (A4) |
| `numerar_paginas.py` | Estampa el pie de página y los metadatos sobre el PDF |

## Regenerar el PDF

Tras editar el HTML, desde esta carpeta:

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless --disable-gpu --no-pdf-header-footer \
  --print-to-pdf="Avance0.48.pdf" \
  "file://$(pwd)/Avance0.48.html"

python3 numerar_paginas.py
```

Los números de página del índice están escritos en el HTML (atributo `data-ref`). Si una edición
mueve el contenido de página, deben actualizarse antes de regenerar el PDF.

## Convenio de confidencialidad

El NDA firmado por los integrantes no se incluye en este repositorio ni en el entregable por su
carácter confidencial. El sponsor y el asesor tienen conocimiento de su firma.

## Pendientes para el Avance 1

- Caracterizar el conjunto de imágenes: formato, resolución, tiendas, categorías, anotaciones y metadatos.
- Confirmar con el líder técnico de Bnext si existen planogramas de referencia asociados.
- Validar con el sponsor las metas propuestas de la Tabla 3.
