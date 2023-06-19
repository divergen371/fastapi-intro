# Standard Library
from typing import List

# Third Party Library
from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session

# Local Library
from ..database import get_db
from ..schema import Blog, ShowBlog, User
from ..fanctions import blog
from .. import oauth2

router = APIRouter(prefix="/blog", tags=["blogs"])


@router.post(path="", status_code=status.HTTP_201_CREATED)
def create(request: Blog, db: Session = Depends(dependency=get_db)):
    return blog.create(blog=request, db=db)


@router.delete(path="/{article_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(article_id: int, db: Session = Depends(get_db)):
    return blog.destroy(article_id=article_id, db=db)


@router.get(path="", response_model=List[ShowBlog])
def all_fetch(
    db: Session = Depends(dependency=get_db),
    current_user: User = Depends(oauth2.get_current_user),
):
    return blog.get_all(db=db)


@router.get(
    "/{article_id}",
    status_code=status.HTTP_200_OK,
    response_model=ShowBlog,
)
def show(article_id: int, response: Response, db: Session = Depends(get_db)):
    return blog.show(article_id=article_id, response=response, db=db)


@router.put(
    path="/{article_id}",
    status_code=status.HTTP_202_ACCEPTED,
)
def update(article_id, request: Blog, db: Session = Depends(get_db)):
    return blog.update(article_id=article_id, request=request, db=db)
