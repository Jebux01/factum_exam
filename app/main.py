import secure
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware

from app.api import healthcheck
from app.api.api_v1.api import api_router

secure_headers = secure.Secure()


tags_metadata = [
    {
        "name": "Calculos",
        "description": "Calculos en Fibonacci, Collatz, Factorial e IMC",
    },
    {
        "name": "Validaciones",
        "description": "Validar Fibonacci, Factorial, Primo y Palindromo",
    },
    {
        "name": "Operaciones",
        "description": "Calcular numeros aletarorios en iteraciones, Calculando Promedio, Suma, Minimo, Maximo y el rango",
    },
    {
        "name": "Conversiones",
        "description": "Conversiones de diferentes unidades de medida",
    },
]

fastapi_app = FastAPI(
    title="Examen Backend",
    description="API Examen",
    contact={
        "name": "Christian Gutierrez",
        "url": "https://www.linkedin.com/in/christian-gutierrez-371973176/",
        "email": "christiangtzv@gmail.com",
    },
    openapi_tags=tags_metadata
)


# Cors middleware
fastapi_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@fastapi_app.middleware("http")
async def set_secure_headers(request, call_next):
    """
    Secure headers middleware
    """
    response = await call_next(request)
    secure_headers.framework.fastapi(response)
    return response


fastapi_app.include_router(api_router, prefix="/api/v1")

app = fastapi_app
