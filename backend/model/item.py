from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    id: Optional[int] = None
    estado: str = "disponible"

class Libro(Item):
    titulo: str
    autor: str
    genero: str

class Laptop(Item):
    marca: str
    modelo: str
