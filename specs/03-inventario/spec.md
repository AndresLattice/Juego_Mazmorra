# Spec: Inventario

Versión 1.0. Soporta HU-03 (Must).

## Propósito

Guardar los objetos que carga el jugador.

## Fuera de alcance

- Límite de capacidad.
- Ordenar el inventario.

## Operaciones

| Firma | Precondiciones | Postcondiciones | Errores |
|---|---|---|---|
| agregar(objeto) | ninguna | el objeto queda en el inventario | ninguno |
| quitar(objeto) | el objeto está en el inventario | el objeto sale del inventario | ValueError si no está |
| listar() | ninguna | devuelve los objetos del más reciente al más antiguo | ninguno |
| esta_vacio() | ninguna | verdadero si no hay objetos | ninguno |

Usar y soltar son acciones de la partida. Las dos llaman a `quitar`. Soltar además deja el objeto en la celda del jugador.

## Criterios de aceptación

| ID | Criterio | Prueba |
|---|---|---|
| CA-05 | Pisar una celda con objeto lo agrega al inventario y lo quita del mapa | test_pisar_objeto_lo_recoge |
| CA-06 | Listar el inventario vacío muestra un mensaje de inventario vacío, sin error | test_listar_inventario_vacio |
| CA-07 | Soltar un objeto lo quita del inventario y lo deja en la celda actual | test_soltar_objeto |

## Casos extremos

- Inventario vacío.
- Un solo objeto.
- Quitar un objeto que no está.
- Dos objetos iguales: se quita solo uno.

## Historial de cambios

| Versión | Fecha | Cambio | Motivo |
|---|---|---|---|
| 1.0 | 2026-10-27 | Versión inicial | Entrega 2 |
