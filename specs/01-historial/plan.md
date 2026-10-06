# Plan: Historial de acciones

## Estructura elegida

Dos pilas, `hechas` y `deshechas`. Cada una es una pila enlazada propia en `estructuras/pila.py`. El historial se implementa en `dominio/historial.py`.

## Por qué esta estructura

- Deshacer y rehacer siempre operan sobre la acción más reciente.
- Apilar y desapilar son O(1).
- Una acción nueva vacía la pila de deshechas.

## Complejidad

| Operación | Costo |
|---|---|
| Pila.apilar | O(1) |
| Pila.desapilar | O(1) |
| Pila.ver_tope | O(1) |
| Pila.vaciar | O(1) |
| Historial.registrar | O(1) |
| Historial.deshacer | O(1) |
| Historial.rehacer | O(1) |

## Alternativa descartada

Lista doble con cursor. También es O(1), pero exige mantener el cursor y cortar la lista en cada acción nueva. Más código para el mismo resultado.

## Soporte interno

Ninguno. La pila se construye con nodos propios, sin `list` ni `deque`.

## Integración con el dominio

`dominio/historial.py` usa dos instancias de `Pila`. Cada acción del jugador se registra al final de su turno junto con sus efectos, como un objeto recogido.

## Historial de cambios

| Versión | Fecha | Cambio | Motivo |
|---|---|---|---|
| 1.0 | 2026-10-06 | Versión inicial | Entrega 1 |
