from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from src.model.condominioModel import Condominio

# Modelo para Unidade Condominial
class UnidadeCondominial(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    bloco: str
    numero: int
    metros_quadrados: int
    numero_de_comodos: int
    condominio_id: int = Field(foreign_key="condominio.id")

    condominio: Optional[Condominio] = Relationship(back_populates="unidades")
