# Bitácora

## Entrega 1

- Qué hice: Toma de decisiones de todo tipo
- Qué se me dificultó: Profundizar en la idea del juego, que honestamente mas adelante muy seguramente seguire agregando cambios de distintos tipos
- En qué usé IA: Organizacion del SDD y moscow, aparte de la generacion de un artifact para entender y especificar cambios. Tambien en la reutilizacion del test.py, generar y explicar pila.py
- Código reutilizado de Clase: `PilaEnlazada` y `Historial` de `Clase/semana_08` y `Nodo` de `Clase/semana_05`. Se adaptaron a `estructuras/` y `dominio/`. Detalle en `specs/01-historial/plan.md`.

## Entrega 2

- Qué hice: Escribí primero las specs del mapa, el inventario y los eventos, y después el código y las pruebas de cada uno. Uní todo en una partida y armé el menú de consola. Ya se puede mover al jugador, recoger, soltar y usar objetos, deshacer y rehacer, y ver los eventos de cada turno. Corregí la spec del historial, porque CA-11 decía que deshacer sin historial daba error y la historia pedía solo un aviso.
- Qué se me dificultó: Que deshacer y rehacer devolvieran también los efectos de cada acción, como volver a poner en el mapa un objeto recogido. Para eso cada acción se guarda con lo necesario para revertirla.
- En qué usé IA: Para revisar las specs contra la rúbrica, simplificarlas, completar los métodos que faltaban en la lista enlazada de Clase, escribir el código de la partida y del menú, y escribir las pruebas. Revisé cada commit antes de aprobarlo.
- Código reutilizado de Clase: `ListaEnlazada` de `Clase/semana_06` y `ColaEnlazada` de `Clase/semana_09`. Detalle en el `plan.md` de cada componente.
