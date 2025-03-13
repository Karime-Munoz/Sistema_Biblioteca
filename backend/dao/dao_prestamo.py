from dbConnection.supabase_client import supabase
from datetime import datetime, timedelta
from model.prestamo import Prestamo

def solicitar_prestamo(prestamo: Prestamo):
    try:
        item = None
        tipo = None

        # Buscar el libro
        libro = supabase.table("libros").select("estado, titulo, autor").eq("id", prestamo.item_id).execute()
        if libro.data and libro.data[0]["estado"] == "disponible":
            item = libro.data[0]
            tipo = "libro"
        
        # Buscar la laptop
        laptop = supabase.table("laptops").select("estado, marca, modelo").eq("id", prestamo.item_id).execute()
        if laptop.data and laptop.data[0]["estado"] == "disponible":
            item = laptop.data[0]
            tipo = "laptop"

        if not item:
            return "El item no está disponible para préstamo."

        fecha_inicio = datetime.now().strftime("%Y-%m-%d")
        fecha_fin = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")

        # Insertar el préstamo en la BD
        supabase.table("prestamos").insert({
            "matricula": prestamo.matricula,
            "item_id": prestamo.item_id,
            "titulo": item.get("titulo", item.get("marca", "Equipo")),
            "autor": item.get("autor", item.get("modelo", "Modelo desconocido")),
            "fecha_inicio": fecha_inicio,
            "fecha_fin": fecha_fin,
            "tipo": tipo
        }).execute()

        # Actualizar el estado del libro o laptop
        tabla = "libros" if tipo == "libro" else "laptops"
        supabase.table(tabla).update({"estado": "prestado"}).eq("id", prestamo.item_id).execute()

        return f"{tipo.capitalize()} prestado con éxito"
    except Exception as e:
        return f"Error en el préstamo: {str(e)}"

def obtener_prestamos_usuario(matricula: str):
    try:
        response = supabase.table("prestamos").select("*").eq("matricula", matricula).execute()
        return response.data if isinstance(response.data, list) else []
    except Exception as e:
        return []
