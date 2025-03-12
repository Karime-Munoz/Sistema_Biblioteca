from fastapi import APIRouter, HTTPException
from dao.supabase_client import supabase
from model.item import Laptop  

router = APIRouter()


@router.get("/laptops")
def obtener_laptops_disponibles():
    try:
        response = supabase.table("laptops").select("*").eq("estado", "disponible").execute()
        return response.data if response.data else []
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/laptops/todos")
def obtener_todas_laptops():
    try:
        response = supabase.table("laptops").select("*").execute()
        return response.data if response.data else []
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/laptops")
def agregar_laptop(laptop: Laptop):
    try:
        response = supabase.table("laptops").insert(laptop.dict()).execute()
        if response.error:
            raise HTTPException(status_code=400, detail="❌ Error al agregar la laptop")
        return {"message": "✅ Laptop agregada con éxito"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/laptops/{laptop_id}")
def editar_laptop(laptop_id: int, laptop: Laptop):
    try:
        response = supabase.table("laptops").update(laptop.dict()).eq("id", laptop_id).execute()
        if response.error:
            raise HTTPException(status_code=400, detail="❌ Error al actualizar la laptop")
        return {"message": "✅ Laptop actualizada correctamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/laptops/{laptop_id}")
def eliminar_laptop(laptop_id: int):
    try:
        response = supabase.table("laptops").delete().eq("id", laptop_id).execute()
        if response.error:
            raise HTTPException(status_code=400, detail="❌ Error al eliminar la laptop")
        return {"message": "✅ Laptop eliminada correctamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
