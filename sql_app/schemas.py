# This file is for Pydantic models / schemas.
# Different from the SQLAlchemy models, these are used to validate data sent to the API.
# https://fastapi.tiangolo.com/tutorial/sql-databases/#create-the-pydantic-models

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True
