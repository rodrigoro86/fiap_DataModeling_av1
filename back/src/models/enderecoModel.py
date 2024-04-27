from sqlmodel import SQLModel, Field, Relationship
from pydantic import BaseModel
from typing import List, Optional


# Modelo para Endereço
class EnderecoModel(SQLModel, table=True):
    __tablename__ : str = "enderecos"
    id: Optional[int] = Field(default=None, primary_key=True)
    logradouro: str
    numero: int
    complemento: Optional[str] = None
    bairro: str
    cidade: str
    estado: str
    cep: str
    
class EnderecoBase(BaseModel):
    rua: str
    numero: int
    complemento: Optional[str]
    bairro: str
    cidade: str
    estado: str
    pais: str
    cep: str