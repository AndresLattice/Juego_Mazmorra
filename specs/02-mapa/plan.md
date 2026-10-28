# Plan: Mapa

Versión 1.1.

## Estructura elegida

Matriz densa: un arreglo de filas, donde cada fila es un arreglo de celdas. Vive en `dominio/mapa.py`.

Cada celda guarda uno de tres valores:
- `None`: libre.
- `"#"`: obstáculo.
- un texto con el nombre del objeto.

## Por qué esta estructura

- La operación que más se repite es consultar una celda por fila y columna. En una matriz eso es O(1).
- El mapa es pequeño (20x20 = 400 celdas) y casi todas las celdas son libres que el jugador recorre.

## Complejidad

| Operación | Costo |
|---|---|
| Mapa(filas, columnas) | O(f·c) |
| en_rango | O(1) |
| poner_obstaculo, es_obstaculo | O(1) |
| poner_objeto, objeto_en, quitar_objeto | O(1) |

## Alternativa descartada

Matriz dispersa. Solo guarda las celdas con algo. Aquí como máximo el 25 % son obstáculos, así que ahorra poca memoria, y la consulta deja de ser O(1).

## Soporte interno

Se usan `list` de Python como arreglos de tamaño fijo, como el arreglo de la semana 4. Se crean una vez al iniciar y nunca crecen ni se acortan.

## Historial de cambios

| Versión | Fecha | Cambio | Motivo |
|---|---|---|---|
| 1.0 | 2026-10-27 | Versión inicial | Entrega 2 |
| 1.1 | 2026-10-27 | Se agrega `objeto_en` a la tabla de complejidad | Acompaña la spec 1.1 |
