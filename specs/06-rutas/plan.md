# Plan: Rutas

Versión 1.0.

## Estructura elegida

Grafo implícito recorrido con búsqueda en anchura (BFS), en `dominio/rutas.py`.

- **Grafo implícito:** no se guarda una lista de aristas. Los vecinos de una celda se calculan al momento: arriba, abajo, izquierda y derecha, si están dentro del mapa y sin obstáculo.
- **BFS:** usa la `ColaEnlazada` de `estructuras/cola.py`, la misma de los eventos.

## Cómo funciona

1. Se encola la celda del monstruo y se marca como visitada.
2. Mientras la cola no esté vacía, se desencola una celda y se encolan sus vecinos no visitados. Para cada vecino se anota de qué celda vino (su padre).
3. Si se llega al jugador, se camina hacia atrás por los padres hasta la celda cuyo padre es el monstruo. Esa es el siguiente paso.
4. Si la cola se vacía sin llegar, no hay camino.

BFS revisa las celdas por capas de distancia, así que el primer camino que encuentra es uno de menos pasos.

## Complejidad

| Operación | Costo |
|---|---|
| siguiente_paso | O(V + E). Con V = f·c celdas y E ≤ 4V, queda O(f·c) |

## Alternativa descartada

- DFS: no garantiza el camino más corto.
- Guardar el grafo con listas de adyacencia: ocupa memoria extra y el mapa ya dice quién es vecino de quién.

## Soporte interno

`visitado` y `padre` son matrices del mismo tamaño que el mapa, hechas con `list` de filas como en `dominio/mapa.py`. Se crean una vez por búsqueda y no crecen.

## Historial de cambios

| Versión | Fecha | Cambio | Motivo |
|---|---|---|---|
| 1.0 | 2026-11-09 | Versión inicial | Entrega final |
