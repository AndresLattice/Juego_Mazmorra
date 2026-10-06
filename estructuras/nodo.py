"""Nodo simple: un dato y una referencia al siguiente.

Origen: adaptado de Clase/semana_05/nodo.py (laboratorio de la semana 5).
Se reutiliza para las estructuras enlazadas del proyecto.
"""


class Nodo:
    """Un eslabón de una cadena: un dato y una referencia al siguiente.

    `siguiente` es None cuando este nodo es el último de la cadena.
    """

    def __init__(self, dato, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente

    def __repr__(self):
        return f"Nodo({self.dato!r})"
