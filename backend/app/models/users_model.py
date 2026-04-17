from sqlmodel import SQLModel, Field

class UserBase(SQLModel):
    username: str = Field(max_length=50, unique=True)
    email: str = Field(max_length=100, unique=True)
    hashed_password: str = Field(max_length=255)
    user_type: str = Field(max_length=20)

class UserCreateIn(UserBase): ...

class UserCreateOut(SQLModel):
    id: int = Field()

class User(UserBase, table=True):
    id: int = Field(default=None, primary_key=True)