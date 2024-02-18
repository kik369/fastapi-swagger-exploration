from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, text
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

    # default: This is a Python-side default value. It's used when you create a new instance of the model in Python and don't provide a value for this column. SQLAlchemy will use this default value when inserting the new row into the database.
    is_active = Column(Boolean, default=True)
    is_staff = Column(Boolean, default=False)
    is_premium = Column(Boolean, default=False)

    # server_default: This is a server-side default value. It's used when a new row is inserted into the database and no value is provided for this column. The database itself will use this default value. It's also used when the column is added to an existing table during a migration.
    is_superuser = Column(Boolean, default=False, server_default=text("false"))

    # in sqlalchemy, the relationsip needs to be established from both sides
    # unlike in Django where the relationship is established from one side
    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    # relationsip needs to be established from both sides
    owner = relationship("User", back_populates="items")
