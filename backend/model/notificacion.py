from pydantic import BaseModel
from typing import Optional

class Notificacion(BaseModel):
    id: Optional[int] = None
    usuario_id: int
    mensaje: str
    leida: bool = False
