import pytest

from dominio.mapa import Mapa


# ---------- crear ----------

def test_crear_mapa_todo_libre():
    """Soporte de CA-03: un mapa nuevo tiene todas las celdas libres."""
    m = Mapa(3, 4)
    for f in range(3):
        for c in range(4):
            assert not m.es_obstaculo(f, c)
            assert m.objeto_en(f, c) is None


def test_crear_mapa_uno_por_uno():
    """Soporte de CA-03: el mapa más pequeño es de 1x1."""
    m = Mapa(1, 1)
    assert m.en_rango(0, 0)


def test_crear_mapa_sin_filas_falla():
    """Soporte de CA-01: no se puede crear un mapa de tamaño 0."""
    with pytest.raises(ValueError):
        Mapa(0, 5)


# ---------- en_rango ----------

def test_en_rango_esquinas():
    """Soporte de CA-04: las cuatro esquinas están dentro del mapa."""
    m = Mapa(20, 20)
    assert m.en_rango(0, 0)
    assert m.en_rango(0, 19)
    assert m.en_rango(19, 0)
    assert m.en_rango(19, 19)


def test_en_rango_fuera_del_borde():
    """Soporte de CA-04: salir por el borde queda fuera del mapa."""
    m = Mapa(20, 20)
    assert not m.en_rango(20, 0)
    assert not m.en_rango(0, 20)


def test_en_rango_negativo():
    """Soporte de CA-04: las coordenadas negativas quedan fuera del mapa."""
    m = Mapa(20, 20)
    assert not m.en_rango(-1, 0)
    assert not m.en_rango(0, -1)


# ---------- poner_obstaculo y es_obstaculo ----------

def test_poner_obstaculo():
    """Soporte de CA-04: una celda con obstáculo se reconoce como tal."""
    m = Mapa(5, 5)
    m.poner_obstaculo(2, 3)
    assert m.es_obstaculo(2, 3)


def test_obstaculo_no_afecta_otras_celdas():
    """Soporte de CA-04: poner un obstáculo no cambia las celdas vecinas."""
    m = Mapa(5, 5)
    m.poner_obstaculo(2, 3)
    assert not m.es_obstaculo(2, 2)
    assert not m.es_obstaculo(3, 3)


def test_obstaculo_fuera_del_mapa_falla():
    """Soporte de CA-04: no se puede poner un obstáculo fuera del mapa."""
    m = Mapa(5, 5)
    with pytest.raises(IndexError):
        m.poner_obstaculo(5, 0)


def test_es_obstaculo_fuera_del_mapa_falla():
    """Soporte de CA-04: consultar fuera del mapa da error."""
    m = Mapa(5, 5)
    with pytest.raises(IndexError):
        m.es_obstaculo(-1, 0)


# ---------- poner_objeto y objeto_en ----------

def test_poner_objeto():
    """Soporte de CA-05: el objeto queda guardado en su celda."""
    m = Mapa(5, 5)
    m.poner_objeto(1, 1, "espada")
    assert m.objeto_en(1, 1) == "espada"


def test_objeto_en_celda_con_obstaculo():
    """Soporte de CA-05: un obstáculo no cuenta como objeto."""
    m = Mapa(5, 5)
    m.poner_obstaculo(1, 1)
    assert m.objeto_en(1, 1) is None


def test_poner_objeto_fuera_del_mapa_falla():
    """Soporte de CA-07: no se puede soltar un objeto fuera del mapa."""
    m = Mapa(5, 5)
    with pytest.raises(IndexError):
        m.poner_objeto(0, 5, "espada")


# ---------- quitar_objeto ----------

def test_quitar_objeto_lo_devuelve():
    """Soporte de CA-05: quitar el objeto lo devuelve y deja la celda libre."""
    m = Mapa(5, 5)
    m.poner_objeto(1, 1, "espada")
    assert m.quitar_objeto(1, 1) == "espada"
    assert m.objeto_en(1, 1) is None


def test_quitar_objeto_de_celda_vacia():
    """Soporte de CA-05: quitar de una celda vacía devuelve None."""
    m = Mapa(5, 5)
    assert m.quitar_objeto(1, 1) is None


def test_quitar_objeto_no_borra_obstaculo():
    """Soporte de CA-04: quitar un objeto no elimina un obstáculo."""
    m = Mapa(5, 5)
    m.poner_obstaculo(1, 1)
    assert m.quitar_objeto(1, 1) is None
    assert m.es_obstaculo(1, 1)
