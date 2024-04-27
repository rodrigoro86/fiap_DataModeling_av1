from src.db.administradoraCrud import AdministradoraCrud
from src.models.administradoraModel import AdministradoraModel
from asyncio import run


obj_administradora = AdministradoraCrud()

# Substitua os valores abaixo pelos dados reais da administradora que você deseja criar
administradora_data = {
    "nome": "Nome da Administradora",
    "endereco": "Endereço da Administradora",
    # Adicione aqui todos os outros campos necessários
}

administradora_model = AdministradoraModel(**administradora_data)

# 
# Cria a administradora

administradora = run(obj_administradora.create_administradora(administradora_model))

print(administradora)

print(run(obj_administradora.get_administradoras()))