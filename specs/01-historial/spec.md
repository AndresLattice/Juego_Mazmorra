# Spec: Historial de acciones

Versión 1.0. Soporta HU-04 (Must).

## Propósito

Guardar las acciones del jugador para poder deshacerlas y rehacerlas, conservando sus efectos.

## Fuera de alcance

- Guardar el historial en disco.
- Historial de las acciones de los monstruos.
- Límite máximo de acciones guardadas.

## Operaciones

| Firma | Precondiciones | Postcondiciones | Errores |
|---|---|---|---|
| registrar(accion) | ninguna | la acción es la más reciente y no queda nada por rehacer | ninguno |
| deshacer() | hay al menos una acción registrada | devuelve la acción más reciente y queda disponible para rehacer | historial vacío |
| rehacer() | hay al menos una acción deshecha | devuelve la última acción deshecha y vuelve a ser la más reciente | nada que rehacer |
| hay_que_deshacer() | ninguna | verdadero si existe una acción registrada | ninguno |
| hay_que_rehacer() | ninguna | verdadero si existe una acción deshecha | ninguno |

## Invariantes

- La acción devuelta al deshacer es siempre la más reciente.
- Registrar una acción nueva nunca deja acciones por rehacer.

## Criterios de aceptación

| ID | Criterio | Prueba |
|---|---|---|
| CA-08 | Deshacer devuelve la última acción registrada | test_deshacer_devuelve_ultima |
| CA-09 | La acción devuelta conserva sus efectos para poder revertirlos | test_accion_conserva_efectos |
| CA-10 | Registrar una acción nueva elimina todo lo rehacible | test_registrar_vacia_rehacer |
| CA-11 | Deshacer sin historial avisa y no falla | test_deshacer_vacio |
| CA-12 | Rehacer después de deshacer devuelve la misma acción | test_rehacer_devuelve_deshecha |

## Casos extremos

- Historial vacío.
- Un solo elemento.
- Deshacer más veces que acciones registradas.
- Rehacer sin haber deshecho nada.

## Historial de cambios

| Versión | Fecha | Cambio | Motivo |
|---|---|---|---|
| 1.0 | 2026-10-06 | Versión inicial | Entrega 1 |
