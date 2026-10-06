# Historias de usuario

Formato: Como [quién], quiero [qué], para [valor].

## HU-01 Iniciar partida (F-01)
Como jugador, quiero iniciar una partida con mapa, monstruos y tesoros, para empezar a jugar sin configurar nada.
- CA-01: El mapa tiene al menos 20x20 celdas y los obstáculos ocupan como máximo el 25 %.
- CA-02: Al iniciar existen 1 jugador, al menos 2 monstruos y al menos 1 tesoro, todos en celdas libres y distintas.

## HU-02 Mover al jugador (F-02)
Como jugador, quiero moverme una casilla por turno o esperar, para explorar la mazmorra.
- CA-03: Mover hacia una celda libre cambia la posición del jugador en exactamente una casilla.
- CA-04: Mover hacia un obstáculo o fuera del borde no cambia la posición y avisa el motivo.

## HU-03 Inventario (F-03)
Como jugador, quiero recoger, usar, soltar y listar objetos, para gestionar lo que cargo.
- CA-05: Pisar una celda con objeto lo agrega al inventario y lo quita del mapa.
- CA-06: Listar el inventario vacío muestra un mensaje de inventario vacío, sin error.
- CA-07: Soltar un objeto lo quita del inventario y lo deja en la celda actual.

## HU-04 Deshacer y rehacer (F-04)
Como jugador, quiero deshacer y rehacer mis jugadas, para corregir errores sin reiniciar la partida.
- CA-08: Deshacer devuelve la última acción registrada y restaura posición e inventario.
- CA-09: Si deshago una recogida, el objeto vuelve al mapa.
- CA-10: Una acción nueva después de deshacer vacía lo que se podía rehacer.
- CA-11: Deshacer sin historial avisa que no hay nada que deshacer, sin error.
- CA-12: Rehacer después de deshacer repite la misma acción.

## HU-05 Monstruos persiguen (F-05)
Como jugador, quiero que cada monstruo me persiga por el camino más corto, para que el juego tenga reto.
- CA-13: En cada turno cada monstruo avanza una casilla por una ruta de menos pasos hacia el jugador.
- CA-14: Si no existe ruta al jugador, el monstruo se queda quieto, sin error.

## HU-06 Eventos del turno (F-06)
Como jugador, quiero ver los eventos de cada turno, para entender qué pasó.
- CA-15: Los eventos (aparición, recolección, colisión) se muestran en el orden en que ocurrieron.
- CA-16: Un turno sin eventos muestra un mensaje de turno sin novedades.

## HU-07 Victoria y derrota (F-07)
Como jugador, quiero que el juego detecte si gané o perdí, para saber cuándo termina la partida.
- CA-17: Si recojo todos los tesoros, la partida termina con victoria.
- CA-18: Si un monstruo ocupa mi celda, la partida termina con derrota. Si HU-10 entra, este criterio cambia: la derrota llega cuando la vida es 0 (ver CA-28).

## HU-08 Buscar entidad y consultar puntajes (F-08)
Como jugador, quiero buscar una entidad por su identificador y ver el mejor puntaje, para consultar datos rápido.
- CA-19: Buscar un identificador existente devuelve la entidad con su posición.
- CA-20: Buscar un identificador inexistente avisa que no existe, sin error.
- CA-21: Consultar el mejor puntaje devuelve el máximo registrado.
- CA-22: Consultar el mejor puntaje sin puntajes avisa que no hay registros.

## HU-09 Persecución con A* (mejora de F-05)
Como jugador, quiero que los monstruos calculen su ruta con A*, para que el juego responda rápido en mapas grandes.
- CA-23: La ruta encontrada por A* tiene el mismo largo que la de la búsqueda en anchura.
- CA-24: En el mismo mapa, A* explora igual o menos celdas que la búsqueda en anchura.

## HU-10 Combate con pregunta de cultura general (extiende F-05 y F-07)
Como jugador, quiero responder una pregunta de cultura general cuando un monstruo me alcanza, para vencerlo con conocimiento en lugar de perder al instante.
- CA-25: Cuando un monstruo ocupa la celda del jugador, se muestra una pantalla de combate en la consola con una pregunta y sus opciones.
- CA-26: Si el jugador responde bien, el monstruo desaparece del mapa.
- CA-27: Si el jugador responde mal, pierde un porcentaje fijo de su vida y el monstruo sigue en el mapa.
- CA-28: Si la vida del jugador llega a 0, la partida termina con derrota.
- CA-29: Las preguntas rotan sin repetirse hasta haber salido todas las del banco.
