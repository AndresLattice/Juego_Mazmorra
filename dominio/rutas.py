"""Rutas de los monstruos con búsqueda en anchura (BFS).

El mapa se ve como un grafo implícito: cada celda sin obstáculo es un
vértice, y sus vecinos son las celdas de arriba, abajo, izquierda y
derecha que también están libres de obstáculos.
"""

from estructuras.cola import ColaEnlazada

MOVIMIENTOS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def siguiente_paso(mapa, desde, hasta):
    """Devuelve la celda vecina de `desde` en un camino más corto a `hasta`.

    Devuelve None si no hay camino o si `desde` es igual a `hasta`.
    Complejidad: O(V + E), con V = filas · columnas.
    """
    if desde == hasta:
        return None

    visitado = []
    padre = []
    for _ in range(mapa.filas):
        visitado.append([False] * mapa.columnas)
        padre.append([None] * mapa.columnas)

    cola = ColaEnlazada()
    cola.encolar(desde)
    visitado[desde[0]][desde[1]] = True

    while not cola.esta_vacia():
        fila, columna = cola.desencolar()
        if (fila, columna) == hasta:
            return _primer_paso(padre, desde, hasta)
        for cambio_fila, cambio_columna in MOVIMIENTOS:
            f = fila + cambio_fila
            c = columna + cambio_columna
            if mapa.en_rango(f, c) and not mapa.es_obstaculo(f, c) and not visitado[f][c]:
                visitado[f][c] = True
                padre[f][c] = (fila, columna)
                cola.encolar((f, c))
    return None


def _primer_paso(padre, desde, hasta):
    """Camina hacia atrás desde `hasta` hasta la celda cuyo padre es `desde`."""
    celda = hasta
    while padre[celda[0]][celda[1]] != desde:
        celda = padre[celda[0]][celda[1]]
    return celda
