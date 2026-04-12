from fastapi import FastAPI
from .api.personal import router as personal_router
from .api.formacion import router as formacion_router
from app.db import engine, Base

# Crea las tablas en la base de datos al iniciar
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Gestión de Personal - Evaluación 2",
    description="Sistema de registro de personal y formación académica ITM",
    version="1.0.0"
)

# Registro de routers
app.include_router(personal_router)
app.include_router(formacion_router)

@app.get("/")
def root():
    return {"message": "API funcionando correctamente. Visite /docs"}