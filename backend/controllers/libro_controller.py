from fastapi import APIRouter
from dao.dao_libro import (
    obtener_libros_disponibles,
    obtener_todos_libros,
    agregar_libro,
    editar_libro,
    eliminar_libro,
)
from model.item import Libro

router = APIRouter()

@router.get("/libros")
def get_libros_disponibles():
    return obtener_libros_disponibles()

@router.get("/libros/todos")
def get_todos_libros():
    return obtener_todos_libros()

@router.post("/libros")
def post_agregar_libro(libro: Libro):
    return agregar_libro(libro)

@router.put("/libros/{libro_id}")
def put_editar_libro(libro_id: int, libro: Libro):
    return editar_libro(libro_id, libro)

@router.delete("/libros/{libro_id}")
def delete_eliminar_libro(libro_id: int):
    return eliminar_libro(libro_id)
