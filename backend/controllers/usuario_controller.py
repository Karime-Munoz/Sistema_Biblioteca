from fastapi import APIRouter
from dao.dao_usuario import obtener_usuarios, agregar_usuario, editar_usuario, eliminar_usuario
from pydantic import BaseModel

class Usuario(BaseModel):
    nombre: str
    apellido: str
    matricula: str
    rol: str
    contrasena: str

router = APIRouter()

@router.get("/usuarios")
def get_usuarios():
    return obtener_usuarios()

@router.post("/usuarios")
def post_agregar_usuario(usuario: Usuario):
    return agregar_usuario(usuario)

@router.put("/usuarios/{matricula}")
def put_editar_usuario(matricula: str, usuario: Usuario):
    return editar_usuario(matricula, usuario)

@router.delete("/usuarios/{matricula}")
def delete_eliminar_usuario(matricula: str):
    return eliminar_usuario(matricula)
