import os
from sqlmodel import create_engine
from dotenv import load_dotenv

load_dotenv()

POSTGRES_SERVER=os.getenv("POSTGRES_SERVER")
POSTGRES_PORT=os.getenv("POSTGRES_PORT")
POSTGRES_DB=os.getenv("POSTGRES_DB")
POSTGRES_USER=os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD=os.getenv("POSTGRES_PASSWORD")

db_url = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

engine = create_engine(url=db_url)