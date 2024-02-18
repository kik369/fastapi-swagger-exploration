# This file is for Pydantic models / schemas.
# Different from the SQLAlchemy models, these are used to validate data sent to the API.
# https://fastapi.tiangolo.com/tutorial/sql-databases/#create-the-pydantic-models

# schemas.py (Pydantic): This file defines Pydantic models, which are used for data validation, serialization, and documentation. Pydantic models don't interact with the database directly. Instead, they define the shape of the data that your API accepts and returns. When you receive data in a request, you can use a Pydantic model to validate the data and convert it into Python types. When you send data in a response, you can use a Pydantic model to convert the Python types into JSON.

# Pydantic models represent the structure of your data in HTTP requests and responses.

# The structure of the API as visible in the Swagger UI (or any other API documentation tool that FastAPI uses, like ReDoc) is defined by the Pydantic models.

from typing import List, Optional

from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None
    owner_id: int


class ItemCreate(BaseModel):
    title: str
    description: Optional[str] = None


class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True


# When you create a new instance of UserBase (or any model that inherits from UserBase) and don't provide a value for these fields, Pydantic will use the default values specified by Field().
class UserBase(BaseModel):
    email: str
    is_active: Optional[bool] = Field(True)
    is_staff: Optional[bool] = Field(False)
    is_premium: Optional[bool] = Field(False)
    is_superuser: Optional[bool] = Field(False)


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    items: List[Item] = []

    class Config:
        orm_mode = True
