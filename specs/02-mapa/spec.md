# Spec: Mapa

Versión 1.0. Soporta HU-01 y HU-02 (Must).

## Propósito

Representar la mazmorra como una rejilla de celdas. Cada celda puede estar libre, tener un obstáculo o tener un objeto.

## Fuera de alcance

- Mapas que cambian de tamaño durante la partida.
- Dibujar con colores (HU-11, Could).

## Operaciones

| Firma | Precondiciones | Postcondiciones | Errores |
|---|---|---|---|
| Mapa(filas, columnas) | filas y columnas mayores que 0 | todas las celdas están libres | ValueError |
| en_rango(fila, columna) | ninguna | verdadero si la celda existe | ninguno |
| poner_obstaculo(fila, columna) | la celda existe | la celda tiene obstáculo | IndexError si la celda no existe |
| es_obstaculo(fila, columna) | la celda existe | verdadero si tiene obstáculo | IndexError |
| poner_objeto(fila, columna, objeto) | la celda existe | la celda guarda el objeto | IndexError |
| quitar_objeto(fila, columna) | la celda existe | devuelve el objeto y deja la celda libre; None si no había | IndexError |

## Invariantes

- El tamaño del mapa no cambia después de crearlo.

## Criterios de aceptación

| ID | Criterio | Prueba |
|---|---|---|
| CA-01 | Una partida nueva tiene un mapa de al menos 20x20 y como máximo 25 % de obstáculos | test_partida_nueva_mapa_valido |
| CA-02 | Al iniciar, jugador, monstruos y tesoros están en celdas libres y distintas | test_partida_nueva_celdas_distintas |
| CA-03 | Moverse a una celda libre cambia la posición en exactamente una casilla | test_mover_a_celda_libre |
| CA-04 | Moverse a un obstáculo o fuera del borde no cambia la posición y avisa el motivo | test_mover_contra_obstaculo, test_mover_fuera_del_borde |

Los cuatro criterios se verifican sobre la partida, que usa el mapa.

## Casos extremos

- Mapa de 1x1.
- Celda en una esquina.
- Coordenadas negativas o mayores que el tamaño.
- Quitar un objeto de una celda vacía.

## Historial de cambios

| Versión | Fecha | Cambio | Motivo |
|---|---|---|---|
| 1.0 | 2026-10-27 | Versión inicial | Entrega 2 |
