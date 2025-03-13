from fastapi import APIRouter
from dao.dao_notificacion import obtener_notificaciones

router = APIRouter()

@router.get("/notificaciones/{usuario_id}")
def get_obtener_notificaciones(usuario_id: int):
    return obtener_notificaciones(usuario_id)
