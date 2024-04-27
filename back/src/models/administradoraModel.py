from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from pydantic import BaseModel
import importlib

# Modelo para Administradora
class AdministradoraModel(SQLModel, table=True):
    __tablename__ : str = "administradoras"

    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str = Field(max_length=100, nullable=False, unique=True)

    condominio_id: Optional[int] = Field(foreign_key="condominios.id")
    
    @property
    def condominios(self):
        CondominioModel = importlib.import_module("src.models.condominioModel").CondominioModel
        return Relationship(back_populates="administradoras", sa_relationship_kwargs={"model": CondominioModel})


# Modelo para Administradora
class AdministradoraBase(BaseModel):
    nome: str = Field(max_length=100, nullable=False, unique=True)
    condominio_id: Optional[List[int]]

