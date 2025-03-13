from fastapi import APIRouter
from dao.dao_login import verificar_credenciales
from pydantic import BaseModel

class LoginRequest(BaseModel):
    matricula: str
    contrasena: str

router = APIRouter()

@router.post("/login")
def post_verificar_credenciales(user: LoginRequest):
    return verificar_credenciales(user)
