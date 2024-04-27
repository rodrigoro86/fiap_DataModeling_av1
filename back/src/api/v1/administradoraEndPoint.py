from typing import List
from src.models.administradoraModel import AdministradoraModel, AdministradoraCreateModel
from src.db.administradoraCrud import AdministradoraCrud

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)


router = APIRouter()


# GET Cursos
@router.get('/', response_model=List[AdministradoraModel])
async def get_administradoras():
    administradora = AdministradoraCrud()
    return await administradora.get_administradoras()

# Post Administradora
@router.post('/', response_model=AdministradoraModel)
async def create_administradora(administradora: AdministradoraCreateModel):
    administradora_crud = AdministradoraCrud()
    return await administradora_crud.create_administradora(administradora)

# Update Administradora
@router.put('/{nome}', response_model=AdministradoraModel)
async def update_administradora(nome: str, administradora: AdministradoraCreateModel):
    administradora_crud = AdministradoraCrud()
    try: 
        return await administradora_crud.update_administradora(nome, administradora)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Administradora não encontrada")
    
# Delete Administradora
@router.delete('/{nome}')
async def delete_administradora(nome: str):
    administradora_crud = AdministradoraCrud()
    try: 
        if await administradora_crud.delete_administradora(nome):
            raise HTTPException(status_code=status.HTTP_200_OK, detail="Administradora deletada com sucesso")
    except ValueError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Administradora não encontrada")
    