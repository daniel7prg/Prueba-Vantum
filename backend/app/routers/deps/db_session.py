from typing import Generator, Annotated
from sqlmodel import Session
from fastapi import Depends
from config.db_settings import engine

def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_db)]