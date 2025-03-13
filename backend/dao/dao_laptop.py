from dbConnection.supabase_client import supabase
from model.item import Laptop

def obtener_laptops_disponibles():
    try:
        response = supabase.table("laptops").select("*").eq("estado", "disponible").execute()
        return response.data if response.data else []
    except Exception as e:
        return f"Error obteniendo laptops disponibles: {str(e)}"

def obtener_todas_laptops():
    try:
        response = supabase.table("laptops").select("*").execute()
        return response.data if response.data else []
    except Exception as e:
        return f"Error obteniendo todas las laptops: {str(e)}"

def agregar_laptop(laptop: Laptop):
    try:
        response = supabase.table("laptops").insert(laptop.dict()).execute()
        return "Laptop agregada con éxito" if response.data else "Error al agregar la laptop"
    except Exception as e:
        return f"Error agregando laptop: {str(e)}"

def editar_laptop(laptop_id: int, laptop: Laptop):
    try:
        response = supabase.table("laptops").update(laptop.dict()).eq("id", laptop_id).execute()
        return "Laptop actualizada correctamente" if response.data else "Error al actualizar la laptop"
    except Exception as e:
        return f"Error editando laptop: {str(e)}"

def eliminar_laptop(laptop_id: int):
    try:
        response = supabase.table("laptops").delete().eq("id", laptop_id).execute()
        return "Laptop eliminada correctamente" if response.data else "Error al eliminar la laptop"
    except Exception as e:
        return f"Error eliminando laptop: {str(e)}"
