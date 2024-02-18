from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# connect_args={"check_same_thread": False} is usedonly for sqlite
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Each instance of the SessionLocal class will be a database session.
# The class itself is not a database session.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Returns a class.
# This class will be used in models.py as a base class for database models.
Base = declarative_base()
