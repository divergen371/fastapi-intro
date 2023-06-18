# Standard Library
from typing import Any

# Third Party Library
from sqlalchemy import Engine, create_engine
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "sqlite:///./blog.db"

engine: Engine = create_engine(
    url=DATABASE_URL, connect_args={"check_same_thread": False}
)

Base: Any = declarative_base()
