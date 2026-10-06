# Plan: Historial de acciones

Versión 1.1.

## Estructura elegida

Dos pilas, `hechas` y `deshechas`. Cada una es una `PilaEnlazada` en `estructuras/pila.py`. El historial se implementa en `dominio/historial.py`.

## Por qué esta estructura

- Deshacer y rehacer siempre operan sobre la acción más reciente.
- `push` y `pop` son O(1).
- Una acción nueva reemplaza la pila de deshechas por una vacía.

## Complejidad

| Operación | Costo |
|---|---|
| PilaEnlazada.push | O(1) |
| PilaEnlazada.pop | O(1) |
| PilaEnlazada.peek | O(1) |
| PilaEnlazada.esta_vacia | O(1) |
| PilaEnlazada.tamaño | O(1) |
| Historial.registrar | O(1) |
| Historial.deshacer | O(1) |
| Historial.rehacer | O(1) |
| Historial.puede_deshacer | O(1) |
| Historial.puede_rehacer | O(1) |

## Alternativa descartada

Lista doble con cursor. También es O(1), pero exige mantener el cursor y cortar la lista en cada acción nueva. Más código para el mismo resultado.

## Soporte interno

Ninguno. La pila usa nodos propios, sin `list` ni `deque`.

## Código reutilizado de Clase

Este componente se apoya en código hecho en los laboratorios del curso. Se declara aquí para que quede registrado.

| Archivo del proyecto | Origen en Clase | Qué se hizo |
|---|---|---|
| `estructuras/nodo.py` | `Clase/semana_05/nodo.py` | Se tomó el `Nodo` tal cual |
| `estructuras/pila.py` | `Clase/semana_08/pila.py`, clase `PilaEnlazada` | Se conservó el diseño y los nombres. Se quitó `PilaArreglo` porque usa `list` |
| `dominio/historial.py` | `Clase/semana_08/historial.py` | Se conservó el diseño de dos pilas. Se agregaron docstrings con complejidad |

Lo propio de este proyecto es que cada acción del jugador se guarda con sus efectos, como el objeto recogido (CA-09), y la integración con el mapa y el inventario.

## Integración con el dominio

`dominio/historial.py` usa dos instancias de `PilaEnlazada`. Cada acción del jugador se registra al final de su turno junto con sus efectos.

## Historial de cambios

| Versión | Fecha | Cambio | Motivo |
|---|---|---|---|
| 1.0 | 2026-10-06 | Versión inicial | Entrega 1 |
| 1.1 | 2026-10-06 | La pila pasa a ser `PilaEnlazada` de Clase. Se agrega la sección de código reutilizado | Usar el diseño del laboratorio de la semana 8 y dejarlo declarado |
