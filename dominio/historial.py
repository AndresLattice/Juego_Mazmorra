"""Historial de acciones del jugador con deshacer y rehacer.

Origen: adaptado de Clase/semana_08/historial.py (laboratorio de la
semana 8). Se conserva el diseño de dos pilas. Cada acción es un objeto
que el dominio arma con sus efectos, y el historial lo guarda tal cual.
"""

from estructuras.pila import PilaEnlazada


class Historial:
    """Sistema de deshacer y rehacer con dos pilas.

    La regla que casi todos olvidan: cuando llega una acción NUEVA,
    la pila de rehacer debe vaciarse. Si no, podrías «rehacer» una
    acción que ya no tiene sentido en el nuevo estado.

    Complejidad: registrar O(1), deshacer O(1), rehacer O(1),
    puede_deshacer O(1), puede_rehacer O(1)
    """

    def __init__(self):
        self._hechas = PilaEnlazada()
        self._deshechas = PilaEnlazada()

    def registrar(self, accion):
        """Registra una acción nueva. Invalida el historial de rehacer. O(1)."""
        self._hechas.push(accion)
        self._deshechas = PilaEnlazada()

    def deshacer(self):
        """Devuelve la última acción y la mueve a la pila de rehacer. O(1).

        Lanza PilaVaciaError si no hay nada que deshacer.
        """
        accion = self._hechas.pop()
        self._deshechas.push(accion)
        return accion

    def rehacer(self):
        """Devuelve la última acción deshecha y la vuelve a registrar. O(1).

        Lanza PilaVaciaError si no hay nada que rehacer.
        """
        accion = self._deshechas.pop()
        self._hechas.push(accion)
        return accion

    def puede_deshacer(self):
        """Indica si hay al menos una acción registrada. O(1)."""
        return not self._hechas.esta_vacia()

    def puede_rehacer(self):
        """Indica si hay al menos una acción deshecha. O(1)."""
        return not self._deshechas.esta_vacia()
