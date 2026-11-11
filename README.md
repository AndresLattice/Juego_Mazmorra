# Juego de mazmorra: motor 2D con pathfinding

Proyecto integrador de Estructuras de Datos, Temática A.

Un aventurero explora una mazmorra y recoge tesoros mientras dos monstruos lo persiguen por el camino más corto.

## Requisitos

- Python 3.11 o superior
- pytest (solo para las pruebas)

## Instalar y ejecutar

Desde la carpeta del proyecto:

```bash
python -m pip install pytest
python main.py
```

Importante: el juego se inicia con `main.py`. Los archivos de `dominio/` y `estructuras/` son módulos y no se ejecutan solos.

## Correr las pruebas

```bash
python -m pytest
```

## Cómo se juega

| Comando | Acción |
|---|---|
| `w` `a` `s` `d` | mover arriba, izquierda, abajo, derecha |
| `e` | esperar un turno |
| `i` | ver el inventario |
| `soltar NOMBRE` | soltar un objeto en la celda actual |
| `usar NOMBRE` | usar un objeto |
| `z` | deshacer |
| `y` | rehacer |
| `h` | ayuda |
| `q` | salir |

En el mapa: `@` jugador, `M` monstruo, `#` obstáculo, `*` objeto, `.` libre.

- **Ganas** si recoges todos los tesoros.
- **Pierdes** si un monstruo llega a tu celda o si tú entras a la suya.
- **Con espada** sobrevives a un choque: el monstruo muere, reaparece en otro lugar y la espada se gasta.

## Estructura

- `main.py`: interfaz de consola
- `estructuras/`: una estructura por módulo (nodo, pila, lista enlazada, lista circular, cola)
- `dominio/`: lógica del juego (mapa, inventario, historial, eventos, rutas, partida)
- `tests/`: pruebas con pytest
- `specs/`: artefactos SDD
- `docs/`: informe final y evidencias
- `ANALISIS.md`: complejidad y comparación de decisiones
- `CAMBIOS.md`: resumen de lo que se omitió y cambió
- `BITACORA.md`: qué se hizo, qué se dificultó y uso de IA

## Código reutilizado

Parte de las estructuras se adapta de los laboratorios del curso (carpeta `Clase`, semanas 5 a 9). Cada archivo reutilizado dice su origen en el docstring inicial. La tabla completa está en `CAMBIOS.md`.
