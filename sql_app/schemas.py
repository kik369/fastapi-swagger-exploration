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
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int
    owner: "User"  # This is a forward reference. It allows you to reference the User model before it's actually defined. This is necessary for the relationship between User and Item, because they both reference each other. You can use a string with the name of the model, as a string, inside quotes. This is a special syntax that tells Pydantic that it's a forward reference. It's not a string, it's a reference to a model that will be defined later.

    # You can customize the behavior of your Pydantic models by defining a Config class inside your model. This allows you to control things like whether fields are required by default, whether unknown fields are allowed, and how fields are serialized.
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
