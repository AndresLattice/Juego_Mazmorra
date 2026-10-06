"""Pila enlazada. Soporta el componente historial.

Origen: adaptado de Clase/semana_08/pila.py, clase PilaEnlazada (laboratorio
de la semana 8). Se conserva el diseño y los nombres de las operaciones.
Cambios respecto a Clase: se eliminó PilaArreglo, que usa `list` como
estructura principal, y el nodo se importa desde estructuras/nodo.py.
"""

from estructuras.nodo import Nodo


class PilaVaciaError(IndexError):
    """Se intentó operar sobre una pila vacía."""


class PilaEnlazada:
    """Pila sobre nodos enlazados. El tope es la CABEZA.

    ¿Por qué la cabeza? Porque insertar y quitar al inicio de una lista
    enlazada es O(1); al final sería O(n) por el recorrido.

    Complejidad: push O(1), pop O(1), peek O(1), esta_vacia O(1), tamaño O(1)
    """

    def __init__(self):
        self._tope = None
        self._tamaño = 0

    def push(self, elemento):
        """Agrega un elemento al tope. O(1)."""
        self._tope = Nodo(elemento, self._tope)
        self._tamaño += 1

    def pop(self):
        """Quita y devuelve el tope. Lanza PilaVaciaError si está vacía. O(1)."""
        if self.esta_vacia():
            raise PilaVaciaError("pop sobre pila vacía")
        dato = self._tope.dato
        self._tope = self._tope.siguiente
        self._tamaño -= 1
        return dato

    def peek(self):
        """Devuelve el tope sin quitarlo. Lanza PilaVaciaError si está vacía. O(1)."""
        if self.esta_vacia():
            raise PilaVaciaError("peek sobre pila vacía")
        return self._tope.dato

    def esta_vacia(self):
        """Indica si no hay elementos. O(1)."""
        return self._tope is None

    def tamaño(self):
        """Cantidad de elementos. O(1)."""
        return self._tamaño

    def __len__(self):
        return self._tamaño
