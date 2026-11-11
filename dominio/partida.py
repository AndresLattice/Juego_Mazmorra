"""Partida: une el mapa, el jugador, el inventario, el historial y los eventos.

Las posiciones son tuplas (fila, columna).
"""

import random

from dominio.eventos import Eventos
from dominio.historial import Historial
from dominio.inventario import Inventario
from dominio.mapa import Mapa
from dominio.rutas import siguiente_paso
from estructuras.lista_circular import ListaCircular
from estructuras.lista_enlazada import ListaEnlazada
from estructuras.pila import PilaVaciaError

FILAS = 20
COLUMNAS = 20
PORCENTAJE_OBSTACULOS = 15
CANTIDAD_MONSTRUOS = 2
OBJETOS_INICIALES = ["tesoro", "tesoro", "tesoro", "espada", "poción"]

DIRECCIONES = {
    "arriba": (-1, 0),
    "abajo": (1, 0),
    "izquierda": (0, -1),
    "derecha": (0, 1),
}


class Accion:
    """Una acción del jugador con lo necesario para deshacerla.

    tipo     "mover", "soltar" o "usar"
    desde    posición antes de mover
    hasta    posición después de mover
    objeto   objeto recogido al mover, o el objeto soltado o usado
    """

    def __init__(self, tipo, desde=None, hasta=None, objeto=None):
        self.tipo = tipo
        self.desde = desde
        self.hasta = hasta
        self.objeto = objeto


class Monstruo:
    """Un monstruo con su nombre y su posición."""

    def __init__(self, nombre, posicion):
        self.nombre = nombre
        self.posicion = posicion


