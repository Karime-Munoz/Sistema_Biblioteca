from dbConnection.supabase_client import supabase
from pydantic import BaseModel

class Usuario(BaseModel):
    nombre: str
    apellido: str
    matricula: str
    rol: str  # "Alumno", "Profesor", "Administrador"
    contrasena: str

def obtener_usuarios():
    try:
        response = supabase.table("usuarios").select("*").execute()
        return response.data if response.data else []
    except Exception as e:
        return f"Error obteniendo usuarios: {str(e)}"

def agregar_usuario(usuario: Usuario):
    try:
        existe = supabase.table("usuarios").select("matricula").eq("matricula", usuario.matricula).execute()
        if existe.data:
            return "La matrícula ya está registrada."

        response = supabase.table("usuarios").insert(usuario.dict()).execute()
        if "data" in response and response.data:
            return "Usuario agregado correctamente"
        return "Error al agregar el usuario en la base de datos."
    except Exception as e:
        return f"Error al agregar usuario: {str(e)}"

def editar_usuario(matricula: str, usuario: Usuario):
    try:
        response = supabase.table("usuarios").update(usuario.dict()).eq("matricula", matricula).execute()
        if response.error:
            return "Error al actualizar el usuario"
        return "Usuario actualizado correctamente"
    except Exception as e:
        return f"Error al actualizar el usuario: {str(e)}"

def eliminar_usuario(matricula: str):
    try:
        response = supabase.table("usuarios").delete().eq("matricula", matricula).execute()
        if response.error:
            return "Error al eliminar el usuario"
        return "Usuario eliminado correctamente"
    except Exception as e:
        return f"Error al eliminar el usuario: {str(e)}"
