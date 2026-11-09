import pytest

from estructuras.lista_circular import ListaCircular


# ---------- esta_vacia ----------

def test_lista_nueva_esta_vacia():
    """Soporte de CA-13: una lista nueva no tiene turnos."""
    assert ListaCircular().esta_vacia()


def test_con_un_elemento_no_esta_vacia():
    """Soporte de CA-13: con un elemento ya no está vacía."""
    lc = ListaCircular()
    lc.agregar("jugador")
    assert not lc.esta_vacia()


def test_tamaño_crece_al_agregar():
    """Soporte de CA-13: cada elemento agregado cuenta."""
    lc = ListaCircular()
    lc.agregar("a")
    lc.agregar("b")
    assert len(lc) == 2


# ---------- agregar ----------

def test_agregar_primero_apunta_a_si_mismo():
    """Soporte de CA-13: con un solo nodo, el nodo apunta a sí mismo."""
    lc = ListaCircular()
    lc.agregar("a")
    assert lc._actual.siguiente is lc._actual


def test_agregar_no_cambia_el_actual():
    """Soporte de CA-13: agregar no le quita el turno al actual."""
    lc = ListaCircular()
    lc.agregar("a")
    lc.agregar("b")
    assert lc.actual() == "a"


def test_agregar_queda_despues_del_actual():
    """Soporte de CA-13: el elemento agregado es el siguiente en jugar."""
    lc = ListaCircular()
    lc.agregar("a")
    lc.agregar("b")
    assert lc.avanzar() == "b"


# ---------- actual ----------

def test_actual_un_elemento():
    """Soporte de CA-13: con un solo elemento, el turno es suyo."""
    lc = ListaCircular()
    lc.agregar("a")
    assert lc.actual() == "a"


def test_actual_no_avanza():
    """Soporte de CA-13: consultar el actual no pasa el turno."""
    lc = ListaCircular()
    lc.agregar("a")
    lc.agregar("b")
    lc.actual()
    assert lc.actual() == "a"


def test_actual_vacia_falla():
    """Soporte de CA-13: no hay turno en una lista vacía."""
    with pytest.raises(IndexError):
        ListaCircular().actual()


# ---------- avanzar ----------

def test_avanzar_un_elemento_vuelve_a_si_mismo():
    """Soporte de CA-13: con un solo elemento, avanzar lo deja igual."""
    lc = ListaCircular()
    lc.agregar("a")
    assert lc.avanzar() == "a"


def test_avanzar_vuelta_completa():
    """Soporte de CA-13: después de una vuelta el turno vuelve al inicio."""
    lc = ListaCircular()
    lc.agregar("a")
    lc.agregar("b")
    lc.agregar("c")
    for _ in range(3):
        lc.avanzar()
    assert lc.actual() == "a"


def test_avanzar_vacia_falla():
    """Soporte de CA-13: no se puede avanzar en una lista vacía."""
    with pytest.raises(IndexError):
        ListaCircular().avanzar()
