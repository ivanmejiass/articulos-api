from fastapi import APIRouter
from models.comentario import Comentario
from typing import List

router = APIRouter()

comentarios = []

@router.post("/comentarios/")
def crear_comentario(comentario: Comentario):
    comentarios.append(comentario)
    return comentario

@router.get("/comentarios/", response_model=List[Comentario])
def leer_comentarios():
    return comentarios

@router.get("/comentarios/{comentario_id}", response_model=Comentario)
def leer_comentario(comentario_id: int):
    for comentario in comentarios:
        if comentario.id == comentario_id:
            return comentario
    return {"error": "Comentario no encontrado"}

@router.put("/comentarios/{comentario_id}")
def actualizar_comentario(comentario_id: int, comentario: Comentario):
    for index, existing_comentario in enumerate(comentarios):
        if existing_comentario.id == comentario_id:
            comentarios[index] = comentario
            return comentario
    return {"error": "Comentario no encontrado"}

@router.delete("/comentarios/{comentario_id}")
def borrar_comentario(comentario_id: int):
    for index, existing_comentario in enumerate(comentarios):
        if existing_comentario.id == comentario_id:
            del comentarios[index]
            return {"message": "Comentario borrado"}
    return {"error": "Comentario no encontrado"}
