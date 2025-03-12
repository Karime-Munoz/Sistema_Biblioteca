from fastapi import APIRouter, HTTPException
from dao.supabase_client import supabase
from model.item import Libro

router = APIRouter()


@router.get("/libros")
def obtener_libros_disponibles():
    try:
        response = supabase.table("libros").select("*").eq("estado", "disponible").execute()
        return response.data if response.data else []
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/libros/todos")
def obtener_todos_libros():
    try:
        response = supabase.table("libros").select("*").execute()
        return response.data if response.data else []
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/libros")
def agregar_libro(libro: Libro):
    try:
        response = supabase.table("libros").insert(libro.dict()).execute()
        if response.error:
            raise HTTPException(status_code=400, detail="❌ Error al agregar el libro")
        return {"message": "✅ Libro agregado con éxito"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/libros/{libro_id}")
def editar_libro(libro_id: int, libro: Libro):
    try:
        response = supabase.table("libros").update(libro.dict()).eq("id", libro_id).execute()
        if response.error:
            raise HTTPException(status_code=400, detail="❌ Error al actualizar el libro")
        return {"message": "✅ Libro actualizado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/libros/{libro_id}")
def eliminar_libro(libro_id: int):
    try:
        response = supabase.table("libros").delete().eq("id", libro_id).execute()
        if response.error:
            raise HTTPException(status_code=400, detail="❌ Error al eliminar el libro")
        return {"message": "✅ Libro eliminado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
