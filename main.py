from fastapi import FastAPI

from app.v1.router.client_router import router as client_router
from app.v1.router.cuenta_router import router as cuenta_router

app = FastAPI()

app.include_router(client_router)
app.include_router(cuenta_router)