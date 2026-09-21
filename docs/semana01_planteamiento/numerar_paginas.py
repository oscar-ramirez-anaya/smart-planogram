"""Estampa el pie de página sobre DatosGenerales.48.pdf.

Chrome en modo headless no admite una plantilla de pie personalizada desde la linea de
comandos: o imprime su pie por omision (con la URL local del archivo) o no imprime ninguno.
Este script agrega el pie correcto sobre el PDF ya generado.

Uso, desde esta carpeta:
    python3 numerar_paginas.py
"""

from pathlib import Path

import fitz

PDF = Path(__file__).parent / "DatosGenerales.48.pdf"
IZQUIERDA = "TC5035.10 Proyecto Integrador  ·  Equipo 48 — Smart Planogram"
GRIS = (0.42, 0.42, 0.42)
LINEA = (0.79, 0.81, 0.84)
MARGEN_X = 56.7   # 20 mm
BASE_Y = 42.5     # 15 mm desde el borde inferior


def main() -> None:
    documento = fitz.open(PDF)
    total = documento.page_count

    for indice, pagina in enumerate(documento, start=1):
        if indice == 1:                      # la portada no lleva pie
            continue

        ancho, alto = pagina.rect.width, pagina.rect.height
        y = alto - BASE_Y

        pagina.draw_line(
            fitz.Point(MARGEN_X, y - 9), fitz.Point(ancho - MARGEN_X, y - 9),
            color=LINEA, width=0.5,
        )
        pagina.insert_text(
            fitz.Point(MARGEN_X, y + 2), IZQUIERDA,
            fontname="helv", fontsize=7.5, color=GRIS,
        )

        derecha = f"Página {indice} de {total}"
        ancho_texto = fitz.get_text_length(derecha, fontname="helv", fontsize=7.5)
        pagina.insert_text(
            fitz.Point(ancho - MARGEN_X - ancho_texto, y + 2), derecha,
            fontname="helv", fontsize=7.5, color=GRIS,
        )

    documento.set_metadata({
        "title": "Planteamiento del proyecto — Smart Planogram",
        "author": "Equipo 48 — Smart Planogram",
        "subject": "TC5035.10 Proyecto Integrador — Semana 1",
        "keywords": "planograma, retail, vision computacional, deteccion de objetos",
    })
    documento.saveIncr()
    documento.close()
    print(f"Pie de página aplicado a {total} páginas: {PDF.name}")


if __name__ == "__main__":
    main()
