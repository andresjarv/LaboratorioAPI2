from sqlalchemy.orm import Session
from app.models.formacion import Formacion
from app.schemas.formacion import FormacionCreate, FormacionUpdate

def get_formaciones(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Formacion).offset(skip).limit(limit).all()

def create_formacion(db: Session, formacion: FormacionCreate):
    db_formacion = Formacion(**formacion.model_dump())
    db.add(db_formacion)
    db.commit()
    db.refresh(db_formacion)
    return db_formacion

def update_formacion(db: Session, formacion_id: int, formacion: FormacionUpdate):
    db_formacion = db.query(Formacion).filter(Formacion.id == formacion_id).first()
    if db_formacion:
        for key, value in formacion.model_dump(exclude_unset=True).items():
            setattr(db_formacion, key, value)
        db.commit()
        db.refresh(db_formacion)
    return db_formacion

def delete_formacion(db: Session, formacion_id: int):
    db_formacion = db.query(Formacion).filter(Formacion.id == formacion_id).first()
    if db_formacion:
        db.delete(db_formacion)
        db.commit()
        return True
    return False