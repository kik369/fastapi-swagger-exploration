from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


# These classes are the SQLAlchemy models.
# They describe the database tables and their properties.
# Akin to Django's models.py
class User(Base):
    __tablename__ = "users"  # name of the table to use in the database for each of these models

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    # in sqlalchemy, the relationsip needs to be established from both sides
    # unlike in Django where the relationship is established from one side
    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
