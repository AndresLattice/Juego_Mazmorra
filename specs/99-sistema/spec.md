# Spec del sistema (versión inicial)

## Qué hace

Un juego por turnos en consola sobre una rejilla de al menos 20x20. Un aventurero recoge tesoros en una mazmorra mientras al menos 2 monstruos lo persiguen. El jugador puede deshacer y rehacer sus jugadas. Los eventos de cada turno se muestran en orden. La partida termina con victoria o derrota.

## Componentes previstos

| Componente | Estructura | Historias |
|---|---|---|
| 01-historial | Dos pilas | HU-04 |
| 02-mapa | Matriz densa | HU-01, HU-02 |
| 03-inventario | Lista enlazada simple | HU-03 |
| 04-eventos | Cola | HU-06 |
| 05-turnos | Lista circular, también para el banco de preguntas | HU-05, HU-10 |
| 06-rutas | Grafo implícito con BFS | HU-05 |
| 07-montículo | Montículo máximo | HU-08 y A* de HU-09 |
| 08-indice | Tabla hash | HU-08 |

## Cómo encajan los contratos

- El turno recorre la lista circular de entidades.
- La acción del jugador se registra en el historial con sus efectos.
- Cada monstruo pide una ruta al componente de rutas y avanza una casilla.
- Todo cambio genera un evento en la cola.
- Si un monstruo alcanza al jugador, se abre una pantalla de combate en la consola con una pregunta del banco. Acertar elimina al monstruo y fallar resta un porcentaje de vida (HU-10).
- Al final del turno se evalúa victoria o derrota.

## Código reutilizado

Parte de las estructuras se adapta de los laboratorios de la carpeta `Clase` (semanas 5 a 9). La tabla completa está en `specs/00-producto/estructuras.md` y el detalle de cada componente en su `plan.md`.

## Fuera de alcance

Interfaz gráfica, guardado de partidas y monstruos con comportamientos distintos.

## Historial de cambios

| Versión | Fecha | Cambio | Motivo |
|---|---|---|---|
| 0.1 | 2026-10-06 | Versión inicial | Entrega 1 |
