# Análisis de complejidad

Versión final. Entrega final. n es la cantidad de elementos; f y c son las filas y columnas del mapa.

## Tabla de complejidad

| Estructura | Operación | Complejidad |
|---|---|---|
| PilaEnlazada | push, pop, peek | O(1) |
| PilaEnlazada | esta_vacia, tamaño | O(1) |
| Historial | registrar, deshacer, rehacer | O(1) |
| Historial | puede_deshacer, puede_rehacer | O(1) |
| ListaEnlazada | insertar(0), insertar(tamaño) | O(1) |
| ListaEnlazada | insertar(i) en medio | O(n) |
| ListaEnlazada | eliminar(0) | O(1) |
| ListaEnlazada | eliminar(i) | O(n) |
| ListaEnlazada | obtener, buscar, recorrer | O(n) |
| ListaEnlazada | tamaño | O(1) |
| Inventario | agregar | O(1) |
| Inventario | quitar, listar | O(n) |
| Inventario | esta_vacio | O(1) |
| ColaEnlazada | encolar, desencolar, frente | O(1) |
| ColaEnlazada | esta_vacia, tamaño | O(1) |
| Eventos | registrar, hay_eventos | O(1) |
| Eventos | sacar_todos | O(n) |
| Mapa | crear | O(f·c) |
| Mapa | en_rango, poner_obstaculo, es_obstaculo | O(1) |
| Mapa | poner_objeto, objeto_en, quitar_objeto | O(1) |
| ListaCircular | agregar, actual, avanzar, esta_vacia | O(1) |
| Rutas (BFS) | siguiente_paso | O(V + E) = O(f·c) |

## Justificación por estructura

**Dos pilas (historial).** Deshacer y rehacer siempre trabajan con la acción más reciente, y eso es justo lo que hace una pila: el último en entrar es el primero en salir. Todas las operaciones son O(1). La alternativa era una lista doble con un cursor, que también es O(1), pero obliga a mover el cursor y cortar la lista cada vez que llega una acción nueva. Con dos pilas basta con crear una pila vacía de deshechas.

**Lista enlazada simple (inventario).** Recoger objetos es lo que más pasa, y agregar al inicio cuesta O(1). El jugador pide los objetos por nombre, no por posición, así que no se pierde nada al no tener acceso directo. Usar y soltar cuestan O(n) porque hay que buscar el objeto, pero en un arreglo dinámico también habría que buscar y además correr los elementos siguientes. La misma lista guarda las posiciones de los monstruos.

**Cola enlazada (eventos).** Los eventos se deben mostrar en el orden en que ocurrieron: el primero en entrar es el primero en salir. Encolar y desencolar son O(1). Se descartó la cola de prioridad porque insertar cuesta O(log n) y ningún evento es más urgente que otro.

**Lista circular (turnos).** Los turnos giran sin fin: jugador, monstruo, monstruo, jugador. En la lista circular el último nodo apunta al primero, así que pasar el turno es una sola operación O(1). La alternativa era una cola, que en cada turno obliga a desencolar y volver a encolar.

**Grafo implícito con BFS (rutas).** No se guarda una lista de aristas: los vecinos de una celda se calculan al momento (4 direcciones sin obstáculo). BFS revisa las celdas por capas de distancia, así que el primer camino que encuentra tiene la menor cantidad de pasos. Usa la misma cola de los eventos. Se descartó DFS porque no garantiza el camino más corto.

**Matriz densa (mapa).** Cada movimiento consulta una celda por fila y columna, y en una matriz eso es O(1). El mapa es de 20x20 y como máximo el 25 % son obstáculos, así que una matriz dispersa ahorraría poca memoria y haría la consulta más lenta.

## Costo de las acciones de la partida

| Acción | Complejidad | Por qué |
|---|---|---|
| mover, esperar | O(m · f·c) | después de actuar, cada uno de los m monstruos hace un BFS |
| soltar, usar | O(n) | busca el objeto en el inventario |
| deshacer, rehacer | O(n) | O(1) en el historial, más el costo de revertir sobre el inventario |
| revisar victoria | O(f·c) | busca tesoros en todo el mapa |
| revisar derrota | O(m) | revisa la posición de cada monstruo |
| pelear | O(n + f·c) | quita la espada del inventario y busca una celda libre al azar |
| crear partida | O(f·c) | crea el mapa celda por celda |

## Comparación de decisiones contra su alternativa

### 1. Deshacer y rehacer: dos pilas contra lista doble con cursor

| Operación | Dos pilas | Lista doble con cursor |
|---|---|---|
| registrar acción nueva | O(1): push y crear una pila vacía | O(1): insertar después del cursor y cortar lo que sigue |
| deshacer | O(1): pop de hechas, push en deshechas | O(1): mover el cursor atrás |
| rehacer | O(1): pop de deshechas, push en hechas | O(1): mover el cursor adelante |
| casos que cuidar | pila vacía | cursor al inicio, al final, y cortar la lista sin perder enlaces |

Las dos tienen el mismo costo. Se eligieron las dos pilas porque el código es más corto y cada operación es un push o un pop. Con la lista doble hay que mantener el cursor y los enlaces en ambos sentidos.

### 2. Inventario: lista enlazada simple contra arreglo dinámico

| Operación | Lista enlazada | Arreglo dinámico |
|---|---|---|
| recoger (agregar) | O(1) al inicio | O(1) amortizado al final |
| usar o soltar (quitar por nombre) | O(n): buscar + cambiar un enlace | O(n): buscar + correr los elementos siguientes |
| listar | O(n) | O(n) |
| acceso por posición | O(n) | O(1) |

El juego nunca pide un objeto por posición, así que la ventaja del arreglo no se aprovecha. Al quitar, la lista solo cambia un enlace, mientras el arreglo tiene que mover los elementos. Por eso se eligió la lista.

### 3. Rutas: BFS contra DFS

| | BFS | DFS |
|---|---|---|
| costo | O(V + E) | O(V + E) |
| estructura auxiliar | cola | pila |
| camino encontrado | siempre uno de menos pasos | cualquiera, puede dar muchas vueltas |

Cuestan lo mismo, pero solo BFS cumple CA-13: el monstruo debe avanzar por una ruta de menos pasos.
