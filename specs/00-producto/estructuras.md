# Decisión de estructuras

Versión 1.2.

| Capacidad | Estructura | Por qué esta y operación dominante | Alternativa descartada y motivo | Complejidad clave |
|---|---|---|---|---|
| Inventario del jugador | Lista enlazada simple | Recoger (agregar al inicio) es lo más frecuente; no se necesita acceso por índice | Arreglo dinámico: quitar en medio desplaza elementos | O(1) agregar, O(n) quitar y listar |
| Orden de los turnos | Lista circular | Pasar al siguiente en ciclo sin fin | Cola: sacar y reinsertar en cada turno | O(1) avanzar |
| Deshacer y rehacer | Dos pilas | Siempre se opera sobre lo más reciente | Lista doble con cursor: hay que cortarla en cada acción nueva | O(1) |
| Eventos del juego | Cola | El orden de llegada es el requisito | Cola de prioridad: no hay eventos más urgentes | O(1) |
| Ruta de los monstruos | Grafo implícito con BFS | BFS da el camino con menos pasos usando la cola | DFS: no garantiza el camino más corto | O(V + E) |
| Representación del mapa | Matriz densa (arreglo 2D) | Consultar una celda por coordenadas | Matriz dispersa: con 20x20 y hasta 25 % ocupado ahorra poco | O(1) consultar |

## Capacidades que salieron

| Capacidad | Estructura prevista | Motivo |
|---|---|---|
| Índice de entidades | Tabla hash | Solo la usaba HU-08, que pasó a Won't |
| Puntajes | Montículo máximo | Solo lo usaban HU-08 y HU-09, que pasaron a Won't |

## Notas

- BFS usa la misma cola de los eventos (`estructuras/cola.py`).
- La lista enlazada también guarda a los monstruos de la partida.
- Soporte interno: el mapa y las matrices `visitado` y `padre` de BFS usan `list` de filas de tamaño fijo. Se justifica en `02-mapa/plan.md` y `06-rutas/plan.md`.

## Código de Clase que se reutiliza

Los laboratorios del curso (carpeta `Clase`) ya traen implementaciones de varias estructuras. Se parte de ellas y se adaptan. Cada componente declara su origen en su `plan.md`.

| Capacidad | Origen en Clase | Estado |
|---|---|---|
| Deshacer y rehacer | `semana_08/pila.py` (`PilaEnlazada`) y `semana_08/historial.py` | Reutilizado |
| Nodo de las estructuras enlazadas | `semana_05/nodo.py` | Reutilizado |
| Inventario | `semana_06/lista_enlazada.py` | Reutilizado |
| Orden de los turnos | `semana_07/lista_circular.py` | Reutilizado |
| Eventos y BFS | `semana_09/cola.py` (`ColaEnlazada`) | Reutilizado |
| Mapa | Propio | Sin reutilizar |
| Rutas (BFS) | Propio | Sin reutilizar |

Regla: `list` solo se acepta como soporte interno y se justifica en el `plan.md` del componente.

## Historial de cambios

| Versión | Fecha | Cambio | Motivo |
|---|---|---|---|
| 1.0 | 2026-10-06 | Versión inicial | Entrega 1 |
| 1.1 | 2026-10-06 | Se agrega la tabla de código reutilizado de Clase | Dejar declarado qué viene de los laboratorios |
| 1.2 | 2026-11-09 | Salen la tabla hash y el montículo. La ruta queda solo con BFS. Se actualiza el estado del código reutilizado | HU-08, HU-09 y HU-10 pasaron a Won't (ver `moscow.md` 1.2) |
