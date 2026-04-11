from pydantic import BaseModel, EmailStr
from typing import Optional, List
from .formacion import Formacion

class PersonalBase(BaseModel):
    nombre: str
    apellido: str
    tipo_documento: str
    documento: str
    email: EmailStr # Requiere 'email-validator' (pip install email-validator)
    telefono: Optional[str] = None

class PersonalCreate(PersonalBase):
    pass # Para crear pedimos todo lo de PersonalBase

class PersonalUpdate(PersonalBase):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    tipo_documento: Optional[str] = None
    documento: Optional[str] = None
    email: Optional[EmailStr] = None

class Personal(PersonalBase):
    id: int
    # Incluimos la relación para que el Swagger muestre la formación de la persona
    formaciones: List[Formacion] = []

    class Config:
        from_attributes = True