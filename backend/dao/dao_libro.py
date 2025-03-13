from dbConnection.supabase_client import supabase
from model.item import Libro

def obtener_libros_disponibles():
    try:
        response = supabase.table("libros").select("*").eq("estado", "disponible").execute()
        return response.data if response.data else []
    except Exception as e:
        return f"Error obteniendo libros disponibles: {str(e)}"

def obtener_todos_libros():
    try:
        response = supabase.table("libros").select("*").execute()
        return response.data if response.data else []
    except Exception as e:
        return f"Error obteniendo todos los libros: {str(e)}"

def agregar_libro(libro: Libro):
    try:
        response = supabase.table("libros").insert(libro.dict()).execute()
        if response.error:
            return "Error al agregar el libro"
        return "Libro agregado con éxito"
    except Exception as e:
        return f"Error al agregar el libro: {str(e)}"

def editar_libro(libro_id: int, libro: Libro):
    try:
        response = supabase.table("libros").update(libro.dict()).eq("id", libro_id).execute()
        if response.error:
            return "Error al actualizar el libro"
        return "Libro actualizado correctamente"
    except Exception as e:
        return f"Error al actualizar el libro: {str(e)}"

def eliminar_libro(libro_id: int):
    try:
        response = supabase.table("libros").delete().eq("id", libro_id).execute()
        if response.error:
            return "Error al eliminar el libro"
        return "Libro eliminado correctamente"
    except Exception as e:
        return f"Error al eliminar el libro: {str(e)}"
