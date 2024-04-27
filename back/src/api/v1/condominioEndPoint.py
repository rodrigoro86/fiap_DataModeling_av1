from fastapi import APIRouter, HTTPException

from src.models.condominioModel import CondominioBase

router = APIRouter()

@router.post("/condominios/", response_model=CondominioBase)
def create_condominio(condominio: CondominioBase):

    return "ok"

"""@router.get("/condominios/", response_model=List[CondominioModel])
def read_condominios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    condominios = db.select(select(CondominioModel).offset(skip).limit(limit)).all()
    return condominios

@router.get("/condominios/{condominio_id}", response_model=CondominioModel)
def read_condominio(condominio_id: int, db: Session = Depends(get_db)):
    condominio = db.select(select(CondominioModel).where(CondominioModel.id == condominio_id)).first()
    if not condominio:
        raise HTTPException(status_code=404, detail="Condominio not found")
    return condominio

@router.put("/condominios/{condominio_id}", response_model=CondominioModel)
def update_condominio(condominio_id: int, condominio: CondominioModel, db: Session = Depends(get_db)):
    db_condominio = db.select(select(CondominioModel).where(CondominioModel.id == condominio_id)).first()
    if not db_condominio:
        raise HTTPException(status_code=404, detail="Condominio not found")
    condominio_data = condominio.dict()
    for key, value in condominio_data.items():
        setattr(db_condominio, key, value)
    db.add(db_condominio)
    db.commit()
    db.refresh(db_condominio)
    return db_condominio

@router.delete("/condominios/{condominio_id}")
def delete_condominio(condominio_id: int, db: Session = Depends(get_db)):
    condominio = db.select(select(CondominioModel).where(CondominioModel.id == condominio_id)).first()
    if not condominio:
        raise HTTPException(status_code=404, detail="Condominio not found")
    db.delete(condominio)
    db.commit()
    return {"message": "Condominio deleted successfully"}"""