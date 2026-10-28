from dominio.eventos import Eventos


# ---------- registrar ----------

def test_registrar_un_evento():
    """Soporte de CA-15: un evento registrado queda pendiente."""
    e = Eventos()
    e.registrar("Recogiste una espada")
    assert e.hay_eventos()


def test_registrar_varios_conserva_orden():
    """Soporte de CA-15: registrar varios conserva el orden de llegada."""
    e = Eventos()
    e.registrar("A")
    e.registrar("B")
    assert e.sacar_todos() == ["A", "B"]


def test_registrar_despues_de_sacar_todos():
    """Soporte de CA-15: se puede registrar después de vaciar."""
    e = Eventos()
    e.registrar("A")
    e.sacar_todos()
    e.registrar("B")
    assert e.sacar_todos() == ["B"]


# ---------- hay_eventos ----------

def test_sin_eventos_al_crear():
    """Soporte de CA-16: al crear no hay eventos."""
    assert not Eventos().hay_eventos()


def test_hay_eventos_con_uno():
    """Soporte de CA-15: con un evento, hay eventos."""
    e = Eventos()
    e.registrar("A")
    assert e.hay_eventos()


def test_no_hay_eventos_tras_sacar_todos():
    """Soporte de CA-16: después de sacar todos no quedan eventos."""
    e = Eventos()
    e.registrar("A")
    e.sacar_todos()
    assert not e.hay_eventos()


# ---------- sacar_todos ----------

def test_eventos_en_orden():
    """Verifica CA-15: los eventos salen en el orden en que ocurrieron."""
    e = Eventos()
    e.registrar("Apareció un monstruo")
    e.registrar("Recogiste una espada")
    e.registrar("Un monstruo te alcanzó")
    assert e.sacar_todos() == [
        "Apareció un monstruo",
        "Recogiste una espada",
        "Un monstruo te alcanzó",
    ]


def test_sacar_todos_sin_eventos():
    """Soporte de CA-16: sacar todos sin eventos devuelve una lista vacía."""
    assert Eventos().sacar_todos() == []


def test_sacar_todos_un_evento():
    """Soporte de CA-15: sacar todos con un solo evento."""
    e = Eventos()
    e.registrar("A")
    assert e.sacar_todos() == ["A"]
