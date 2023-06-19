# Third Party Library
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

# Local Library
from .database import Base


class Blog(Base):
    __tablename__: str = "blogs"

    article_id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)

    user_id = Column(Integer, ForeignKey(column="users.user_id"))
    creator = relationship("User", back_populates="blogs")


class User(Base):
    __tablename__: str = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = relationship("Blog", back_populates="creator")
