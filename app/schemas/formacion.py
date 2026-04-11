from pydantic import BaseModel
from typing import Optional

# Propiedades compartidas (Base)
class FormacionBase(BaseModel):
    nivel_formacion: str
    institucion: str
    titulo: str
    fecha_grado: Optional[str] = None

# Propiedades para crear (POST)
class FormacionCreate(FormacionBase):
    id_personal: int

# Propiedades para actualización (PATCH/PUT)
class FormacionUpdate(FormacionBase):
    nivel_formacion: Optional[str] = None
    institucion: Optional[str] = None
    titulo: Optional[str] = None

# Lo que devolvemos al cliente (Response)
class Formacion(FormacionBase):
    id: int
    id_personal: int

    class Config:
        from_attributes = True # Permite que Pydantic lea modelos de SQLAlchemy