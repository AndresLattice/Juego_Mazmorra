# Resumen de cambios y decisiones

Vista general para la sustentación. El detalle de cada punto está en el archivo que se indica.

## Lo que se omitió

| Qué | Motivo | Detalle |
|---|---|---|
| HU-08 Buscar entidad y puntajes | Era Should. El tiempo alcanzó para los Must completos y probados | `specs/00-producto/moscow.md` |
| HU-09 Persecución con A* | Era Should. BFS ya da el camino más corto en 20x20 | `moscow.md` |
| HU-10 Combate con pregunta | Era Should. Sin él, la colisión es derrota directa | `moscow.md` |
| HU-11 Mapa con colores | Era Could | `moscow.md` |
| Tabla hash (índice de entidades) | Solo la usaba HU-08 | `specs/00-producto/estructuras.md` |
| Montículo (puntajes y A*) | Solo lo usaban HU-08 y HU-09 | `estructuras.md` |
| Interfaz gráfica, guardar partidas, monstruos distintos | Won't desde la Entrega 1 | `moscow.md` |

## Versiones de cada archivo

| Archivo | Versión | Qué cambió y por qué |
|---|---|---|
| `00-producto/historias.md` | 1.1 | Se agrega historial de cambios |
| | 1.2 | HU-08, 09 y 10 marcadas Won't. CA-18 queda como derrota directa |
| `00-producto/moscow.md` | 1.1 | Avance de la Entrega 2. HU-06 se construyó antes que HU-05 para tener la cola lista para BFS |
| | 1.2 | HU-08, 09 y 10 pasan de Should a Won't |
| `00-producto/estructuras.md` | 1.1 | Tabla de código reutilizado de Clase |
| | 1.2 | Salen tabla hash y montículo. La ruta queda solo con BFS |
| `01-historial/spec.md` | 1.1 | Nombres y `PilaVaciaError` alineados con el laboratorio de la semana 8 |
| | 1.2 | CA-11: deshacer sin historial avisa sin error. La 1.1 contradecía la historia |
| `01-historial/plan.md` | 1.1 | La pila pasa a ser `PilaEnlazada` de Clase |
| `02-mapa/spec.md` y `plan.md` | 1.1 | Se agrega `objeto_en`, que la consola necesita para dibujar |
| `03-inventario/plan.md` | 1.1 | Se declara lo que se quitó de la lista de Clase |
| `07-partida/spec.md` | 1.0 | La partida existía desde la Entrega 2 sin spec propia |
| `99-sistema/spec.md` | 0.2 | Estado de la Entrega 2 |
| `trazabilidad.md` | 2.0 | Trazabilidad en ambos sentidos |

## Decisiones de diseño que te pueden preguntar

| Decisión | Por qué | Dónde |
|---|---|---|
| Deshacer y rehacer no mueven a los monstruos | El historial guarda solo acciones del jugador | `07-partida/spec.md` |
| Chocar con un muro no gasta el turno | La acción no se hizo | `07-partida/plan.md` |
| Si ganas y te alcanzan en el mismo turno, ganas | El jugador actúa primero | `07-partida/spec.md` |
| Pisar a un monstruo es derrota | Un monstruo no es obstáculo; la colisión termina la partida | `07-partida/spec.md` |
| Un monstruo no entra a la celda de otro | Evita que dos monstruos queden en la misma celda | `07-partida/plan.md` |
| BFS no esquiva a otros monstruos al calcular la ruta | Mantiene el BFS simple | `06-rutas/spec.md` |
| La matriz del mapa usa `list` de filas | Arreglo de tamaño fijo, nunca crece | `02-mapa/plan.md` |
| Cada objeto y cada evento es un texto | Es lo más simple que cumple las historias | `03-inventario/spec.md`, `04-eventos/spec.md` |
| La victoria revisa todo el mapa cada turno | O(f·c) con 400 celdas es barato y más simple que un contador | `07-partida/plan.md` |

## Código tomado de Clase

| Archivo | Origen | Qué se cambió |
|---|---|---|
| `estructuras/nodo.py` | semana 5 | Nada |
| `estructuras/pila.py` | semana 8 | Se quitó `PilaArreglo` porque usa `list` |
| `dominio/historial.py` | semana 8 | Docstrings con complejidad |
| `estructuras/lista_enlazada.py` | semana 6 | Se completaron `_insertar_en_medio` y `_eliminar_no_primero`. Se quitaron `__getitem__` y `__repr__` |
| `estructuras/lista_circular.py` | semana 7 | Se quitaron `eliminar_actual`, `rotar` y `__iter__` |
| `estructuras/cola.py` | semana 9 | Se quitó `ColaCircular` porque usa `list` |

Propios del proyecto: `dominio/mapa.py`, `dominio/rutas.py`, `dominio/inventario.py`, `dominio/eventos.py`, `dominio/partida.py` y `main.py`.
