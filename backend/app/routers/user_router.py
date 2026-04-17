from fastapi import APIRouter
from models import User, UserCreateIn, UserCreateOut
from routers.deps import SessionDep
from sqlmodel import select
from typing import List
from jose import jwt
from dotenv import load_dotenv
import os

user_router = APIRouter()
load_dotenv()
my_secret_key = str(os.getenv("SECRET_KEY"))

@user_router.get("/")
def get_users(db: SessionDep) -> List[User]:
    statement = select(User)
    result = db.exec(statement).all()
    print(type(result))
    return list[User](result)

@user_router.post("/")
def create_user(user: UserCreateIn, db: SessionDep) -> UserCreateOut:
    user_obj = User(**user.model_dump())
    transform_password = user_obj.hashed_password
    transform_password = jwt.encode({"hashed_password": transform_password}, my_secret_key, algorithm="HS256")
    user_obj.hashed_password = transform_password
    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    return UserCreateOut(id=user_obj.id)