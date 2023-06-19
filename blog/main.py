# Standard Library
from typing import Any, Generator, List

# Third Party Library
from fastapi import Depends, FastAPI, HTTPException, Response, status
from sqlalchemy.orm import Session

# Local Library
from . import models
from .database import engine, session_local
from .hashing import Hash
from .models import Base
from .schema import Blog, ShowBlog, User, ShowUser

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


@app.delete(path="/blog/{article_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(article_id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.article_id == article_id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {article_id} is not found",
        )
    blog.delete(synchronize_session=False)
    db.commit()

    return "Deletion of articles has been completed."


@app.get(path="/blog", response_model=List[ShowBlog])
def all_fetch(db: Session = Depends(dependency=get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.get(
    "/blog/{article_id}",
    status_code=status.HTTP_200_OK,
    response_model=ShowBlog,
)
def show(article_id: int, response: Response, db: Session = Depends(get_db)):
    blog = (
        db.query(models.Blog)
        .filter(models.Blog.article_id == article_id)
        .first()
    )
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {article_id} is not found.",
        )
    return blog


@app.put(path="/blog/{article_id}", status_code=status.HTTP_202_ACCEPTED)
def update(article_id, request: Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.article_id == article_id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {article_id} is not found.",
        )
    blog.update(request.dict())
    db.commit()
    return "Update completed."


@app.post(path="/user")
def create_user(request: User, db: Session = Depends(get_db)):
    new_user = models.User(
        name=request.name,
        email=request.email,
        password=Hash.crypt(request.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get(path="/user/{user_id}", response_model=ShowUser)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with the id {user_id} is not found.",
        )
    return user
