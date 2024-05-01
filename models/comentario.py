from pydantic import BaseModel

class Comentario(BaseModel):
    id: int
    articulo_id: int
    autor: str
    contenido: str
