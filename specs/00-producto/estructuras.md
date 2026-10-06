# Decisión de estructuras

| Capacidad | Estructura | Por qué esta y operación dominante | Alternativa descartada y motivo | Complejidad clave |
|---|---|---|---|---|
| Inventario del jugador | Lista enlazada simple | Agregar y quitar al inicio, sin acceso por índice | Arreglo dinámico: quitar en medio desplaza elementos | O(1) agregar, O(n) listar |
| Orden de los turnos | Lista circular | Pasar al siguiente en ciclo sin fin | Cola: sacar y reinsertar en cada turno | O(1) |
| Deshacer y rehacer | Dos pilas | Siempre se opera sobre lo más reciente | Lista doble con cursor: hay que cortarla en cada acción nueva | O(1) |
| Eventos del juego | Cola | El orden de llegada es el requisito | Cola de prioridad: no hay eventos más urgentes | O(1) |
| Índice de entidades | Tabla hash | Buscar por identificador es la operación frecuente | BST: O(log n) y no se necesita recorrer en orden | O(1) promedio |
| Puntajes | Montículo máximo | Encontrar el máximo es lo que se repite | Tabla hash: no ordena, obligaría a recorrer todo | O(1) máximo, O(log n) insertar |
| Ruta de los monstruos | Grafo implícito con BFS, A* como mejora (HU-09) | BFS da el camino con menos pasos usando la cola. A* explora menos celdas en mapas grandes | DFS: no garantiza el camino más corto | BFS O(V + E), A* O(E log V) |
| Representación del mapa | Matriz densa (arreglo 2D) | Consultar una celda por coordenadas | Matriz dispersa: con 20x20 y hasta 25 % ocupado ahorra poco | O(1) consultar |

## Notas

- BFS usa la cola de eventos. Se reutiliza el mismo módulo.
- A* usa el montículo como cola de prioridad. Se reutiliza el mismo módulo. Entra solo si hay capacidad, según `moscow.md`.
- Heurística de A*: distancia Manhattan. Es admisible porque el movimiento es en 4 direcciones con costo 1 por casilla.
- El banco de preguntas del combate (HU-10) reutiliza la lista circular de turnos. Rota sin fin y no repite hasta agotar el banco. No agrega estructura nueva.
- Soporte interno: el montículo y la tabla hash usan un arreglo como almacenamiento. Se justifica en el `plan.md` de cada uno.

## Historial de cambios

| Versión | Fecha | Cambio | Motivo |
|---|---|---|---|
| 1.0 | 2026-10-06 | Versión inicial | Entrega 1 |
