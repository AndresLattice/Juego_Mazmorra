import pytest

from dominio.historial import Historial
from estructuras.pila import PilaVaciaError


# ---------- registrar ----------

def test_registrar_queda_como_la_mas_reciente():
    """Verifica CA-08: la acción registrada es la primera en deshacerse."""
    h = Historial()
    h.registrar("mover")
    h.registrar("recoger")
    assert h.deshacer() == "recoger"


def test_accion_nueva_vacia_rehacer():
    """Verifica CA-10: registrar una acción nueva elimina lo rehacible."""
    h = Historial()
    h.registrar("A")
    h.registrar("B")
    h.deshacer()
    assert h.puede_rehacer()
    h.registrar("C")
    assert not h.puede_rehacer()


def test_registrar_en_historial_vacio():
    """Verifica CA-08: se puede registrar en un historial vacío."""
    h = Historial()
    h.registrar("A")
    assert h.puede_deshacer()


# ---------- deshacer ----------

def test_deshacer_devuelve_ultima():
    """Verifica CA-08: deshacer devuelve la última acción registrada."""
    h = Historial()
    h.registrar("A")
    h.registrar("B")
    assert h.deshacer() == "B"
    assert h.deshacer() == "A"


def test_deshacer_conserva_efectos():
    """Verifica CA-09: la acción devuelta conserva sus efectos."""
    h = Historial()
    accion = {"tipo": "recoger", "objeto": "llave", "posicion": (3, 4)}
    h.registrar(accion)
    assert h.deshacer() is accion


def test_deshacer_sin_historial():
    """Verifica CA-11: deshacer sin historial lanza PilaVaciaError."""
    with pytest.raises(PilaVaciaError):
        Historial().deshacer()


def test_deshacer_mas_veces_que_acciones():
    """Verifica CA-11: deshacer de más falla sin romper el historial."""
    h = Historial()
    h.registrar("A")
    h.deshacer()
    with pytest.raises(PilaVaciaError):
        h.deshacer()
    assert h.puede_rehacer()


# ---------- rehacer ----------

def test_rehacer_devuelve_deshecha():
    """Verifica CA-12: rehacer devuelve la misma acción que se deshizo."""
    h = Historial()
    h.registrar("escribir B")
    assert h.deshacer() == "escribir B"
    assert h.rehacer() == "escribir B"


def test_rehacer_sin_deshacer():
    """Verifica CA-12: rehacer sin nada deshecho lanza PilaVaciaError."""
    h = Historial()
    h.registrar("A")
    with pytest.raises(PilaVaciaError):
        h.rehacer()


def test_rehacer_tras_accion_nueva():
    """Verifica CA-10: tras una acción nueva no hay nada que rehacer."""
    h = Historial()
    h.registrar("A")
    h.deshacer()
    h.registrar("B")
    with pytest.raises(PilaVaciaError):
        h.rehacer()


# ---------- puede_deshacer ----------

def test_puede_deshacer_historial_vacio():
    """Verifica CA-11: un historial nuevo no puede deshacer."""
    assert not Historial().puede_deshacer()


def test_puede_deshacer_con_accion():
    """Verifica CA-08: con una acción registrada se puede deshacer."""
    h = Historial()
    h.registrar("A")
    assert h.puede_deshacer()


def test_puede_deshacer_tras_deshacer_todo():
    """Verifica CA-11: al deshacer todo ya no se puede deshacer."""
    h = Historial()
    h.registrar("A")
    h.deshacer()
    assert not h.puede_deshacer()


# ---------- puede_rehacer ----------

def test_puede_rehacer_historial_nuevo():
    """Verifica CA-12: un historial nuevo no puede rehacer."""
    assert not Historial().puede_rehacer()


def test_puede_rehacer_tras_deshacer():
    """Verifica CA-12: tras deshacer se puede rehacer."""
    h = Historial()
    h.registrar("A")
    h.deshacer()
    assert h.puede_rehacer()


def test_puede_rehacer_tras_rehacer_todo():
    """Verifica CA-12: al rehacer todo ya no queda nada por rehacer."""
    h = Historial()
    h.registrar("A")
    h.deshacer()
    h.rehacer()
    assert not h.puede_rehacer()