class Partida:
    """Estado de una partida en curso."""

    def __init__(self, semilla=None):
        """Crea el mapa y coloca jugador, monstruos y objetos. O(f·c)."""
        self._azar = random.Random(semilla)
        self.mapa = Mapa(FILAS, COLUMNAS)
        self.inventario = Inventario()
        self.historial = Historial()
        self.eventos = Eventos()
        self.monstruos = ListaEnlazada()
        self.turnos = ListaCircular()
        self.jugador = None
        self.estado = "jugando"

        cantidad = FILAS * COLUMNAS * PORCENTAJE_OBSTACULOS // 100
        for _ in range(cantidad):
            fila, columna = self._celda_libre_al_azar()
            self.mapa.poner_obstaculo(fila, columna)

        self.jugador = self._celda_libre_al_azar()
        self.turnos.agregar("jugador")

        for numero in range(1, CANTIDAD_MONSTRUOS + 1):
            monstruo = Monstruo(f"Monstruo {numero}", self._celda_libre_al_azar())
            self.agregar_monstruo(monstruo)
            self.eventos.registrar(f"Apareció {monstruo.nombre} en {monstruo.posicion}")

        for objeto in OBJETOS_INICIALES:
            fila, columna = self._celda_libre_al_azar()
            self.mapa.poner_objeto(fila, columna, objeto)

    # ---------- acciones del jugador ----------

    def mover(self, direccion):
        """Mueve al jugador una casilla. Devuelve un mensaje. O(n) por los monstruos.

        Si la celda tiene un objeto, lo recoge.
        """
        if self.estado != "jugando":
            return "La partida terminó"
        cambio_fila, cambio_columna = DIRECCIONES[direccion]
        fila = self.jugador[0] + cambio_fila
        columna = self.jugador[1] + cambio_columna

        if not self.mapa.en_rango(fila, columna):
            return "No puedes salir del mapa"
        if self.mapa.es_obstaculo(fila, columna):
            return "Hay un obstáculo"

        desde = self.jugador
        self.jugador = (fila, columna)
        objeto = self.mapa.quitar_objeto(fila, columna)
        if objeto is not None:
            self.inventario.agregar(objeto)
            self.eventos.registrar(f"Recogiste: {objeto}")
        for monstruo in self.monstruos:
            if monstruo.posicion == self.jugador:
                self.eventos.registrar(f"Chocaste con {monstruo.nombre}")
                self.pelear(monstruo)

        self.historial.registrar(Accion("mover", desde, self.jugador, objeto))
        self.terminar_turno()
        return f"Te moviste hacia {direccion}"

    def esperar(self):
        """El jugador no hace nada y los monstruos se mueven."""
        if self.estado != "jugando":
            return "La partida terminó"
        self.terminar_turno()
        return "Esperaste un turno"

    def soltar(self, objeto):
        """Deja un objeto del inventario en la celda actual. O(n)."""
        if self.estado != "jugando":
            return "La partida terminó"
        fila, columna = self.jugador
        if self.mapa.objeto_en(fila, columna) is not None:
            return "Ya hay un objeto en esta celda"
        try:
            self.inventario.quitar(objeto)
        except ValueError:
            return f"No tienes: {objeto}"
        self.mapa.poner_objeto(fila, columna, objeto)
        self.historial.registrar(Accion("soltar", objeto=objeto))
        self.terminar_turno()
        return f"Soltaste: {objeto}"

    def usar(self, objeto):
        """Usa un objeto del inventario y lo consume. O(n)."""
        if self.estado != "jugando":
            return "La partida terminó"
        try:
            self.inventario.quitar(objeto)
        except ValueError:
            return f"No tienes: {objeto}"
        self.historial.registrar(Accion("usar", objeto=objeto))
        self.terminar_turno()
        return f"Usaste: {objeto}"

    # ---------- fin del turno ----------

    def terminar_turno(self):
        """Revisa el fin de la partida y, si sigue, mueve a los monstruos."""
        self.revisar_fin()
        if self.estado == "jugando":
            self.mover_monstruos()
            self.revisar_fin()

    def revisar_fin(self):
        """Cambia el estado a victoria o derrota si corresponde. O(f·c)."""
        if not self.quedan_tesoros():
            self.estado = "victoria"
            self.eventos.registrar("Recogiste todos los tesoros. ¡Ganaste!")
        elif self.hay_monstruo(self.jugador[0], self.jugador[1]):
            self.estado = "derrota"
            self.eventos.registrar("Un monstruo te atrapó. Perdiste")

    def quedan_tesoros(self):
        """Indica si queda algún tesoro en el mapa. O(f·c)."""
        for fila in range(self.mapa.filas):
            for columna in range(self.mapa.columnas):
                if self.mapa.objeto_en(fila, columna) == "tesoro":
                    return True
        return False

    # ---------- monstruos ----------

    def agregar_monstruo(self, monstruo):
        """Pone al monstruo en el mapa y en el orden de turnos. O(1)."""
        self.monstruos.insertar(0, monstruo)
        self.turnos.agregar(monstruo)

    def mover_monstruos(self):
        """Da un turno a cada monstruo hasta volver al jugador. O(m · f·c)."""
        monstruo = self.turnos.avanzar()
        while monstruo != "jugador":
            paso = siguiente_paso(self.mapa, monstruo.posicion, self.jugador)
            if paso is not None and not self.hay_monstruo(paso[0], paso[1]):
                monstruo.posicion = paso
                if paso == self.jugador:
                    self.eventos.registrar(f"{monstruo.nombre} te alcanzó")
                    self.pelear(monstruo)
            monstruo = self.turnos.avanzar()

    def pelear(self, monstruo):
        """Si el jugador tiene espada, el monstruo muere y reaparece. O(n + f·c).

        Si no tiene espada no pasa nada aquí: revisar_fin declara la derrota.
        """
        try:
            self.inventario.quitar("espada")
        except ValueError:
            return
        monstruo.posicion = self._celda_libre_al_azar()
        self.eventos.registrar(f"Mataste a {monstruo.nombre} con la espada")
        self.eventos.registrar(f"Apareció {monstruo.nombre} en {monstruo.posicion}")

    def hay_monstruo(self, fila, columna):
        """Indica si algún monstruo está en la celda. O(m)."""
        for monstruo in self.monstruos:
            if monstruo.posicion == (fila, columna):
                return True
        return False

    # ---------- deshacer y rehacer ----------

    def deshacer(self):
        """Revierte la última acción con sus efectos. O(n)."""
        if self.estado != "jugando":
            return "La partida terminó"
        try:
            accion = self.historial.deshacer()
        except PilaVaciaError:
            return "No hay nada que deshacer"

        if accion.tipo == "mover":
            self.jugador = accion.desde
            if accion.objeto is not None:
                self.inventario.quitar(accion.objeto)
                fila, columna = accion.hasta
                self.mapa.poner_objeto(fila, columna, accion.objeto)
        elif accion.tipo == "soltar":
            fila, columna = self.jugador
            self.mapa.quitar_objeto(fila, columna)
            self.inventario.agregar(accion.objeto)
        elif accion.tipo == "usar":
            self.inventario.agregar(accion.objeto)
        return f"Deshiciste: {accion.tipo}"

    def rehacer(self):
        """Vuelve a aplicar la última acción deshecha. O(n)."""
        if self.estado != "jugando":
            return "La partida terminó"
        try:
            accion = self.historial.rehacer()
        except PilaVaciaError:
            return "No hay nada que rehacer"

        if accion.tipo == "mover":
            self.jugador = accion.hasta
            if accion.objeto is not None:
                fila, columna = accion.hasta
                self.mapa.quitar_objeto(fila, columna)
                self.inventario.agregar(accion.objeto)
        elif accion.tipo == "soltar":
            fila, columna = self.jugador
            self.inventario.quitar(accion.objeto)
            self.mapa.poner_objeto(fila, columna, accion.objeto)
        elif accion.tipo == "usar":
            self.inventario.quitar(accion.objeto)
        return f"Rehiciste: {accion.tipo}"

    # ---------- turno ----------

    def eventos_del_turno(self):
        """Devuelve los eventos del turno en orden y los borra. O(n)."""
        if not self.eventos.hay_eventos():
            return ["Turno sin novedades"]
        return self.eventos.sacar_todos()

    # ---------- apoyo ----------

    def celda_libre(self, fila, columna):
        """Indica si la celda no tiene obstáculo, objeto, jugador ni monstruo. O(n)."""
        if self.mapa.es_obstaculo(fila, columna):
            return False
        if self.mapa.objeto_en(fila, columna) is not None:
            return False
        if self.jugador == (fila, columna):
            return False
        if self.hay_monstruo(fila, columna):
            return False
        return True

    def _celda_libre_al_azar(self):
        """Elige una celda libre al azar. Se usa solo al crear la partida."""
        while True:
            fila = self._azar.randint(0, FILAS - 1)
            columna = self._azar.randint(0, COLUMNAS - 1)
            if self.celda_libre(fila, columna):
                return (fila, columna)
