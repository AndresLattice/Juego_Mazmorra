"""Inventario del jugador sobre una lista enlazada simple.

Cada objeto es un texto con su nombre. Los objetos nuevos entran al
inicio de la lista, así que `listar` los muestra del más reciente al
más antiguo.
"""

from estructuras.lista_enlazada import ListaEnlazada


class Inventario:
    """Objetos que carga el jugador.

    Complejidad: agregar O(1), quitar O(n), listar O(n), esta_vacio O(1).
    """

    def __init__(self):
        self._objetos = ListaEnlazada()

    def agregar(self, objeto):
        """Agrega el objeto al inicio. O(1)."""
        self._objetos.insertar(0, objeto)

    def quitar(self, objeto):
        """Quita una aparición del objeto. O(n).

        Lanza ValueError si el objeto no está en el inventario.
        """
        posicion = self._objetos.buscar(objeto)
        if posicion == -1:
            raise ValueError("el objeto no está en el inventario")
        self._objetos.eliminar(posicion)

    def listar(self):
        """Devuelve los objetos del más reciente al más antiguo. O(n)."""
        objetos = []
        for objeto in self._objetos:
            objetos.append(objeto)
        return objetos

    def esta_vacio(self):
        """Indica si no hay objetos. O(1)."""
        return self._objetos.tamaño() == 0
