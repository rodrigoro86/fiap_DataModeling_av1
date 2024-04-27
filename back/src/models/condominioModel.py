from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
import importlib
from src.models.enderecoModel import EnderecoModel, EnderecoBase
from pydantic import BaseModel

# Modelo para Condominio
class CondominioModel(SQLModel, table=True):
    __tablename__ : str = "condominios"


    id: Optional[int] = Field(default=None, primary_key=True)
    situacao: str
      
    #unidades: List[UnidadeCondominial] = Relationship(back_populates="condominio")
    endereco_id: int = Field(foreign_key="enderecos.id")
    administradora_id: Optional[int] = Field(foreign_key="administradoras.id")
    #Arrume endereco 
    
    
    @property
    def administradora(self):
        AdministradoraModel = importlib.import_module("src.models.administradoraModel").AdministradoraModel
        return Relationship(back_populates="condominios", sa_relationship_kwargs={"model": AdministradoraModel})

    @property
    def endereco(self):
        EnderecoModel = importlib.import_module("src.models.enderecoModel").EnderecoModel
        return Relationship(back_populates="condominios", sa_relationship_kwargs={"model": EnderecoModel})
    

class CondominioBase(BaseModel):
    id: Optional[int]
    situacao: str
    endereco: EnderecoBase
    administradora_id: Optional[int]

    class Config:
        orm_mode = True