# Third Party Library
from typing import Any, Generator
from fastapi import Depends, FastAPI, status
from sqlalchemy.orm import Session

# Local Library
from . import models
from .database import engine, session_local
from .models import Base
from .schema import Blog

app = FastAPI()

Base.metadata.create_all(engine)


def get_db() -> Generator[Session, Any, None]:
    db: Session = session_local()
    try:
        yield db
    finally:
        db.close()


@app.post(path="/blog", status_code=status.HTTP_201_CREATED)
def create(blog: Blog, db: Session = Depends(dependency=get_db)):
    new_blog = models.Blog(title=blog.title, body=blog.body)
    db.add(instance=new_blog)
    db.commit()
    db.refresh(instance=new_blog)
    return new_blog


@app.get(path="/blog")
def all_fetch(db: Session = Depends(dependency=get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.get("/blog/{article_id}")
def show(article_id: int, db: Session = Depends(get_db)):
    blog = (
        db.query(models.Blog)
        .filter(models.Blog.article_id == article_id)
        .first()
    )
    return blog
