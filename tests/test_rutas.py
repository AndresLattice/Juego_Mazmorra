from dominio.mapa import Mapa
from dominio.rutas import siguiente_paso


def test_siguiente_paso_ruta_mas_corta():
    """Verifica CA-13: en línea recta el paso va directo hacia el jugador."""
    m = Mapa(5, 5)
    assert siguiente_paso(m, (0, 0), (0, 3)) == (0, 1)


def test_siguiente_paso_rodea_muro():
    """Verifica CA-13: si hay un muro, el paso lo rodea por el camino corto."""
    m = Mapa(5, 5)
    m.poner_obstaculo(0, 1)
    m.poner_obstaculo(1, 1)
    m.poner_obstaculo(2, 1)
    m.poner_obstaculo(3, 1)
    # El único paso es por la fila 4, así que primero baja.
    assert siguiente_paso(m, (0, 0), (0, 2)) == (1, 0)


def test_siguiente_paso_vecino():
    """Verifica CA-13: si el jugador está al lado, el paso es su celda."""
    m = Mapa(5, 5)
    assert siguiente_paso(m, (2, 2), (2, 3)) == (2, 3)


def test_misma_celda_devuelve_none():
    """Verifica CA-13: si ya está en la celda del jugador, no hay paso."""
    m = Mapa(5, 5)
    assert siguiente_paso(m, (2, 2), (2, 2)) is None


def test_sin_ruta_devuelve_none():
    """Verifica CA-14: si el jugador está encerrado, no hay paso."""
    m = Mapa(5, 5)
    m.poner_obstaculo(1, 2)
    m.poner_obstaculo(3, 2)
    m.poner_obstaculo(2, 1)
    m.poner_obstaculo(2, 3)
    assert siguiente_paso(m, (0, 0), (2, 2)) is None


def test_mapa_de_una_fila():
    """Verifica CA-13: funciona en el mapa más angosto."""
    m = Mapa(1, 4)
    assert siguiente_paso(m, (0, 3), (0, 0)) == (0, 2)
