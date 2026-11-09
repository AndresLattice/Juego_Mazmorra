# Plan: Partida

Versión 1.0.

## Estructura elegida

Ninguna nueva. Vive en `dominio/partida.py` y usa las de los demás componentes.

## Cómo es un turno

1. El jugador actúa. Si la acción no se pudo hacer (por ejemplo, chocar con un muro), no pasa el turno.
2. Se revisa victoria y derrota.
3. La lista circular de turnos avanza por cada monstruo hasta volver al jugador. Cada monstruo pide su siguiente paso a `rutas` y avanza, salvo que la celda esté ocupada por otro monstruo.
4. Se revisa derrota otra vez.

## Victoria y derrota

- Victoria: no queda ningún tesoro en el mapa. Revisarlo cuesta O(f·c), una vez por turno.
- Derrota: algún monstruo está en la celda del jugador.

## Complejidad

| Operación | Costo |
|---|---|
| un turno completo | O(m · f·c): un BFS por cada uno de los m monstruos |
| revisar victoria | O(f·c) |
| revisar derrota | O(m) |

## Historial de cambios

| Versión | Fecha | Cambio | Motivo |
|---|---|---|---|
| 1.0 | 2026-11-09 | Versión inicial | Entrega final |
