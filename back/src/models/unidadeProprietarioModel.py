from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional

# Tabela de relacionamento muitos para muitos entre Unidade Condominial e Proprietário
class UnidadeProprietario(SQLModel, table=True):
    unidade_id: Optional[int] = Field(foreign_key="unidade_condominial.id", primary_key=True)
    proprietario_id: str = Field(foreign_key="proprietario.cpf", primary_key=True)