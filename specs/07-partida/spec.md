# Spec: Partida

Versión 1.0. Soporta HU-01 a HU-07.

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
| CA-18 | Si un monstruo ocupa mi celda, la partida termina con derrota | test_monstruo_alcanza_al_jugador_pierde, test_jugador_pisa_monstruo_pierde |

La partida también verifica CA-01 a CA-16 junto con cada componente.

## Casos extremos

- Actuar después de terminar la partida.
- Ganar y ser alcanzado en el mismo turno: gana la victoria, porque el jugador actúa primero.
- Soltar un tesoro después de recogerlo: vuelve a faltar.

## Historial de cambios

| Versión | Fecha | Cambio | Motivo |
|---|---|---|---|
| 1.0 | 2026-11-09 | Versión inicial | Entrega final. La partida existía desde la Entrega 2 sin spec propia |
