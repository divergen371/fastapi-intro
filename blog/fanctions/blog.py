# Third Party Library
from fastapi import HTTPException, status, Response
from sqlalchemy.orm import Session

# Local Library
from .. import models
from ..schema import Blog


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(blog: Blog, db: Session):
    new_blog = models.Blog(title=blog.title, body=blog.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def update(article_id: int, request: Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.article_id == article_id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {article_id} is not found.",
        )
    blog.update(request.dict())
    db.commit()
    return "Update completed."


def destroy(article_id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.article_id == article_id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {article_id} is not found",
        )
    blog.delete(synchronize_session=False)
    db.commit()

    return "Deletion of articles has been completed."


def show(article_id: int, response: Response, db: Session):
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
