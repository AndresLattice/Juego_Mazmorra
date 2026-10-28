import pytest

from dominio.inventario import Inventario


# ---------- agregar ----------

def test_agregar_a_inventario_vacio():
    """Soporte de CA-05: agregar un objeto lo deja en el inventario."""
    inv = Inventario()
    inv.agregar("espada")
    assert inv.listar() == ["espada"]


def test_agregar_queda_como_el_mas_reciente():
    """Soporte de CA-05: el último objeto agregado sale primero al listar."""
    inv = Inventario()
    inv.agregar("espada")
    inv.agregar("llave")
    assert inv.listar() == ["llave", "espada"]


def test_agregar_repetido():
    """Soporte de CA-05: se permiten objetos repetidos."""
    inv = Inventario()
    inv.agregar("poción")
    inv.agregar("poción")
    assert inv.listar() == ["poción", "poción"]


# ---------- quitar ----------

def test_quitar_unico_objeto():
    """Soporte de CA-07: quitar el único objeto deja el inventario vacío."""
    inv = Inventario()
    inv.agregar("espada")
    inv.quitar("espada")
    assert inv.esta_vacio()


def test_quitar_repetido_quita_solo_uno():
    """Soporte de CA-07: con dos objetos iguales, quitar saca solo uno."""
    inv = Inventario()
    inv.agregar("poción")
    inv.agregar("poción")
    inv.quitar("poción")
    assert inv.listar() == ["poción"]


def test_quitar_objeto_que_no_esta_falla():
    """Soporte de CA-07: quitar un objeto que no está da error."""
    inv = Inventario()
    with pytest.raises(ValueError):
        inv.quitar("espada")


# ---------- listar ----------

def test_listar_inventario_vacio():
    """Verifica CA-06: listar un inventario vacío no da error."""
    assert Inventario().listar() == []


def test_listar_un_objeto():
    """Soporte de CA-06: listar un inventario de un objeto."""
    inv = Inventario()
    inv.agregar("espada")
    assert inv.listar() == ["espada"]


def test_listar_tras_quitar_del_medio():
    """Soporte de CA-06: listar después de quitar un objeto del medio."""
    inv = Inventario()
    inv.agregar("a")
    inv.agregar("b")
    inv.agregar("c")
    inv.quitar("b")
    assert inv.listar() == ["c", "a"]


# ---------- esta_vacio ----------

def test_esta_vacio_nuevo():
    """Soporte de CA-06: un inventario nuevo está vacío."""
    assert Inventario().esta_vacio()


def test_no_esta_vacio_con_un_objeto():
    """Soporte de CA-06: con un objeto ya no está vacío."""
    inv = Inventario()
    inv.agregar("espada")
    assert not inv.esta_vacio()


def test_esta_vacio_tras_quitar_todo():
    """Soporte de CA-06: queda vacío al quitar todos los objetos."""
    inv = Inventario()
    inv.agregar("a")
    inv.agregar("b")
    inv.quitar("a")
    inv.quitar("b")
    assert inv.esta_vacio()
