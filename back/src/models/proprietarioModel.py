from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional

# Modelo para Proprietário
class Proprietario(SQLModel, table=True):
    cpf: str = Field(primary_key=True)
    nome_completo: str
    
    unidades: List[UnidadeCondominial] = Relationship(
        link_model=UnidadeProprietario, 
        back_populates="proprietarios"
    )
    