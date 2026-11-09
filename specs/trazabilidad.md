# Trazabilidad

Se lee en dos sentidos: de criterio a prueba y código, y de código a criterio.

## De criterio a prueba y código

| Criterio | Prueba | Código |
|---|---|---|
| CA-01 | tests/test_partida.py::test_partida_nueva_mapa_valido | dominio/partida.py `Partida.__init__`, dominio/mapa.py |
| CA-02 | tests/test_partida.py::test_partida_nueva_celdas_distintas, test_partida_nueva_tiene_tesoros | dominio/partida.py `celda_libre`, `_celda_libre_al_azar` |
| CA-03 | tests/test_partida.py::test_mover_a_celda_libre, test_mover_en_las_cuatro_direcciones, test_esperar_no_mueve | dominio/partida.py `mover`, `esperar` |
| CA-04 | tests/test_partida.py::test_mover_contra_obstaculo, test_mover_fuera_del_borde | dominio/partida.py `mover`, dominio/mapa.py `en_rango`, `es_obstaculo` |
| CA-05 | tests/test_partida.py::test_pisar_objeto_lo_recoge | dominio/partida.py `mover`, dominio/inventario.py `agregar` |
| CA-06 | tests/test_inventario.py::test_listar_inventario_vacio | dominio/inventario.py `listar`, main.py `mostrar_inventario` |
| CA-07 | tests/test_partida.py::test_soltar_objeto, test_soltar_objeto_que_no_tiene | dominio/partida.py `soltar`, dominio/inventario.py `quitar` |
| CA-08 | tests/test_historial.py::test_deshacer_devuelve_ultima, tests/test_partida.py::test_deshacer_restaura_posicion, test_deshacer_soltar_recupera_objeto | dominio/historial.py `deshacer`, dominio/partida.py `deshacer` |
| CA-09 | tests/test_historial.py::test_deshacer_conserva_efectos, tests/test_partida.py::test_deshacer_recogida_devuelve_objeto | dominio/partida.py `Accion`, `deshacer` |
| CA-10 | tests/test_historial.py::test_accion_nueva_vacia_rehacer, tests/test_partida.py::test_accion_nueva_borra_rehacer | dominio/historial.py `registrar` |
| CA-11 | tests/test_historial.py::test_deshacer_sin_historial, tests/test_partida.py::test_deshacer_sin_historial_avisa | dominio/partida.py `deshacer` |
| CA-12 | tests/test_historial.py::test_rehacer_devuelve_deshecha, tests/test_partida.py::test_rehacer_mover, test_rehacer_sin_deshacer_avisa | dominio/historial.py `rehacer`, dominio/partida.py `rehacer` |
| CA-15 | tests/test_eventos.py::test_eventos_en_orden, tests/test_partida.py::test_eventos_de_recoger_en_orden, test_aparicion_de_monstruos_al_iniciar | dominio/eventos.py, dominio/partida.py |
| CA-13 | tests/test_rutas.py::test_siguiente_paso_ruta_mas_corta, test_siguiente_paso_rodea_muro, test_siguiente_paso_vecino, test_misma_celda_devuelve_none, test_mapa_de_una_fila, tests/test_partida.py::test_monstruo_avanza_una_casilla, test_cada_monstruo_avanza_en_su_turno | dominio/rutas.py `siguiente_paso`, dominio/partida.py `mover_monstruos` |
| CA-14 | tests/test_rutas.py::test_sin_ruta_devuelve_none, tests/test_partida.py::test_monstruo_sin_ruta_se_queda_quieto | dominio/rutas.py `siguiente_paso`, dominio/partida.py `mover_monstruos` |
| CA-16 | tests/test_partida.py::test_turno_sin_eventos | dominio/partida.py `eventos_del_turno` |
| CA-17 | tests/test_partida.py::test_recoger_todos_los_tesoros_gana, test_queda_un_tesoro_sigue_jugando | dominio/partida.py `revisar_fin`, `quedan_tesoros` |
| CA-18 | tests/test_partida.py::test_monstruo_alcanza_al_jugador_pierde, test_jugador_pisa_monstruo_pierde, test_no_se_puede_actuar_al_terminar | dominio/partida.py `revisar_fin`, `terminar_turno` |

CA-04 también se verifica con tests/test_partida.py::test_chocar_con_muro_no_mueve_monstruos.

CA-19 a CA-29 son de HU-08, HU-09 y HU-10, que pasaron a Won't.

## Pruebas de soporte

Prueban las estructuras por dentro. Su docstring dice «Soporte de CA-XX».

| Archivo de pruebas | Estructura | Criterios que apoya |
|---|---|---|
| tests/test_pila.py | estructuras/pila.py | CA-08, CA-11, CA-12 |
| tests/test_mapa.py | dominio/mapa.py | CA-01, CA-03, CA-04, CA-05, CA-07 |
| tests/test_lista_enlazada.py | estructuras/lista_enlazada.py | CA-05, CA-06, CA-07 |
| tests/test_inventario.py | dominio/inventario.py | CA-05, CA-06, CA-07 |
| tests/test_cola.py | estructuras/cola.py | CA-15, CA-16; también la usa BFS (CA-13, CA-14) |
| estructuras/lista_circular.py | CA-13 |
| tests/test_eventos.py | dominio/eventos.py | CA-15, CA-16 |
| tests/test_lista_circular.py | estructuras/lista_circular.py | CA-13 |

## De código a criterio

| Código | Criterios |
|---|---|
| estructuras/nodo.py | base de pila, lista enlazada y cola |
| estructuras/pila.py | CA-08, CA-10, CA-11, CA-12 |
| estructuras/lista_enlazada.py | CA-05, CA-06, CA-07; también guarda los monstruos (CA-02) |
| estructuras/cola.py | CA-15, CA-16; también la usa BFS (CA-13, CA-14) |
| estructuras/lista_circular.py | CA-13 |
| dominio/mapa.py | CA-01, CA-03, CA-04, CA-05, CA-07 |
| dominio/inventario.py | CA-05, CA-06, CA-07 |
| dominio/historial.py | CA-08, CA-10, CA-11, CA-12 |
| dominio/eventos.py | CA-15, CA-16 |
| dominio/rutas.py | CA-13, CA-14 |
| dominio/partida.py | CA-01 a CA-05, CA-07 a CA-18 |
| main.py | CA-06 (mensaje de inventario vacío), CA-17 y CA-18 (muestra el fin), y los mensajes de los demás |

## Historial de cambios

| Versión | Fecha | Cambio | Motivo |
|---|---|---|---|
| 1.0 | 2026-10-06 | Tabla del componente historial | Entrega 1 |
| 2.0 | 2026-10-27 | Se cubren mapa, inventario, eventos y partida, en ambos sentidos | Entrega 2 |
| 3.0 | 2026-11-09 | Se agregan CA-13, CA-14, CA-17 y CA-18, lista circular y rutas | Entrega final |
