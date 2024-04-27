from fastapi import APIRouter

from src.api.v1 import administradoraEndPoint, condominioEndPoint


api_router = APIRouter()
api_router.include_router(administradoraEndPoint.router, prefix='/administradoras', tags=['administradoras'])
api_router.include_router(condominioEndPoint.router, prefix='/condominios', tags=['condominios'])
