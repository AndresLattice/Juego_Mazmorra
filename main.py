"""Interfaz de consola del juego de mazmorra."""

from dominio.partida import Partida

AYUDA = """Comandos:
  w / s / a / d   mover arriba, abajo, izquierda, derecha
  e               esperar
  i               ver inventario
  soltar NOMBRE   soltar un objeto
  usar NOMBRE     usar un objeto
  z               deshacer
  y               rehacer
  h               ayuda
  q               salir"""

TECLAS = {"w": "arriba", "s": "abajo", "a": "izquierda", "d": "derecha"}


def dibujar(partida):
    """Dibuja el mapa. @ jugador, M monstruo, # obstáculo, * objeto, . libre."""
    for fila in range(partida.mapa.filas):
        linea = ""
        for columna in range(partida.mapa.columnas):
            if partida.jugador == (fila, columna):
                linea += "@ "
            elif partida.monstruos.buscar((fila, columna)) != -1:
                linea += "M "
            elif partida.mapa.es_obstaculo(fila, columna):
                linea += "# "
            elif partida.mapa.objeto_en(fila, columna) is not None:
                linea += "* "
            else:
                linea += ". "
        print(linea)


def mostrar_inventario(partida):
    if partida.inventario.esta_vacio():
        return "Inventario vacío"
    return "Inventario: " + ", ".join(partida.inventario.listar())


def ejecutar(partida, comando):
    """Ejecuta un comando y devuelve el mensaje para el jugador."""
    if comando in TECLAS:
        return partida.mover(TECLAS[comando])
    if comando == "e":
        return partida.esperar()
    if comando == "i":
        return mostrar_inventario(partida)
    if comando == "z":
        return partida.deshacer()
    if comando == "y":
        return partida.rehacer()
    if comando == "h":
        return AYUDA
    if comando.startswith("soltar "):
        return partida.soltar(comando[7:])
    if comando.startswith("usar "):
        return partida.usar(comando[5:])
    return "Comando desconocido. Escribe h para ver la ayuda"


def main():
    print("Juego de mazmorra: motor 2D con pathfinding")
    print(AYUDA)
    partida = Partida()
    while True:
        print()
        dibujar(partida)
        for evento in partida.eventos_del_turno():
            print("-", evento)
        comando = input("> ").strip().lower()
        if comando == "q":
            print("Hasta luego")
            break
        print(ejecutar(partida, comando))


if __name__ == "__main__":
    main()
