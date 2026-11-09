# Spec: Rutas

Versión 1.0. Soporta HU-05 (Must).

## Propósito

Encontrar hacia dónde debe dar el siguiente paso un monstruo para llegar al jugador por un camino de menos pasos.

## Fuera de alcance

- A* (HU-09).
- Movimiento en diagonal.
- Esquivar a otros monstruos al calcular la ruta.

## Operaciones

| Firma | Precondiciones | Postcondiciones | Errores |
|---|---|---|---|
| siguiente_paso(mapa, desde, hasta) | `desde` y `hasta` están dentro del mapa | devuelve la celda vecina de `desde` que inicia un camino de menos pasos hacia `hasta`; None si no hay camino o si `desde` es igual a `hasta` | ninguno |

Las celdas son tuplas (fila, columna). Se puede pasar por cualquier celda sin obstáculo, en 4 direcciones.

## Criterios de aceptación

| ID | Criterio | Prueba |
|---|---|---|
| CA-13 | En cada turno cada monstruo avanza una casilla por una ruta de menos pasos hacia el jugador | test_siguiente_paso_ruta_mas_corta, test_monstruo_avanza_una_casilla |
| CA-14 | Si no existe ruta al jugador, el monstruo se queda quieto, sin error | test_sin_ruta_devuelve_none, test_monstruo_sin_ruta_se_queda_quieto |

## Casos extremos

- `desde` igual a `hasta`.
- Jugador vecino del monstruo.
- Jugador encerrado por obstáculos.
- Camino que obliga a rodear un muro.

## Historial de cambios

| Versión | Fecha | Cambio | Motivo |
|---|---|---|---|
| 1.0 | 2026-11-09 | Versión inicial | Entrega final |
