"""Eventos de cada turno sobre una cola enlazada.

Cada evento es un texto, por ejemplo "Recogiste una espada".
"""

from estructuras.cola import ColaEnlazada


class Eventos:
    """Guarda los eventos del turno en orden de llegada.

    Complejidad: registrar O(1), hay_eventos O(1), sacar_todos O(n).
    """

    def __init__(self):
        self._cola = ColaEnlazada()

    def registrar(self, evento):
        """Agrega el evento al final. O(1)."""
        self._cola.encolar(evento)

    def hay_eventos(self):
        """Indica si queda algún evento. O(1)."""
        return not self._cola.esta_vacia()

    def sacar_todos(self):
        """Devuelve los eventos en orden de llegada y deja la cola vacía. O(n)."""
        eventos = []
        while not self._cola.esta_vacia():
            eventos.append(self._cola.desencolar())
        return eventos
