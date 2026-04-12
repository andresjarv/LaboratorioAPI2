from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db import get_db
from app.schemas.formacion import Formacion, FormacionCreate, FormacionUpdate
from app.crud import formacion as crud_formacion

router = APIRouter(prefix="/formacion", tags=["Formación"])

@router.post("/", response_model=Formacion)
def create_formacion(formacion: FormacionCreate, db: Session = Depends(get_db)):
    return crud_formacion.create_formacion(db=db, formacion=formacion)

@router.get("/", response_model=List[Formacion])
def read_formaciones(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_formacion.get_formaciones(db, skip=skip, limit=limit)

@router.put("/{formacion_id}", response_model=Formacion)
def update_formacion(formacion_id: int, formacion: FormacionUpdate, db: Session = Depends(get_db)):
    db_formacion = crud_formacion.update_formacion(db, formacion_id=formacion_id, formacion=formacion)
    if db_formacion is None:
        raise HTTPException(status_code=404, detail="Registro de formación no encontrado")
    return db_formacion

@router.delete("/{formacion_id}")
def delete_formacion(formacion_id: int, db: Session = Depends(get_db)):
    success = crud_formacion.delete_formacion(db, formacion_id=formacion_id)
    if not success:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return {"message": "Registro eliminado correctamente"}