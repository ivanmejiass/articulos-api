from fastapi import FastAPI
from routes import articulos, comentarios

app = FastAPI()

app.include_router(articulos.router)
app.include_router(comentarios.router)
