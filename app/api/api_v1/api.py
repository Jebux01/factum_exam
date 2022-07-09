from fastapi import APIRouter, status

# from app.api.api_V1.endpoints import ( 
    
# )

from app.api.api_v1.endpoints import (
    calculates,
    conversions,
    operations,
    validations
)

api_router = APIRouter()

api_router.include_router(
    calculates.router,
    prefix="/calculos",
    tags=["Calculos"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)

api_router.include_router(
    conversions.router,
    prefix="/conversiones",
    tags=["Conversiones"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)

api_router.include_router(
    operations.router,
    prefix="/operaciones",
    tags=["Operaciones"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)

api_router.include_router(
    validations.router,
    prefix="/validaciones",
    tags=["Validaciones"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)