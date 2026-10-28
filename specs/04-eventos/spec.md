# Spec: Eventos

Versión 1.0. Soporta HU-06 (Must).

## Propósito

Guardar lo que pasa en cada turno y mostrarlo en el mismo orden en que ocurrió.

## Fuera de alcance

- Eventos con prioridad.
- Guardar los eventos de turnos anteriores.

## Operaciones

| Firma | Precondiciones | Postcondiciones | Errores |
|---|---|---|---|
| registrar(evento) | ninguna | el evento queda al final | ninguno |
| hay_eventos() | ninguna | verdadero si queda algún evento | ninguno |
| sacar_todos() | ninguna | devuelve los eventos en orden de llegada y deja la cola vacía | ninguno |

Cada evento es un texto, por ejemplo `"Recogiste una espada"`.

## Invariantes

- El primer evento registrado es el primero en salir.

## Criterios de aceptación

| ID | Criterio | Prueba |
|---|---|---|
| CA-15 | Los eventos se muestran en el orden en que ocurrieron | test_eventos_en_orden |
| CA-16 | Un turno sin eventos muestra un mensaje de turno sin novedades | test_turno_sin_eventos |

## Casos extremos

- Sin eventos.
- Un solo evento.
- Registrar después de sacar todos.

## Historial de cambios

| Versión | Fecha | Cambio | Motivo |
|---|---|---|---|
| 1.0 | 2026-10-27 | Versión inicial | Entrega 2 |
