from pydantic import BaseModel

class Articulo(BaseModel):
    id: int
    titulo: str
    contenido: str
