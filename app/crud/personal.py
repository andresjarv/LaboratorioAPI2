from sqlalchemy.orm import Session
from app.models.personal import Personal
from app.schemas.personal import PersonalCreate, PersonalUpdate

def get_persona(db: Session, persona_id: int):
    return db.query(Personal).filter(Personal.id == persona_id).first()

def get_personas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Personal).offset(skip).limit(limit).all()

def create_persona(db: Session, persona: PersonalCreate):
    db_persona = Personal(**persona.model_dump())
    db.add(db_persona)
    db.commit()
    db.refresh(db_persona)
    return db_persona

def update_persona(db: Session, persona_id: int, persona: PersonalUpdate):
    db_persona = get_persona(db, persona_id)
    if db_persona:
        update_data = persona.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_persona, key, value)
        db.commit()
        db.refresh(db_persona)
    return db_persona

def delete_persona(db: Session, persona_id: int):
    db_persona = get_persona(db, persona_id)
    if db_persona:
        db.delete(db_persona)
        db.commit()
        return True
    return False