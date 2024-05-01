from fastapi import APIRouter
from models.articulo import Articulo
from typing import List

router = APIRouter()

articulos = []

@router.post("/articulos/")
def crear_articulo(articulo: Articulo):
    articulos.append(articulo)
    return articulo

@router.get("/articulos/", response_model=List[Articulo])
def leer_articulos():
    return articulos

@router.get("/articulos/{articulo_id}", response_model=Articulo)
def leer_articulo(articulo_id: int):
    for articulo in articulos:
        if articulo.id == articulo_id:
            return articulo
    return {"error": "Artículo no encontrado"}

@router.put("/articulos/{articulo_id}")
def actualizar_articulo(articulo_id: int, articulo: Articulo):
    for index, existing_articulo in enumerate(articulos):
        if existing_articulo.id == articulo_id:
            articulos[index] = articulo
            return articulo
    return {"error": "Artículo no encontrado"}

@router.delete("/articulos/{articulo_id}")
def borrar_articulo(articulo_id: int):
    for index, existing_articulo in enumerate(articulos):
        if existing_articulo.id == articulo_id:
            del articulos[index]
            return {"message": "Artículo borrado"}
    return {"error": "Artículo no encontrado"}
