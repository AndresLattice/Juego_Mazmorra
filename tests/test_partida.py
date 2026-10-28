from dominio.mapa import Mapa
from dominio.partida import FILAS, COLUMNAS, Partida
from estructuras.lista_enlazada import ListaEnlazada


def partida_vacia():
    """Partida con mapa sin obstáculos, sin monstruos y jugador en (5, 5)."""
    p = Partida(semilla=1)
    p.mapa = Mapa(FILAS, COLUMNAS)
    p.monstruos = ListaEnlazada()
    p.jugador = (5, 5)
    p.eventos.sacar_todos()
    return p


# ---------- iniciar partida ----------

def test_partida_nueva_mapa_valido():
    """Verifica CA-01: mapa de al menos 20x20 y como máximo 25 % de obstáculos."""
    p = Partida(semilla=7)
    assert p.mapa.filas >= 20
    assert p.mapa.columnas >= 20
    obstaculos = 0
    for f in range(p.mapa.filas):
        for c in range(p.mapa.columnas):
            if p.mapa.es_obstaculo(f, c):
                obstaculos += 1
    assert obstaculos * 100 <= 25 * p.mapa.filas * p.mapa.columnas


def test_partida_nueva_celdas_distintas():
    """Verifica CA-02: jugador, 2 monstruos y tesoros en celdas libres y distintas."""
    p = Partida(semilla=7)
    assert p.monstruos.tamaño() >= 2
    ocupadas = [p.jugador]
    for m in p.monstruos:
        ocupadas.append(m)
    for f, c in ocupadas:
        assert not p.mapa.es_obstaculo(f, c)
        assert p.mapa.objeto_en(f, c) is None
    for i in range(len(ocupadas)):
        for j in range(i + 1, len(ocupadas)):
            assert ocupadas[i] != ocupadas[j]


def test_partida_nueva_tiene_tesoros():
    """Verifica CA-02: al iniciar hay al menos un tesoro en el mapa."""
    p = Partida(semilla=7)
    tesoros = 0
    for f in range(p.mapa.filas):
        for c in range(p.mapa.columnas):
            if p.mapa.objeto_en(f, c) == "tesoro":
                tesoros += 1
    assert tesoros >= 1


# ---------- mover ----------

def test_mover_a_celda_libre():
    """Verifica CA-03: moverse a una celda libre cambia una casilla."""
    p = partida_vacia()
    p.mover("derecha")
    assert p.jugador == (5, 6)


def test_mover_en_las_cuatro_direcciones():
    """Verifica CA-03: cada dirección cambia una sola casilla."""
    p = partida_vacia()
    p.mover("arriba")
    assert p.jugador == (4, 5)
    p.mover("abajo")
    assert p.jugador == (5, 5)
    p.mover("izquierda")
    assert p.jugador == (5, 4)


def test_mover_contra_obstaculo():
    """Verifica CA-04: chocar con un obstáculo no mueve y avisa el motivo."""
    p = partida_vacia()
    p.mapa.poner_obstaculo(5, 6)
    mensaje = p.mover("derecha")
    assert p.jugador == (5, 5)
    assert mensaje == "Hay un obstáculo"


def test_mover_fuera_del_borde():
    """Verifica CA-04: salir del mapa no mueve y avisa el motivo."""
    p = partida_vacia()
    p.jugador = (0, 0)
    mensaje = p.mover("arriba")
    assert p.jugador == (0, 0)
    assert mensaje == "No puedes salir del mapa"


def test_esperar_no_mueve():
    """Verifica CA-03: esperar deja al jugador en su celda."""
    p = partida_vacia()
    p.esperar()
    assert p.jugador == (5, 5)


# ---------- inventario ----------

def test_pisar_objeto_lo_recoge():
    """Verifica CA-05: pisar un objeto lo pasa al inventario y lo quita del mapa."""
    p = partida_vacia()
    p.mapa.poner_objeto(5, 6, "espada")
    p.mover("derecha")
    assert p.inventario.listar() == ["espada"]
    assert p.mapa.objeto_en(5, 6) is None


