# Plan: Turnos

Versión 1.0.

## Estructura elegida

Lista circular simple, `ListaCircular` en `estructuras/lista_circular.py`. La partida guarda en ella al jugador y a cada monstruo.

## Por qué esta estructura

- Los turnos no tienen fin: después del último vuelve el primero. En la lista circular el último nodo apunta al primero, así que pasar el turno siempre es `actual = actual.siguiente`.
- Avanzar es O(1).

## Complejidad

| Operación | Costo |
|---|---|
| agregar | O(1) |
| actual | O(1) |
| avanzar | O(1) |
| esta_vacia | O(1) |

## Alternativa descartada

Cola: también sirve, pero cada turno hay que desencolar y volver a encolar. Son dos operaciones para lo que en la lista circular es una.

## Soporte interno

Ninguno. Usa los nodos de `estructuras/nodo.py`.

## Código reutilizado de Clase

| Archivo del proyecto | Origen en Clase | Qué se hizo |
|---|---|---|
| `estructuras/lista_circular.py` | `Clase/semana_07/lista_circular.py` | Se conservan el diseño y los nombres. Se quitan `eliminar_actual`, `rotar` y `__iter__`, que el proyecto no usa |

## Historial de cambios

| Versión | Fecha | Cambio | Motivo |
|---|---|---|---|
| 1.0 | 2026-11-09 | Versión inicial | Entrega final |
