# Plan: Eventos

Versión 1.0.

## Estructura elegida

Cola enlazada, `ColaEnlazada` en `estructuras/cola.py`. Los eventos se manejan en `dominio/eventos.py`.

## Por qué esta estructura

- El requisito es atender por orden de llegada: el primero en entrar es el primero en salir.
- Encolar y desencolar son O(1).
- La misma cola servirá para BFS en la persecución (HU-05).

## Complejidad

| Operación | Costo |
|---|---|
| registrar | O(1) |
| hay_eventos | O(1) |
| sacar_todos | O(n) |

## Alternativa descartada

Cola de prioridad. Insertar cuesta O(log n) y en este juego ningún evento es más urgente que otro.

## Soporte interno

Ninguno. La cola usa los nodos de `estructuras/nodo.py`.

## Código reutilizado de Clase

| Archivo del proyecto | Origen en Clase | Qué se hizo |
|---|---|---|
| `estructuras/cola.py` | `Clase/semana_09/cola.py`, clase `ColaEnlazada` | Se conservan el diseño y los nombres. Se quita `ColaCircular` porque usa `list` |

## Historial de cambios

| Versión | Fecha | Cambio | Motivo |
|---|---|---|---|
| 1.0 | 2026-10-27 | Versión inicial | Entrega 2 |
