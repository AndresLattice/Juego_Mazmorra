# Priorización MoSCoW: Juego de mazmorra

**Fecha:** 2026-10-06 · **Versión:** 1.0

## Capacidad

8 h por semana × 4 semanas = 32 h
− 20 % de imprevistos = **25 h reales**

Motivo del porcentaje: es la primera vez que implemento varias de estas estructuras, así que mantengo el 20 % de la guía y no lo bajo. Cubre configurar el entorno, depurar errores, entender estructuras nuevas, reescribir si la spec cambia y preparar cada entrega.

## Must (suman 24 h de 25 h)

| Historia | Horas | Por qué es Must | Componente |
|----------|-------|-----------------|------------|
| HU-01 Iniciar partida con mapa, monstruos y tesoros | 2 | Mínimo del dominio: mapa de 20x20 con obstáculos | 02-mapa |
| HU-02 Mover al jugador una casilla por turno | 3 | Mínimo del dominio: jugador por turnos | 02-mapa |
| HU-03 Recoger, usar, soltar y listar objetos | 4 | Mínimo del dominio: objetos e inventario | 03-inventario |
| HU-04 Deshacer y rehacer acciones con sus efectos | 5 | Mínimo del dominio: historial completo | 01-historial |
| HU-05 Monstruos persiguen por el camino más corto con búsqueda en anchura | 5 | Mínimo del dominio: sin persecución no hay pathfinding. Versión más simple | 06-rutas |
| HU-06 Ver los eventos de cada turno en orden | 3 | Mínimo del dominio: sistema de eventos | 04-eventos |
| HU-07 Detectar victoria y derrota | 2 | Mínimo del dominio: condiciones de fin | dominio |

Orden de las horas: las 24 h dejan 1 h de holgura. No cabe ningún Should dentro de lo calculado.

## Should

| Historia | Horas | Condición para entrar |
|----------|-------|-----------------------|
| HU-10 Combate con pregunta de cultura general | 4 | Primero en entrar. Necesita HU-05 y HU-07 terminadas. No es un mínimo del dominio: mientras no entre, la colisión es derrota directa |
| HU-09 Persecución con A* y distancia Manhattan | 4 | Solo si HU-05 termina antes de lo estimado. Bajó de Must porque la búsqueda en anchura demuestra lo mismo |
| HU-08 Buscar entidad por identificador y ver el mejor puntaje | 4 | Solo si los Must cierran con holgura. No es un mínimo del dominio |

Prioridad entre Should: HU-10, luego HU-09, luego HU-08.

## Could

| Historia | Horas |
|----------|-------|
| HU-11 Mapa con colores en la consola | 2 |

Los Could no entran en el cálculo de horas.

## Won't (esta versión no)

| Historia | Razón |
|----------|-------|
| Interfaz gráfica y ventana emergente de combate | El curso exige consola y no permite dependencias gráficas. El combate se muestra como una pantalla en la consola |
| Guardar y cargar partidas | No agrega ninguna estructura evaluada y consume tiempo |
| Monstruos con comportamientos distintos | Una sola persecución demuestra el pathfinding; más tipos no cambian las estructuras |

## Orden de construcción

1. HU-01 y HU-02: sin mapa y jugador nada más existe.
2. HU-03: el inventario necesita un jugador que recoja.
3. HU-04: no se puede deshacer lo que todavía no existe, así que va tras mover y recoger.
4. HU-06: los eventos se generan a partir de las acciones anteriores.
5. HU-05: la persecución usa el mapa y genera eventos de colisión.
6. HU-07: victoria y derrota dependen de todo lo anterior.

## Plan de contingencia

Si mi capacidad se redujera a la mitad, unas 12 h:
- Los mínimos del dominio no se descartan, se recortan a su versión mínima.
- Persecución: BFS sin optimizaciones, 3 h.
- Inventario: agregar, listar y usar; soltar queda al final.
- Historial: deshacer y rehacer solo de movimientos y recogidas.
- Eventos: solo recolección y colisión.
- HU-08, HU-09, HU-10 y el Could desaparecen.

## Historial de cambios

| Versión | Fecha | Qué cambió de prioridad | Por qué |
|---------|-------|-------------------------|---------|
| 1.0 | 2026-10-06 | Versión inicial | Entrega 1 |
