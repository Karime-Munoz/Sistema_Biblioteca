from dbConnection.supabase_client import supabase

def obtener_notificaciones(usuario_id: int):
    try:
        response = supabase.table("notificaciones").select("*").eq("usuario_id", usuario_id).execute()
        return response.data if response.data else {"message": "No hay notificaciones"}
    except Exception as e:
        return f"Error obteniendo notificaciones: {str(e)}"
