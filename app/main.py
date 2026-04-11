from fastapi import FastAPI
from app.api import personal, formacion
from app.db import engine, Base

# Para este taller, creamos las tablas si no existen al iniciar.
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Gestión de Personal - Evaluación 2",
    description="Servicio web para el registro de personal y su formación académica.",
    version="1.0.0"
)

# Incluir los routers
app.include_router(personal.router)
app.include_router(formacion.router)

@app.get("/")
def root():
    return {"message": "API de Gestión de Personal funcionando. Visite /docs para la documentación."}