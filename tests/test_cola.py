import pytest

from estructuras.cola import ColaEnlazada, ColaVaciaError


# ---------- esta_vacia ----------

def test_cola_nueva_esta_vacia():
    """Soporte de CA-16: una cola nueva está vacía."""
    assert ColaEnlazada().esta_vacia()


def test_cola_con_un_elemento_no_esta_vacia():
    """Soporte de CA-15: con un elemento ya no está vacía."""
    c = ColaEnlazada()
    c.encolar("a")
    assert not c.esta_vacia()


def test_cola_vuelve_a_estar_vacia():
    """Soporte de CA-16: al desencolar todo queda vacía."""
    c = ColaEnlazada()
    c.encolar("a")
    c.desencolar()
    assert c.esta_vacia()


# ---------- tamaño ----------

def test_tamaño_cola_vacia():
    """Soporte de CA-16: una cola nueva tiene tamaño 0."""
    assert ColaEnlazada().tamaño() == 0


def test_tamaño_tras_encolar():
    """Soporte de CA-15: encolar sube el tamaño."""
    c = ColaEnlazada()
    c.encolar("a")
    c.encolar("b")
    assert c.tamaño() == 2


def test_tamaño_tras_desencolar():
    """Soporte de CA-15: desencolar baja el tamaño."""
    c = ColaEnlazada()
    c.encolar("a")
    c.encolar("b")
    c.desencolar()
    assert c.tamaño() == 1


# ---------- encolar ----------

def test_encolar_en_vacia_fija_cabeza_y_cola():
    """Soporte de CA-15: el primer elemento es cabeza y cola a la vez."""
    c = ColaEnlazada()
    c.encolar("a")
    assert c._cabeza is c._cola


def test_encolar_no_cambia_el_frente():
    """Soporte de CA-15: encolar más elementos no cambia el frente."""
    c = ColaEnlazada()
    c.encolar("a")
    c.encolar("b")
    assert c.frente() == "a"


def test_encolar_actualiza_la_cola():
    """Soporte de CA-15: el último encolado queda al final."""
    c = ColaEnlazada()
    c.encolar("a")
    c.encolar("b")
    assert c._cola.dato == "b"
    assert c._cola.siguiente is None


# ---------- desencolar ----------

def test_desencolar_orden_fifo():
    """Soporte de CA-15: sale primero el que entró primero."""
    c = ColaEnlazada()
    c.encolar("a")
    c.encolar("b")
    c.encolar("c")
    assert c.desencolar() == "a"
    assert c.desencolar() == "b"
    assert c.desencolar() == "c"


def test_desencolar_unico_deja_cola_en_none():
    """Soporte de CA-16: desencolar el único deja cabeza y cola en None."""
    c = ColaEnlazada()
    c.encolar("a")
    c.desencolar()
    assert c._cabeza is None
    assert c._cola is None


def test_desencolar_vacia_falla():
    """Soporte de CA-16: desencolar una cola vacía da error."""
    with pytest.raises(ColaVaciaError):
        ColaEnlazada().desencolar()


# ---------- frente ----------

def test_frente_un_elemento():
    """Soporte de CA-15: el frente de una cola de uno es ese elemento."""
    c = ColaEnlazada()
    c.encolar("a")
    assert c.frente() == "a"


def test_frente_no_quita():
    """Soporte de CA-15: consultar el frente no cambia el tamaño."""
    c = ColaEnlazada()
    c.encolar("a")
    c.frente()
    assert c.tamaño() == 1


def test_frente_vacia_falla():
    """Soporte de CA-16: consultar el frente de una cola vacía da error."""
    with pytest.raises(ColaVaciaError):
        ColaEnlazada().frente()
