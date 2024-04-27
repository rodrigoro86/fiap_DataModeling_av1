from src.models.administradoraModel import AdministradoraModel, AdministradoraCreateModel
from core.deps import get_session
from sqlalchemy import select, update, delete


class AdministradoraCrud:
    async def create_administradora(self, administradora):

        async for session in get_session():
            db_administradora = AdministradoraModel(**administradora.dict())
            session.add(db_administradora)
            await session.commit()
            await session.refresh(db_administradora)
            
            return db_administradora

    async def get_administradoras(self):
        async for session in get_session():
            result = await session.execute(select(AdministradoraModel))
            return result.scalars().all()
    
    async def update_administradora(self, nome, administradora):
        async for session in get_session():
            stmt = (
                update(AdministradoraModel).
                where(AdministradoraModel.nome == nome).
                values(nome=administradora.nome)
            )
            result = await session.execute(stmt)
            await session.commit()
            if result.rowcount == 0:
                raise ValueError(f"No Administradora found with name {nome}")
            
            stmt = select(AdministradoraModel).where(AdministradoraModel.nome == administradora.nome)
            result = await session.execute(stmt)
            updated_administradora = result.scalars().first()

            return updated_administradora

    async def delete_administradora(self, nome):
        async for session in get_session():
            stmt = (
                delete(AdministradoraModel).
                where(AdministradoraModel.nome == nome)
            )
            result = await session.execute(stmt)
            await session.commit()

            if result.rowcount == 0:
                raise ValueError(f"No Administradora found with name {nome}")
            
            return True