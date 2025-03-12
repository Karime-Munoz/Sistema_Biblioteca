from pydantic import BaseModel
from typing import Optional, List

class Usuario(BaseModel):
    id: Optional[int] = None
    nombre: str
    apellido: str
    matricula: str
    rol: str  # hay que poner tal cual en BD o no podra loguearse "Alumno", "Profesor", "Administrador"
    contrasena: str
    prestamos: Optional[List["Prestamo"]] = None

class Alumno(Usuario):
    rol: str = "Alumno"

class Profesor(Usuario):
    rol: str = "Profesor"

class Administrador(Usuario):
    rol: str = "Administrador"
