import pytest

from estructuras.pila import Pila


def test_desapilar_vacia_falla():
    """Verifica CA-11: operar sobre una pila vacía falla sin corromper el estado."""
    p = Pila()
    with pytest.raises(IndexError):
        p.desapilar()
    assert p.esta_vacia()


def test_ver_tope_vacia_falla():
    """Verifica CA-11: ver el tope de una pila vacía falla de forma controlada."""
    with pytest.raises(IndexError):
        Pila().ver_tope()


def test_un_elemento():
    """Verifica CA-12: lo apilado es lo que se desapila."""
    p = Pila()
    p.apilar("a")
    assert p.desapilar() == "a"
    assert p.esta_vacia()


def test_ver_tope_no_quita():
    """Verifica CA-08: ver el tope devuelve la acción más reciente sin quitarla."""
    p = Pila()
    p.apilar(1)
    p.apilar(2)
    assert p.ver_tope() == 2
    assert len(p) == 2


def test_orden_lifo():
    """Verifica CA-08: sale primero lo más reciente."""
    p = Pila()
    p.apilar(1)
    p.apilar(2)
    p.apilar(3)
    assert [p.desapilar(), p.desapilar(), p.desapilar()] == [3, 2, 1]


def test_vaciar():
    """Verifica CA-10: vaciar elimina todo lo rehacible."""
    p = Pila()
    p.apilar(1)
    p.apilar(2)
    p.vaciar()
    assert len(p) == 0
    assert p.esta_vacia()


def test_vaciar_pila_vacia():
    """Verifica CA-10: vaciar una pila vacía no falla."""
    p = Pila()
    p.vaciar()
    assert p.esta_vacia()


def test_longitud_sigue_los_cambios():
    """Verifica CA-08: el tamaño refleja apilar y desapilar."""
    p = Pila()
    assert len(p) == 0
    p.apilar("x")
    assert len(p) == 1
    p.desapilar()
    assert len(p) == 0


def test_esta_vacia_cambia():
    """Verifica CA-11: esta_vacia distingue pila vacía y con elementos."""
    p = Pila()
    assert p.esta_vacia()
    p.apilar(1)
    assert not p.esta_vacia()
