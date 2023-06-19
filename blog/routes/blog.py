# Standard Library
from typing import List

# Third Party Library
from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

# Local Library
from .. import models
from ..database import get_db
from ..schema import Blog, ShowBlog

router = APIRouter()


@router.post(path="/blog", status_code=status.HTTP_201_CREATED, tags=["blogs"])
def create(blog: Blog, db: Session = Depends(dependency=get_db)):
    new_blog = models.Blog(title=blog.title, body=blog.body, user_id=1)
    db.add(instance=new_blog)
    db.commit()
    db.refresh(instance=new_blog)
    return new_blog


@router.delete(
    path="/blog/{article_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["blogs"],
)
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


@router.get(path="/blog", response_model=List[ShowBlog], tags=["blogs"])
def all_fetch(db: Session = Depends(dependency=get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@router.get(
    "/blog/{article_id}",
    status_code=status.HTTP_200_OK,
    response_model=ShowBlog,
    tags=["blogs"],
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


@router.put(
    path="/blog/{article_id}",
    status_code=status.HTTP_202_ACCEPTED,
    tags=["blogs"],
)
def update(article_id, request: Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.article_id == article_id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {article_id} is not found.",
        )
    blog.update(requestd.dict())
    db.commit()
    return "Update completed."
