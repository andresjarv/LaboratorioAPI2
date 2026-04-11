from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base

class Formacion(Base):
    __tablename__ = "formacion"
    __table_args__ = {"schema": "grupo_3"}

    id = Column(Integer, primary_key=True, index=True)
    id_personal = Column(Integer, ForeignKey("grupo_3.personal.id"), nullable=False)
    nivel_formacion = Column(String(50), nullable=False)
    institucion = Column(String(150), nullable=False)
    titulo = Column(String(150), nullable=False)
    fecha_grado = Column(String(20), nullable=True) # Se puede usar Date, pero String es más flexible para este taller

    # Relación inversa
    persona = relationship("Personal", back_populates="formaciones")