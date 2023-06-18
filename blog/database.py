# Standard Library
from typing import Any

# Third Party Library
from sqlalchemy import Engine, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./blog.db"

engine: Engine = create_engine(
    url=DATABASE_URL, connect_args={"check_same_thread": False}
)

session_local = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base: Any = declarative_base()
