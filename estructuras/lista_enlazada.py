"""Lista enlazada simple. Soporta el componente inventario.

Origen: adaptado de Clase/semana_06/lista_enlazada.py (laboratorio de la
semana 6). Se conserva el diseño y los nombres de las operaciones.
Cambios respecto a Clase: se completaron _insertar_en_medio y
_eliminar_no_primero, el nodo se importa desde estructuras/nodo.py y se
quitaron __getitem__ y __repr__, que el proyecto no usa.
"""

from estructuras.nodo import Nodo


class PosicionInvalidaError(IndexError):
    """La posición solicitada está fuera del rango válido."""


class ListaEnlazada:
    """Lista implementada sobre nodos enlazados.

    Atributos internos:
        _cabeza  primer nodo, o None si la lista está vacía
        _cola    último nodo, o None si la lista está vacía
        _tamaño  cantidad de nodos

    Invariantes de representación:
        IR-01: _cabeza is None  <=>  _tamaño == 0  <=>  _cola is None
        IR-02: _cola.siguiente is None siempre

    Complejidad:
        insertar(0)        O(1)
        insertar(tamaño)   O(1) gracias a _cola
        insertar(i)        O(n)
        obtener(i)         O(n)
        eliminar(0)        O(1)
        eliminar(i)        O(n)
        buscar             O(n)
        tamaño             O(1)
    """

    def __init__(self):
        self._cabeza = None
        self._cola = None
        self._tamaño = 0

    def tamaño(self):
        """Cantidad de elementos. O(1)."""
        return self._tamaño

    def obtener(self, posicion):
        """Devuelve el elemento en `posicion`. O(n)."""
        self._validar(posicion, incluir_final=False)
        return self._nodo_en(posicion).dato

    def insertar(self, posicion, elemento):
        """Inserta `elemento` en `posicion`. O(1) al inicio o al final, O(n) en medio."""
        self._validar(posicion, incluir_final=True)
        if posicion == 0:
            self._insertar_al_inicio(elemento)
        elif posicion == self._tamaño:
            self._insertar_al_final(elemento)
        else:
            self._insertar_en_medio(posicion, elemento)
        self._tamaño += 1

    def eliminar(self, posicion):
        """Quita y devuelve el elemento en `posicion`. O(1) al inicio, O(n) en otro lugar."""
        self._validar(posicion, incluir_final=False)
        if posicion == 0:
            dato = self._eliminar_primero()
        else:
            dato = self._eliminar_no_primero(posicion)
        self._tamaño -= 1
        return dato

    def buscar(self, elemento):
        """Devuelve la posición de la primera aparición, o -1. O(n)."""
        actual = self._cabeza
        i = 0
        while actual is not None:
            if actual.dato == elemento:
                return i
            actual = actual.siguiente
            i += 1
        return -1

    def _insertar_al_inicio(self, elemento):
        """O(1). Si la lista estaba vacía, también hay que fijar _cola."""
        nuevo = Nodo(elemento, self._cabeza)
        self._cabeza = nuevo
        if self._cola is None:
            self._cola = nuevo

    def _insertar_al_final(self, elemento):
        """O(1) gracias a _cola."""
        nuevo = Nodo(elemento)
        if self._cola is None:
            self._cabeza = nuevo
        else:
            self._cola.siguiente = nuevo
        self._cola = nuevo

    def _insertar_en_medio(self, posicion, elemento):
        """O(n). Hay que llegar al nodo ANTERIOR a la posición."""
        anterior = self._nodo_en(posicion - 1)
        nuevo = Nodo(elemento, anterior.siguiente)
        anterior.siguiente = nuevo

    def _eliminar_primero(self):
        """O(1). Si era el único elemento, _cola también queda en None."""
        nodo = self._cabeza
        self._cabeza = nodo.siguiente
        if self._cabeza is None:
            self._cola = None
        return nodo.dato

    def _eliminar_no_primero(self, posicion):
        """O(n). Si es el último, hay que actualizar _cola."""
        anterior = self._nodo_en(posicion - 1)
        objetivo = anterior.siguiente
        anterior.siguiente = objetivo.siguiente
        if objetivo is self._cola:
            self._cola = anterior
        return objetivo.dato

    def _nodo_en(self, posicion):
        """Devuelve el nodo en `posicion`. O(n)."""
        actual = self._cabeza
        for _ in range(posicion):
            actual = actual.siguiente
        return actual

    def _validar(self, posicion, incluir_final):
        limite = self._tamaño if incluir_final else self._tamaño - 1
        if posicion < 0 or posicion > limite:
            raise PosicionInvalidaError("posición fuera de rango")

    def __len__(self):
        return self._tamaño

    def __iter__(self):
        """Recorre los elementos de la cabeza a la cola. O(n)."""
        actual = self._cabeza
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente
