"""Cola enlazada. Soporta el componente eventos.

Origen: adaptado de Clase/semana_09/cola.py, clase ColaEnlazada (laboratorio
de la semana 9). Se conserva el diseño y los nombres de las operaciones.
Cambios respecto a Clase: se eliminó ColaCircular, que usa `list` como
estructura principal, y el nodo se importa desde estructuras/nodo.py.
"""

from estructuras.nodo import Nodo


class ColaVaciaError(IndexError):
    """Se intentó operar sobre una cola vacía."""


class ColaEnlazada:
    """Cola FIFO sobre nodos. Desencola por la cabeza, encola por la cola.

    Invariantes de representación:
        IR-01: _cabeza is None  <=>  _cola is None  <=>  _tamaño == 0
        IR-02: _cola.siguiente is None siempre

    Complejidad: encolar O(1), desencolar O(1), frente O(1),
    esta_vacia O(1), tamaño O(1)
    """

    def __init__(self):
        self._cabeza = None
        self._cola = None
        self._tamaño = 0

    def esta_vacia(self):
        """Indica si no hay elementos. O(1)."""
        return self._cabeza is None

    def tamaño(self):
        """Cantidad de elementos. O(1)."""
        return self._tamaño

    def encolar(self, elemento):
        """Agrega el elemento al final. O(1)."""
        nuevo = Nodo(elemento)
        if self._cola is None:
            self._cabeza = nuevo
        else:
            self._cola.siguiente = nuevo
        self._cola = nuevo
        self._tamaño += 1

    def desencolar(self):
        """Quita y devuelve el elemento del frente. O(1).

        Lanza ColaVaciaError si la cola está vacía.
        """
        if self.esta_vacia():
            raise ColaVaciaError("desencolar sobre cola vacía")
        nodo = self._cabeza
        self._cabeza = nodo.siguiente
        if self._cabeza is None:
            self._cola = None
        self._tamaño -= 1
        return nodo.dato

    def frente(self):
        """Devuelve el elemento del frente sin quitarlo. O(1).

        Lanza ColaVaciaError si la cola está vacía.
        """
        if self.esta_vacia():
            raise ColaVaciaError("frente sobre cola vacía")
        return self._cabeza.dato

    def __len__(self):
        return self._tamaño
