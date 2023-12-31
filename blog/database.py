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

session_local = sessionmaker(bind=engine, autoflush=False)

Base: Any = declarative_base()


def get_db():
    """
    docstring
    """
    db = session_local()

    try:
        yield db
    finally:
        db.close()
