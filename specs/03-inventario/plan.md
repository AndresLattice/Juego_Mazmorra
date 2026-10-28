# Plan: Inventario

Versión 1.0.

## Estructura elegida

Lista enlazada simple, `ListaEnlazada` en `estructuras/lista_enlazada.py`. El inventario vive en `dominio/inventario.py`. Cada objeto es un texto con su nombre.

## Por qué esta estructura

- Recoger es la operación más frecuente. Agregar al inicio es O(1).
- No se necesita acceso por posición: el jugador pide los objetos por nombre.
- Quitar no desplaza elementos, solo cambia un enlace.

## Complejidad

| Operación | Costo | Nota |
|---|---|---|
| agregar | O(1) | inserta al inicio |
| quitar | O(n) | busca el objeto y lo elimina |
| listar | O(n) | |
| esta_vacio | O(1) | |

Usar y soltar cuestan O(n) porque el objeto puede estar en cualquier posición. Con pocos objetos no afecta el juego.

## Alternativa descartada

Arreglo dinámico. Buscar por nombre es O(n) en ambas, pero en el arreglo quitar del medio además desplaza los elementos siguientes.

## Soporte interno

Ninguno. La lista usa los nodos de `estructuras/nodo.py`.

## Código reutilizado de Clase

| Archivo del proyecto | Origen en Clase | Qué se hizo |
|---|---|---|
| `estructuras/lista_enlazada.py` | `Clase/semana_06/lista_enlazada.py` | Se conservan el diseño y los nombres. Se completan `_insertar_en_medio` y `_eliminar_no_primero`, que en el laboratorio estaban sin terminar. Se quitan `__getitem__` y `__repr__` |

## Historial de cambios

| Versión | Fecha | Cambio | Motivo |
|---|---|---|---|
| 1.0 | 2026-10-27 | Versión inicial | Entrega 2 |
