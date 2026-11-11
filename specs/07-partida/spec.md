# Spec: Partida

Versión 1.1. Soporta HU-01 a HU-07 y HU-12.

## Propósito

Unir mapa, inventario, historial, eventos, turnos y rutas en una partida que se puede ganar o perder.

## Fuera de alcance

- Varias partidas guardadas.
- Deshacer los movimientos de los monstruos.

## Operaciones

| Firma | Precondiciones | Postcondiciones | Errores |
|---|---|---|---|
| Partida(semilla) | ninguna | mapa, jugador, monstruos y objetos listos; estado "jugando" | ninguno |
| mover(direccion), esperar(), soltar(objeto), usar(objeto) | estado "jugando" | si la acción se hizo, cada monstruo da un paso; devuelve un mensaje | ninguno |
| deshacer(), rehacer() | estado "jugando" | revierte o repite la acción del jugador con sus efectos; los monstruos no se mueven | ninguno |
| eventos_del_turno() | ninguna | devuelve los eventos en orden, o "Turno sin novedades" | ninguno |
| estado | ninguna | "jugando", "victoria" o "derrota" | ninguno |

Cuando la partida terminó, las acciones devuelven un aviso y no cambian nada.

## Criterios de aceptación

| ID | Criterio | Prueba |
|---|---|---|
| CA-17 | Si recojo todos los tesoros, la partida termina con victoria | test_recoger_todos_los_tesoros_gana |
| CA-18 | Si un monstruo ocupa mi celda y no tengo espada, la partida termina con derrota | test_monstruo_alcanza_al_jugador_pierde, test_jugador_pisa_monstruo_pierde |
| CA-30 | Con espada, el monstruo que me alcanza muere, la espada se gasta y la partida sigue | test_pisar_monstruo_con_espada_lo_mata, test_monstruo_alcanza_jugador_con_espada |
| CA-31 | El monstruo muerto aparece en otra celda libre | test_monstruo_muerto_reaparece_en_celda_libre |

La partida también verifica CA-01 a CA-16 junto con cada componente.

## Pelea con la espada

Pasa en los dos tipos de choque: cuando el jugador entra a la celda de un monstruo y cuando un monstruo llega a la del jugador. El monstruo no se elimina de la partida: se mueve a una celda libre al azar. Así la lista de monstruos y los turnos no cambian.

Matar un monstruo no se deshace, igual que los movimientos de los monstruos.

## Casos extremos

- Dos monstruos llegan al jugador en el mismo turno con una sola espada: muere el primero y el segundo gana.

- Actuar después de terminar la partida.
- Ganar y ser alcanzado en el mismo turno: gana la victoria, porque el jugador actúa primero.
- Soltar un tesoro después de recogerlo: vuelve a faltar.

## Historial de cambios

| Versión | Fecha | Cambio | Motivo |
|---|---|---|---|
| 1.0 | 2026-11-09 | Versión inicial | Entrega final. La partida existía desde la Entrega 2 sin spec propia |
| 1.1 | 2026-11-11 | Se agrega la pelea con espada (CA-30, CA-31). CA-18 aclara «sin espada» | HU-12 |
