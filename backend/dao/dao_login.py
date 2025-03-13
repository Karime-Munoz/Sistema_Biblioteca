from dbConnection.supabase_client import supabase
from pydantic import BaseModel

class LoginRequest(BaseModel):
    matricula: str
    contrasena: str

def verificar_credenciales(user: LoginRequest):
    try:
        if " " in user.matricula or " " in user.contrasena:
            return "No se permiten espacios en la matrícula o contraseña"

        query = supabase.table("usuarios").select("matricula, contrasena, rol").eq("matricula", user.matricula).execute()
        
        if not query.data:
            return "Matrícula o contraseña incorrecta"

        usuario = query.data[0]

        if usuario["contrasena"] != user.contrasena:
            return "Matrícula o contraseña incorrecta"

        return {"matricula": user.matricula, "rol": usuario["rol"]}
    except Exception as e:
        return f"Error en el login: {str(e)}"
