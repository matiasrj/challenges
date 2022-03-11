from fastapi import FastAPI

from app.v1.router.client_router import router as client_router
app = FastAPI()

app.include_router(client_router)