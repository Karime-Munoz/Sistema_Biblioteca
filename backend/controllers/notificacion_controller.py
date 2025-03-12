from fastapi import APIRouter, HTTPException
from dao.supabase_client import supabase
from model.notificacion import Notificacion

router = APIRouter()

@router.get("/notificaciones/{usuario_id}")
def obtener_notificaciones(usuario_id: int):
    try:
        response = supabase.table("notificaciones").select("*").eq("usuario_id", usuario_id).execute()
        return response.data if response.data else {"message": "No hay notificaciones"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
