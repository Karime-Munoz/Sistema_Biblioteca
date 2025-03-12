from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from dao.supabase_client import supabase  

# Definir el router
router = APIRouter()

# Modelo de lo que recibimos
class LoginRequest(BaseModel):
    matricula: str
    contrasena: str

@router.post("/login")  #Usando router
def verificar_credenciales(user: LoginRequest):
    try:
        if " " in user.matricula or " " in user.contrasena:
            raise HTTPException(status_code=400, detail="No se permiten espacios en la matrícula o contraseña")

        query = supabase.table("usuarios").select("matricula, contrasena, rol").eq("matricula", user.matricula).execute()
        
        if not query.data:
            raise HTTPException(status_code=401, detail="Matrícula o contraseña incorrecta")

        usuario = query.data[0]

        if usuario["contrasena"] != user.contrasena:
            raise HTTPException(status_code=401, detail="Matrícula o contraseña incorrecta")

        return {"matricula": user.matricula, "rol": usuario["rol"]}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
