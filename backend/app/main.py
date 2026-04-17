from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import Response, JSONResponse
from config import engine
from models import User
from routers import login_router, user_router
from sqlmodel import SQLModel

# Configuracion inicial
app = FastAPI()
SQLModel.metadata.create_all(engine)

@app.middleware("http")
async def log_requests(request: Request, call_next) -> Response | JSONResponse:
    print(f"Incoming request: {request.method} {request.url}")
    response = await call_next(request)
    print(f"Response status: {response.status_code}")
    return response

app.include_router(prefix="/login", router=login_router, tags=["login"])
app.include_router(prefix="/users", router=user_router, tags=["users"])