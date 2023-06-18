# Third Party Library
from sqlalchemy import Column, Integer, String

# Local Library
from .database import Base


class Blog(Base):
    __tablename__: str = "blogs"

    article_id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
