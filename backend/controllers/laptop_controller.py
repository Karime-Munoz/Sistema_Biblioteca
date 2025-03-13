from fastapi import APIRouter
from dao.dao_laptop import (
    obtener_laptops_disponibles,
    obtener_todas_laptops,
    agregar_laptop,
    editar_laptop,
    eliminar_laptop,
)
from model.item import Laptop

router = APIRouter()

@router.get("/laptops")
def get_laptops_disponibles():
    return obtener_laptops_disponibles()

@router.get("/laptops/todos")
def get_todas_laptops():
    return obtener_todas_laptops()

@router.post("/laptops")
def post_agregar_laptop(laptop: Laptop):
    return agregar_laptop(laptop)

@router.put("/laptops/{laptop_id}")
def put_editar_laptop(laptop_id: int, laptop: Laptop):
    return editar_laptop(laptop_id, laptop)

@router.delete("/laptops/{laptop_id}")
def delete_eliminar_laptop(laptop_id: int):
    return eliminar_laptop(laptop_id)
