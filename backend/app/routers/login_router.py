import os
from dotenv import load_dotenv
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.exceptions import HTTPException
from typing import Annotated
from jose import jwt

# Configuracion inicial
load_dotenv()
login_router = APIRouter()
my_secret_key = str(os.getenv("SECRET_KEY"))
auth_bearer = OAuth2PasswordBearer(tokenUrl="/login/token")

users = {
    "daniel": {"username": "daniel", "password": "test123"},
    "santizo": {"username": "santizo", "password": "prueba456"},
}

def encode_token(payload: dict) -> str:
    token = jwt.encode(payload, my_secret_key, algorithm="HS256")
    return token

def decode_token(token: Annotated[str, Depends(auth_bearer)]) -> dict:
    data = jwt.decode(token, my_secret_key, algorithms=["HS256"])
    return data

@login_router.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = users.get(form_data.username)
    password = form_data.password
    if not user or user["password"] != password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    token = encode_token({"username": user["username"], "password": user["password"]})
    return {"access_token": token, "token_type": "bearer"}

@login_router.get("/me")
def profile(token: Annotated[str, Depends(auth_bearer)]):
    try:
        payload = decode_token(token)
        username = payload.get("username")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return {"username": username}
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")