def test_soltar_objeto():
    """Verifica CA-07: soltar quita del inventario y deja en la celda actual."""
    p = partida_vacia()
    p.inventario.agregar("espada")
    p.soltar("espada")
    assert p.inventario.esta_vacio()
    assert p.mapa.objeto_en(5, 5) == "espada"


def test_soltar_objeto_que_no_tiene():
    """Verifica CA-07: soltar algo que no se tiene avisa, sin error."""
    p = partida_vacia()
    assert p.soltar("espada") == "No tienes: espada"


def test_usar_objeto_lo_consume():
    """Verifica HU-03: usar un objeto lo quita del inventario."""
    p = partida_vacia()
    p.inventario.agregar("poción")
    p.usar("poción")
    assert p.inventario.esta_vacio()


# ---------- deshacer y rehacer ----------

def test_deshacer_restaura_posicion():
    """Verifica CA-08: deshacer devuelve al jugador a su posición anterior."""
    p = partida_vacia()
    p.mover("derecha")
    p.deshacer()
    assert p.jugador == (5, 5)


def test_deshacer_recogida_devuelve_objeto():
    """Verifica CA-09: deshacer una recogida devuelve el objeto al mapa."""
    p = partida_vacia()
    p.mapa.poner_objeto(5, 6, "espada")
    p.mover("derecha")
    p.deshacer()
    assert p.mapa.objeto_en(5, 6) == "espada"
    assert p.inventario.esta_vacio()


def test_deshacer_soltar_recupera_objeto():
    """Verifica CA-08: deshacer soltar devuelve el objeto al inventario."""
    p = partida_vacia()
    p.inventario.agregar("espada")
    p.soltar("espada")
    p.deshacer()
    assert p.inventario.listar() == ["espada"]
    assert p.mapa.objeto_en(5, 5) is None


def test_deshacer_sin_historial_avisa():
    """Verifica CA-11: deshacer sin historial avisa, sin error."""
    p = partida_vacia()
    assert p.deshacer() == "No hay nada que deshacer"


def test_rehacer_mover():
    """Verifica CA-12: rehacer repite el movimiento deshecho."""
    p = partida_vacia()
    p.mapa.poner_objeto(5, 6, "espada")
    p.mover("derecha")
    p.deshacer()
    p.rehacer()
    assert p.jugador == (5, 6)
    assert p.inventario.listar() == ["espada"]


def test_rehacer_sin_deshacer_avisa():
    """Verifica CA-12: rehacer sin haber deshecho avisa, sin error."""
    p = partida_vacia()
    assert p.rehacer() == "No hay nada que rehacer"


def test_accion_nueva_borra_rehacer():
    """Verifica CA-10: mover después de deshacer impide rehacer."""
    p = partida_vacia()
    p.mover("derecha")
    p.deshacer()
    p.mover("abajo")
    assert p.rehacer() == "No hay nada que rehacer"


# ---------- eventos ----------

def test_eventos_de_recoger_en_orden():
    """Verifica CA-15: los eventos del turno salen en orden."""
    p = partida_vacia()
    p.mapa.poner_objeto(5, 6, "espada")
    p.monstruos.insertar(0, (5, 6))
    p.mover("derecha")
    assert p.eventos_del_turno() == ["Recogiste: espada", "Chocaste con un monstruo"]


def test_turno_sin_eventos():
    """Verifica CA-16: un turno sin eventos muestra que no hubo novedades."""
    p = partida_vacia()
    p.esperar()
    assert p.eventos_del_turno() == ["Turno sin novedades"]


def test_aparicion_de_monstruos_al_iniciar():
    """Verifica CA-15: al iniciar se registra la aparición de cada monstruo."""
    p = Partida(semilla=7)
    eventos = p.eventos_del_turno()
    assert len(eventos) == 2
    assert eventos[0].startswith("Apareció un monstruo")
