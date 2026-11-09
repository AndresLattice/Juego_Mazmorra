# Spec del sistema

Versión 1.0.

## Qué hace

Un juego por turnos en consola sobre una rejilla de 20x20. Un aventurero recoge tesoros en una mazmorra mientras 2 monstruos lo persiguen por el camino más corto. El jugador puede deshacer y rehacer sus jugadas. Los eventos de cada turno se muestran en orden. La partida termina con victoria al recoger todos los tesoros, o con derrota si un monstruo alcanza al jugador.

## Componentes

| Componente | Estructura | Archivos | Historias |
|---|---|---|---|
| 01-historial | Dos pilas | `estructuras/pila.py`, `dominio/historial.py` | HU-04 |
| 02-mapa | Matriz densa | `dominio/mapa.py` | HU-01, HU-02 |
| 03-inventario | Lista enlazada simple | `estructuras/lista_enlazada.py`, `dominio/inventario.py` | HU-03 |
| 04-eventos | Cola | `estructuras/cola.py`, `dominio/eventos.py` | HU-06 |
| 05-turnos | Lista circular | `estructuras/lista_circular.py` | HU-05 |
| 06-rutas | Grafo implícito con BFS | `dominio/rutas.py` | HU-05 |
| 07-partida | Ninguna nueva, une a las demás | `dominio/partida.py`, `main.py` | HU-01 a HU-07 |

Todas las estructuras enlazadas usan `estructuras/nodo.py`.

## Cómo encajan los contratos

Un turno, de principio a fin:

1. `main.py` lee un comando y llama a una acción de la partida (`mover`, `esperar`, `soltar`, `usar`, `deshacer` o `rehacer`).
2. La partida consulta el **mapa** (`en_rango`, `es_obstaculo`). Si la acción no se puede hacer, devuelve el motivo y el turno no pasa.
3. Si se recoge o se suelta un objeto, se usa el **inventario** (`agregar`, `quitar`) y el **mapa** (`quitar_objeto`, `poner_objeto`).
4. La acción se guarda en el **historial** (`registrar`) con sus efectos, para poder deshacerla.
5. Lo que pasó se anota en los **eventos** (`registrar`).
6. Se revisa victoria y derrota.
7. Si la partida sigue, la lista circular de **turnos** (`avanzar`) le da el turno a cada monstruo. Cada uno pide su paso a **rutas** (`siguiente_paso`), que hace BFS con la **cola**.
8. Se revisa derrota otra vez.
9. `main.py` dibuja el mapa y muestra los eventos (`sacar_todos`).

Deshacer y rehacer usan el historial y revierten los efectos sobre mapa e inventario. No mueven a los monstruos.

## Fuera de alcance

Interfaz gráfica, guardado de partidas, monstruos con comportamientos distintos, búsqueda de entidades y puntajes, A* y combate. Ver `specs/00-producto/moscow.md`.

## Historial de cambios

| Versión | Fecha | Cambio | Motivo |
|---|---|---|---|
| 0.1 | 2026-10-06 | Versión inicial | Entrega 1 |
| 0.2 | 2026-10-27 | Se agrega el estado de la Entrega 2 | Registrar qué componentes ya están integrados |
| 1.0 | 2026-11-09 | Versión final: 7 componentes, cómo encajan los contratos paso a paso | Entrega final. Salen montículo e índice (ver `estructuras.md` 1.2) |
