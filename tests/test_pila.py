import pytest

from estructuras.pila import PilaEnlazada, PilaVaciaError


# ---------- push ----------

def test_push_aumenta_tamaño():
    """Verifica CA-08: cada push agrega una acción más a la pila."""
    p = PilaEnlazada()
    p.push("a")
    p.push("b")
    assert p.tamaño() == 2


def test_push_un_elemento_queda_en_tope():
    """Verifica CA-12: lo que entra queda en el tope."""
    p = PilaEnlazada()
    p.push("x")
    assert p.peek() == "x"


def test_push_acepta_cualquier_objeto():
    """Verifica CA-09: la pila guarda objetos completos, con sus efectos."""
    p = PilaEnlazada()
    accion = {"tipo": "recoger", "objeto": "llave"}
    p.push(accion)
    assert p.pop() is accion


# ---------- pop ----------

def test_pop_vacia_falla():
    """Verifica CA-11: pop sobre pila vacía lanza PilaVaciaError."""
    with pytest.raises(PilaVaciaError):
        PilaEnlazada().pop()


def test_pop_un_elemento():
    """Verifica CA-12: push seguido de pop devuelve el mismo elemento."""
    p = PilaEnlazada()
    p.push("x")
    assert p.pop() == "x"
    assert p.esta_vacia()


def test_pop_orden_lifo():
    """Verifica CA-08: sale primero lo más reciente."""
    p = PilaEnlazada()
    for v in [1, 2, 3]:
        p.push(v)
    assert [p.pop(), p.pop(), p.pop()] == [3, 2, 1]


# ---------- peek ----------

def test_peek_vacia_falla():
    """Verifica CA-11: peek sobre pila vacía lanza PilaVaciaError."""
    with pytest.raises(PilaVaciaError):
        PilaEnlazada().peek()


def test_peek_no_modifica():
    """Verifica CA-08: peek no cambia el tamaño ni el tope."""
    p = PilaEnlazada()
    p.push("a")
    assert p.peek() == "a"
    assert p.peek() == "a"
    assert p.tamaño() == 1


def test_peek_devuelve_el_ultimo():
    """Verifica CA-08: el tope es la acción más reciente."""
    p = PilaEnlazada()
    p.push(1)
    p.push(2)
    assert p.peek() == 2


# ---------- esta_vacia ----------

def test_esta_vacia_pila_nueva():
    """Verifica CA-11: una pila nueva está vacía."""
    assert PilaEnlazada().esta_vacia()


def test_esta_vacia_con_elementos():
    """Verifica CA-08: con elementos ya no está vacía."""
    p = PilaEnlazada()
    p.push(1)
    assert not p.esta_vacia()


def test_esta_vacia_tras_sacar_todo():
    """Verifica CA-12: al sacar el último elemento vuelve a estar vacía."""
    p = PilaEnlazada()
    p.push(1)
    p.pop()
    assert p.esta_vacia()


# ---------- tamaño ----------

def test_tamaño_pila_nueva():
    """Verifica CA-11: una pila nueva tiene tamaño 0."""
    assert PilaEnlazada().tamaño() == 0


def test_tamaño_sigue_los_push_y_pop():
    """Verifica CA-08: el tamaño sube con push y baja con pop."""
    p = PilaEnlazada()
    p.push("x")
    assert p.tamaño() == 1
    p.pop()
    assert p.tamaño() == 0


def test_tamaño_no_baja_de_cero_tras_error():
    """Verifica CA-11: un pop fallido no deja un tamaño negativo."""
    p = PilaEnlazada()
    with pytest.raises(PilaVaciaError):
        p.pop()
    assert p.tamaño() == 0
