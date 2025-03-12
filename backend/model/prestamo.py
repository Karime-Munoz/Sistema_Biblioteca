from pydantic import BaseModel
from typing import Optional

class Prestamo(BaseModel):
    id: Optional[int] = None  
    matricula: str 
    item_id: int  
    fecha_inicio: Optional[str] = None  
    fecha_fin: Optional[str] = None  
