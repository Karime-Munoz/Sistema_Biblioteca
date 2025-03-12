from fastapi import APIRouter, HTTPException
from dao.supabase_client import supabase
from pydantic import BaseModel

router = APIRouter()


class Usuario(BaseModel):
    nombre: str
    apellido: str
    matricula: str
    rol: str  # "Alumno", "Profesor", "Administrador"
    contrasena: str


@router.get("/usuarios")
def obtener_usuarios():
    try:
        response = supabase.table("usuarios").select("*").execute()

        if not response or not hasattr(response, "data") or response.data is None:
            raise HTTPException(status_code=500, detail="❌ Error al obtener los usuarios.")

        return response.data  

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"❌ Error inesperado: {str(e)}")

# Agregar un usuario (ID se asigna automáticamente)
@router.post("/usuarios")
def agregar_usuario(usuario: Usuario):
    try:
        # Validar si matrícula ya existe
        existe = supabase.table("usuarios").select("matricula").eq("matricula", usuario.matricula).execute()
        if existe.data:
            raise HTTPException(status_code=400, detail="❌ La matrícula ya está registrada.")

        # Insertar usuario en la BD (ID se asigna automáticamente)
        response = supabase.table("usuarios").insert(usuario.dict()).execute()

        if "data" in response and response.data:
            return {"message": "✅ Usuario agregado correctamente"}
        else:
            raise HTTPException(status_code=400, detail="❌ Error al agregar el usuario en la base de datos.")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"❌ Error inesperado: {str(e)}")
