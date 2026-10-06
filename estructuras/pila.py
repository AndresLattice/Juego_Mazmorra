"""Pila enlazada. Soporta el componente historial."""


class _Nodo:
    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente


class Pila:
    """Pila LIFO con nodos propios."""

    def __init__(self):
        self._tope = None
        self._tamano = 0

    def apilar(self, valor):
        """Agrega al tope. O(1)."""
        self._tope = _Nodo(valor, self._tope)
        self._tamano += 1

    def desapilar(self):
        """Quita y devuelve el tope. Lanza IndexError si está vacía. O(1)."""
        if self._tope is None:
            raise IndexError("pila vacía")
        valor = self._tope.valor
        self._tope = self._tope.siguiente
        self._tamano -= 1
        return valor

    def ver_tope(self):
        """Devuelve el tope sin quitarlo. Lanza IndexError si está vacía. O(1)."""
        if self._tope is None:
            raise IndexError("pila vacía")
        return self._tope.valor

    def vaciar(self):
        """Elimina todos los elementos. O(1)."""
        self._tope = None
        self._tamano = 0

    def esta_vacia(self):
        """Indica si no hay elementos. O(1)."""
        return self._tope is None

    def __len__(self):
        """Cantidad de elementos. O(1)."""
        return self._tamano
