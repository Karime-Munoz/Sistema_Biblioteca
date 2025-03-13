from fastapi import APIRouter
from dao.dao_prestamo import solicitar_prestamo, obtener_prestamos_usuario
from model.prestamo import Prestamo

router = APIRouter()

@router.post("/prestamos")
def post_solicitar_prestamo(prestamo: Prestamo):
    return solicitar_prestamo(prestamo)

@router.get("/prestamos/{matricula}")
def get_prestamos_usuario(matricula: str):
    return obtener_prestamos_usuario(matricula)
