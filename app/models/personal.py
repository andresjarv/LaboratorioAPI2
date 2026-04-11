from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db import Base

class Personal(Base):
    __tablename__ = "personal"
    # IMPORTANTE: Aplicamos el schema asignado por el docente
    __table_args__ = {"schema": "grupo_3"}

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    tipo_documento = Column(String(20), nullable=False)
    documento = Column(String(20), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    telefono = Column(String(20), nullable=True)

    # Relación uno a muchos con Formacion
    formaciones = relationship("Formacion", back_populates="persona", cascade="all, delete-orphan")