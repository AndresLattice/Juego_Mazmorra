"""Mapa de la mazmorra como matriz densa.

Cada celda guarda uno de tres valores:
    None      celda libre
    "#"       obstáculo
    un texto  nombre del objeto que hay en la celda
"""

OBSTACULO = "#"


class Mapa:
    """Rejilla de filas x columnas guardada como una lista de filas.

    Complejidad: crear O(f·c); en_rango, poner_obstaculo, es_obstaculo,
    poner_objeto, objeto_en y quitar_objeto O(1).
    """

    def __init__(self, filas, columnas):
        """Crea un mapa con todas las celdas libres. O(f·c)."""
        if filas < 1 or columnas < 1:
            raise ValueError("el mapa necesita al menos una fila y una columna")
        self.filas = filas
        self.columnas = columnas
        self._celdas = []
        for _ in range(filas):
            fila = []
            for _ in range(columnas):
                fila.append(None)
            self._celdas.append(fila)

    def en_rango(self, fila, columna):
        """Indica si la celda existe. O(1)."""
        return 0 <= fila < self.filas and 0 <= columna < self.columnas

    def poner_obstaculo(self, fila, columna):
        """Pone un obstáculo en la celda. O(1)."""
        self._validar(fila, columna)
        self._celdas[fila][columna] = OBSTACULO

    def es_obstaculo(self, fila, columna):
        """Indica si la celda tiene obstáculo. O(1)."""
        self._validar(fila, columna)
        return self._celdas[fila][columna] == OBSTACULO

    def poner_objeto(self, fila, columna, objeto):
        """Deja un objeto en la celda. O(1)."""
        self._validar(fila, columna)
        self._celdas[fila][columna] = objeto

    def objeto_en(self, fila, columna):
        """Devuelve el objeto de la celda, o None si no hay. O(1)."""
        self._validar(fila, columna)
        valor = self._celdas[fila][columna]
        if valor == OBSTACULO:
            return None
        return valor

    def quitar_objeto(self, fila, columna):
        """Quita el objeto de la celda y lo devuelve. None si no había. O(1)."""
        objeto = self.objeto_en(fila, columna)
        if objeto is not None:
            self._celdas[fila][columna] = None
        return objeto

    def _validar(self, fila, columna):
        if not self.en_rango(fila, columna):
            raise IndexError("la celda no existe en el mapa")
