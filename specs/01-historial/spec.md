# Spec: Historial de acciones

Versión 1.1. Soporta HU-04 (Must).

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
| deshacer() | hay al menos una acción registrada | devuelve la acción más reciente y queda disponible para rehacer | PilaVaciaError si el historial está vacío |
| rehacer() | hay al menos una acción deshecha | devuelve la última acción deshecha y vuelve a ser la más reciente | PilaVaciaError si no hay nada que rehacer |
| puede_deshacer() | ninguna | verdadero si existe una acción registrada | ninguno |
| puede_rehacer() | ninguna | verdadero si existe una acción deshecha | ninguno |

## Invariantes

- La acción devuelta al deshacer es siempre la más reciente.
- Registrar una acción nueva nunca deja acciones por rehacer.

## Criterios de aceptación

| ID | Criterio | Prueba |
|---|---|---|
| CA-08 | Deshacer devuelve la última acción registrada | test_deshacer_devuelve_ultima |
| CA-09 | La acción devuelta conserva sus efectos para poder revertirlos | test_deshacer_conserva_efectos |
| CA-10 | Registrar una acción nueva elimina todo lo rehacible | test_accion_nueva_vacia_rehacer |
| CA-11 | Deshacer sin historial avisa con PilaVaciaError y no corrompe el estado | test_deshacer_sin_historial |
| CA-12 | Rehacer después de deshacer devuelve la misma acción | test_rehacer_devuelve_deshecha |

## Casos extremos

- Historial vacío.
- Un solo elemento.
- Deshacer más veces que acciones registradas.
- Rehacer sin haber deshecho nada.

## Código reutilizado

El comportamiento de este componente coincide con `Historial` del laboratorio de la semana 8 (`Clase/semana_08/historial.py`). Ver el detalle en `plan.md`.

## Historial de cambios

| Versión | Fecha | Cambio | Motivo |
|---|---|---|---|
| 1.0 | 2026-10-06 | Versión inicial | Entrega 1 |
| 1.1 | 2026-10-06 | Nombres `puede_deshacer` y `puede_rehacer`; error `PilaVaciaError`; se declara el código reutilizado | Alinear la spec con el laboratorio de la semana 8 que se reutiliza |
