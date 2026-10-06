# Trazabilidad

Se completa y se mantiene desde la Entrega 2.

## Historial (HU-04)

| Criterio | Prueba | Código |
|---|---|---|
| CA-08 | tests/test_historial.py::test_deshacer_devuelve_ultima | dominio/historial.py |
| CA-09 | tests/test_historial.py::test_deshacer_conserva_efectos | dominio/historial.py |
| CA-10 | tests/test_historial.py::test_accion_nueva_vacia_rehacer | dominio/historial.py |
| CA-11 | tests/test_historial.py::test_deshacer_sin_historial | dominio/historial.py |
| CA-12 | tests/test_historial.py::test_rehacer_devuelve_deshecha | dominio/historial.py |

## Pila (apoya al historial)

| Criterio | Prueba | Código |
|---|---|---|
| CA-08 | tests/test_pila.py::test_pop_orden_lifo | estructuras/pila.py |
| CA-11 | tests/test_pila.py::test_pop_vacia_falla | estructuras/pila.py |
| CA-12 | tests/test_pila.py::test_pop_un_elemento | estructuras/pila.py |

## Código reutilizado

Ver la sección «Código reutilizado de Clase» en `specs/01-historial/plan.md` y la tabla de orígenes en `specs/00-producto/estructuras.md`.
