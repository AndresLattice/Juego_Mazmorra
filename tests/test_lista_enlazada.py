import pytest

from estructuras.lista_enlazada import ListaEnlazada, PosicionInvalidaError


def lista_con(*elementos):
    lista = ListaEnlazada()
    for e in elementos:
        lista.insertar(lista.tamaño(), e)
    return lista


# ---------- tamaño ----------

def test_tamaño_lista_vacia():
    """Soporte de CA-06: una lista nueva tiene tamaño 0."""
    assert ListaEnlazada().tamaño() == 0


def test_tamaño_un_elemento():
    """Soporte de CA-05: después de insertar uno, el tamaño es 1."""
    assert lista_con("a").tamaño() == 1


def test_tamaño_tras_eliminar():
    """Soporte de CA-07: eliminar baja el tamaño."""
    lista = lista_con("a", "b")
    lista.eliminar(0)
    assert lista.tamaño() == 1


# ---------- insertar ----------

def test_insertar_en_vacia_fija_cabeza_y_cola():
    """Soporte de CA-05: el primer elemento es cabeza y cola a la vez."""
    lista = ListaEnlazada()
    lista.insertar(0, "a")
    assert lista._cabeza is lista._cola


def test_insertar_al_inicio():
    """Soporte de CA-05: insertar en 0 deja el elemento primero."""
    lista = lista_con("b")
    lista.insertar(0, "a")
    assert lista.obtener(0) == "a"


def test_insertar_en_medio():
    """Soporte de CA-05: insertar en medio respeta el orden."""
    lista = lista_con("a", "c")
    lista.insertar(1, "b")
    assert list(lista) == ["a", "b", "c"]


def test_insertar_posicion_invalida():
    """Soporte de CA-05: insertar fuera de rango da error."""
    with pytest.raises(PosicionInvalidaError):
        ListaEnlazada().insertar(1, "a")


# ---------- obtener ----------

def test_obtener_un_elemento():
    """Soporte de CA-06: obtener devuelve el único elemento."""
    assert lista_con("a").obtener(0) == "a"


def test_obtener_ultimo():
    """Soporte de CA-06: obtener la última posición."""
    assert lista_con("a", "b", "c").obtener(2) == "c"


def test_obtener_en_vacia_falla():
    """Soporte de CA-06: obtener en una lista vacía da error."""
    with pytest.raises(PosicionInvalidaError):
        ListaEnlazada().obtener(0)


# ---------- eliminar ----------

def test_eliminar_unico_deja_lista_vacia():
    """Soporte de CA-07: eliminar el único deja cabeza y cola en None."""
    lista = lista_con("a")
    assert lista.eliminar(0) == "a"
    assert lista._cabeza is None
    assert lista._cola is None


def test_eliminar_ultimo_actualiza_cola():
    """Soporte de CA-07: eliminar el último mueve la cola al penúltimo."""
    lista = lista_con("a", "b", "c")
    assert lista.eliminar(2) == "c"
    assert lista._cola.dato == "b"
    assert lista._cola.siguiente is None


def test_eliminar_en_medio():
    """Soporte de CA-07: eliminar en medio reengancha los vecinos."""
    lista = lista_con("a", "b", "c")
    assert lista.eliminar(1) == "b"
    assert list(lista) == ["a", "c"]


def test_eliminar_en_vacia_falla():
    """Soporte de CA-07: eliminar en una lista vacía da error."""
    with pytest.raises(PosicionInvalidaError):
        ListaEnlazada().eliminar(0)


# ---------- buscar ----------

def test_buscar_en_vacia():
    """Soporte de CA-07: buscar en una lista vacía devuelve -1."""
    assert ListaEnlazada().buscar("a") == -1


def test_buscar_existente():
    """Soporte de CA-07: buscar devuelve la posición del elemento."""
    assert lista_con("a", "b", "c").buscar("c") == 2


def test_buscar_repetido_devuelve_el_primero():
    """Soporte de CA-07: con repetidos, buscar devuelve la primera aparición."""
    assert lista_con("a", "b", "b").buscar("b") == 1


# ---------- recorrer ----------

def test_recorrer_vacia():
    """Soporte de CA-06: recorrer una lista vacía no da elementos."""
    assert list(ListaEnlazada()) == []


def test_recorrer_un_elemento():
    """Soporte de CA-06: recorrer una lista de un elemento."""
    assert list(lista_con("a")) == ["a"]


def test_recorrer_en_orden():
    """Soporte de CA-06: el recorrido va de la cabeza a la cola."""
    assert list(lista_con("a", "b", "c")) == ["a", "b", "c"]
