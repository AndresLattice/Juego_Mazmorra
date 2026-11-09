"""Lista circular simple. Soporta el componente turnos.

Origen: adaptado de Clase/semana_07/lista_circular.py (laboratorio de la
semana 7). Se conserva el diseño y los nombres de las operaciones.
Cambios respecto a Clase: se quitaron eliminar_actual, rotar y __iter__,
que el proyecto no usa, y el nodo se importa desde estructuras/nodo.py.
"""

from estructuras.nodo import Nodo


class ListaCircular:
    """Lista circular simple: el último nodo apunta al primero.

    Guarda una referencia al nodo ACTUAL, no a la cabeza: en una lista
    circular no hay un «primero» natural.

    Invariantes de representación:
        IR-01: lista vacía  <=>  _actual is None
        IR-02: si tiene un solo nodo, ese nodo apunta a sí mismo

    Complejidad: agregar O(1), actual O(1), avanzar O(1), esta_vacia O(1)
    """

    def __init__(self):
        self._actual = None
        self._tamaño = 0

    def esta_vacia(self):
        """Indica si no hay elementos. O(1)."""
        return self._actual is None

    def agregar(self, dato):
        """Inserta después del actual. O(1)."""
        nuevo = Nodo(dato)
        if self._actual is None:
            nuevo.siguiente = nuevo
            self._actual = nuevo
        else:
            nuevo.siguiente = self._actual.siguiente
            self._actual.siguiente = nuevo
        self._tamaño += 1

    def avanzar(self):
        """Pasa el turno al siguiente y devuelve su dato. O(1)."""
        if self._actual is None:
            raise IndexError("lista circular vacía")
        self._actual = self._actual.siguiente
        return self._actual.dato

    def actual(self):
        """Devuelve el dato del nodo actual. O(1)."""
        if self._actual is None:
            raise IndexError("lista circular vacía")
        return self._actual.dato

    def __len__(self):
        return self._tamaño
