# Spec: Turnos

Versión 1.0. Soporta HU-05 (Must).

## Propósito

Decidir a quién le toca actuar. Los turnos giran sin fin: jugador, monstruo, monstruo, jugador, y así.

## Fuera de alcance

- Entidades que entran a mitad de partida.
- Turnos con distinta velocidad.

## Operaciones

| Firma | Precondiciones | Postcondiciones | Errores |
|---|---|---|---|
| agregar(entidad) | ninguna | la entidad entra al ciclo de turnos | ninguno |
| actual() | hay al menos una entidad | devuelve a quien le toca | IndexError si no hay entidades |
| avanzar() | hay al menos una entidad | pasa el turno a la siguiente y la devuelve | IndexError si no hay entidades |
| esta_vacia() | ninguna | verdadero si no hay entidades | ninguno |

## Invariantes

- Después de avanzar tantas veces como entidades hay, el turno vuelve a la misma entidad.

## Criterios de aceptación

Este componente apoya CA-13: en cada turno, cada monstruo avanza una casilla. La prueba de CA-13 está en la partida.

## Casos extremos

- Sin entidades.
- Una sola entidad: avanzar la deja a ella misma.
- Dar una vuelta completa.

## Historial de cambios

| Versión | Fecha | Cambio | Motivo |
|---|---|---|---|
| 1.0 | 2026-11-09 | Versión inicial | Entrega final |
