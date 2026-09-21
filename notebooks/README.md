# Notebooks

Cuadernos de análisis, experimentación y desarrollo del proyecto.

## Convención de nombrado

`NN_descripcion_corta.ipynb`, donde `NN` es un consecutivo de dos dígitos que fija el orden de
ejecución. Un cuaderno solo depende de los anteriores, nunca de los posteriores.

| Cuaderno | Contenido | Semana |
|---|---|---|
| `01_exploracion_inicial.ipynb` | Inventario y caracterización del corpus visual de anaquel | 3 |

## Reglas de trabajo

- Los cuadernos se ejecutan desde la raíz del repositorio; las rutas a datos son relativas
  (`data/raw/`, `data/processed/`).
- Ningún cuaderno contiene credenciales ni rutas absolutas de la máquina de un integrante.
- Toda operación estocástica fija su semilla al inicio del cuaderno.
- Antes de hacer commit se limpian las salidas que contengan imágenes o datos de la organización
  beneficiaria.
- El código que se reutiliza en más de un cuaderno se promueve a `src/`.
