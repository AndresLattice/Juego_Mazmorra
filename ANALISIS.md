# Análisis de complejidad

Versión 1, Entrega 2. n es la cantidad de elementos; f y c son las filas y columnas del mapa.

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

## Justificación por estructura

**Dos pilas (historial).** Deshacer y rehacer siempre trabajan con la acción más reciente, y eso es justo lo que hace una pila: el último en entrar es el primero en salir. Todas las operaciones son O(1). La alternativa era una lista doble con un cursor, que también es O(1), pero obliga a mover el cursor y cortar la lista cada vez que llega una acción nueva. Con dos pilas basta con crear una pila vacía de deshechas.

**Lista enlazada simple (inventario).** Recoger objetos es lo que más pasa, y agregar al inicio cuesta O(1). El jugador pide los objetos por nombre, no por posición, así que no se pierde nada al no tener acceso directo. Usar y soltar cuestan O(n) porque hay que buscar el objeto, pero en un arreglo dinámico también habría que buscar y además correr los elementos siguientes. La misma lista guarda las posiciones de los monstruos.

**Cola enlazada (eventos).** Los eventos se deben mostrar en el orden en que ocurrieron: el primero en entrar es el primero en salir. Encolar y desencolar son O(1). Se descartó la cola de prioridad porque insertar cuesta O(log n) y ningún evento es más urgente que otro.

**Matriz densa (mapa).** Cada movimiento consulta una celda por fila y columna, y en una matriz eso es O(1). El mapa es de 20x20 y como máximo el 25 % son obstáculos, así que una matriz dispersa ahorraría poca memoria y haría la consulta más lenta.

## Costo de las acciones de la partida

| Acción | Complejidad | Por qué |
|---|---|---|
| mover | O(m) | revisa si choca con alguno de los m monstruos |
| soltar, usar | O(n) | busca el objeto en el inventario |
| deshacer, rehacer | O(n) | O(1) en el historial, más el costo de revertir sobre el inventario |
| crear partida | O(f·c) | crea el mapa celda por celda |
