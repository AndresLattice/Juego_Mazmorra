# Constitución del proyecto

Proyecto: Juego de mazmorra, motor 2D con pathfinding (Temática A).
Autor: Andres Agudelo.
Contexto narrativo: un aventurero explora una mazmorra y recoge tesoros mientras unos monstruos lo persiguen.

## Principios

1. Toda estructura de datos declarada se implementa desde cero. No se usa `list`, `dict`, `set`, `deque` ni `heapq` como sustituto de esa estructura. Si se usan como soporte interno, se justifica en el `plan.md`.
2. Ninguna operación pública está terminada sin docstring con su complejidad y pruebas del caso normal y de los casos extremos.
3. La especificación precede al código. Si cambia el comportamiento, primero cambia el `spec.md`, en su propio commit.
4. Cada estructura se integra al dominio apenas se termina.
5. Cada criterio de aceptación tiene un ID (CA-01, CA-02...) y una prueba que lo cita en su docstring.

## Restricciones

- Lenguaje: Python 3.11 o superior.
- Dependencias permitidas: pytest y, opcionalmente, matplotlib.
- Interfaz: consola.
- Debe ejecutarse en una máquina limpia siguiendo el README.
- Cada estructura vive en su propio módulo. Prohibido un archivo monolítico.

## Definición de terminado

- Todos sus criterios de aceptación tienen prueba y pasan.
- La complejidad real coincide con la declarada en el plan.
- Revisé el código contra la spec antes de integrarlo.
- `spec.md`, `plan.md` y `tasks.md` reflejan el estado real.

## Uso de asistentes de IA

- Permitido para: entender conceptos, depurar errores y revisar mi código contra la spec.
- No permitido para: entregar código que no pueda explicar línea por línea.
- Todo uso se declara en `BITACORA.md` y en el informe final.

## Commits

- Pequeños y frecuentes, uno por tarea.
- Prefijos: `spec`, `plan`, `test`, `feat`, `fix`.
- Mensajes en español, con tildes.

## Historial de cambios

| Versión | Fecha | Cambio | Motivo |
|---|---|---|---|
| 1.0 | 2026-10-06 | Versión inicial | Entrega 1 |
