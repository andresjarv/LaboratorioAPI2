from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db import get_db
from app.schemas.personal import Personal, PersonalCreate, PersonalUpdate
from app.crud import personal as crud_personal

router = APIRouter(prefix="/personal", tags=["Personal"])

@router.post("/", response_model=Personal)
def create_persona(persona: PersonalCreate, db: Session = Depends(get_db)):
    return crud_personal.create_persona(db=db, persona=persona)

@router.get("/", response_model=List[Personal])
def read_personas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_personal.get_personas(db, skip=skip, limit=limit)

@router.get("/{persona_id}", response_model=Personal)
def read_persona(persona_id: int, db: Session = Depends(get_db)):
    db_persona = crud_personal.get_persona(db, persona_id=persona_id)
    if db_persona is None:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    return db_persona

@router.put("/{persona_id}", response_model=Personal)
def update_persona(persona_id: int, persona: PersonalUpdate, db: Session = Depends(get_db)):
    db_persona = crud_personal.update_persona(db, persona_id=persona_id, persona=persona)
    if db_persona is None:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    return db_persona

@router.delete("/{persona_id}")
def delete_persona(persona_id: int, db: Session = Depends(get_db)):
    success = crud_personal.delete_persona(db, persona_id=persona_id)
    if not success:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    return {"message": "Persona eliminada correctamente"}