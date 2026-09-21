# Datos

Los datos del proyecto **no se versionan en este repositorio**. El material de la organización
beneficiaria está marcado como información confidencial y su uso queda sujeto al convenio de
confidencialidad (NDA) que el equipo firma en el Avance 0 (semana 2). Este documento describe el
origen, la estructura y la forma de acceso, conforme a lo solicitado por el curso.

## Origen

| Fuente | Contenido | Provisión |
|---|---|---|
| Organización beneficiaria (Bnext) | Fotografías y video de anaqueles en piso de venta | A través del patrocinador, sujeto a NDA |
| Organización beneficiaria (Bnext) | Planogramas de referencia de las exhibiciones evaluadas | A través del patrocinador, sujeto a NDA |
| Equipo | Anotaciones de caja delimitadora y clase, generadas sobre el material anterior | Trabajo propio |

El alcance definitivo del conjunto (número de exhibiciones, categorías y sucursales) se acuerda con
el patrocinador en el Avance 0 y se documenta aquí en la semana 3.

## Estructura

```
data/
├── raw/          Material tal como se recibe. No se modifica nunca.
├── planogram/    Representación digital del planograma de referencia.
└── processed/    Anotaciones, particiones y derivados listos para modelar.
```

### `raw/`

Imágenes y video de anaquel en su resolución original, organizados por exhibición. Se conserva
intacto para que cualquier resultado pueda rastrearse hasta su fuente.

### `planogram/`

Especificación de la distribución prescrita. El esquema se define como primer objetivo específico
del proyecto y se entrega en la semana 3; expresa, para cada exhibición, la estructura del mueble
(charolas y posiciones) y el producto asignado a cada posición.

### `processed/`

Anotaciones en formato estándar de detección de objetos, junto con las particiones de
entrenamiento, validación y prueba. La partición es **agrupada por exhibición**: todas las
capturas de un mismo anaquel caen en la misma partición, para que la métrica mida generalización y
no memorización del mueble.

## Forma de acceso

1. Firmar el convenio de confidencialidad con la organización beneficiaria (Avance 0, semana 2).
2. Solicitar el acceso al patrocinador: Dr. Juan Arturo Nolazco Flores — jnolazco@tec.mx
3. Descargar el material al directorio local `data/raw/`, respetando la estructura descrita.
4. No copiar el material fuera del entorno de trabajo acordado ni publicarlo en ningún medio.

## Reglas de manejo

- Ningún archivo de imagen, video o planograma se agrega al control de versiones; `.gitignore`
  excluye esos formatos de forma explícita.
- Ningún resultado publicado incluye identificadores comerciales de la organización sin
  autorización expresa del patrocinador.
- Los resultados se reportan de forma agregada o sobre ejemplos autorizados.
