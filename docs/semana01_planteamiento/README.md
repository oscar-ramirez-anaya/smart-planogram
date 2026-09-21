# Semana 1 — Planteamiento del proyecto

Entregable de la semana 1 del Proyecto Integrador.

| Archivo | Descripción |
|---|---|
| `DatosGenerales.48.pdf` | Entregable final, subido a Canvas |
| `DatosGenerales.48.html` | Fuente editable del documento |
| `assets/print.css` | Hoja de estilo de impresión (A4) |

## Regenerar el PDF

Tras editar el HTML, desde esta carpeta:

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless --disable-gpu --no-pdf-header-footer \
  --print-to-pdf="DatosGenerales.48.pdf" \
  "file://$(pwd)/DatosGenerales.48.html"

python3 numerar_paginas.py
```

`numerar_paginas.py` estampa el pie de página ("Página X de Y" y la referencia del equipo) sobre el
PDF generado, porque Chrome en modo headless no admite una plantilla de pie personalizada.

## Datos por confirmar

Estos campos están marcados en el documento y se cierran en el Avance 0 (semana 2):

- Matrículas de Germán Eduardo Rodríguez Vázquez y Jesús Soto Medrano.
- Área o departamento de la organización beneficiaria.
- Sector SCIAN, declarado como 46 (Comercio al por menor) a reserva de validación con el patrocinador.
