# Standard Library
from typing import List

# Third Party Library
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

# Local Library
from .. import models
from ..database import get_db
from ..hashing import Hash
from ..schema import ShowUser, User

router = APIRouter()


@router.post(path="/user", tags=["users"])
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


@router.get(path="/user/{user_id}", response_model=ShowUser, tags=["users"])
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with the id {user_id} is not found.",
        )
    return user


@router.get("/user", response_model=List[ShowUser], tags=["users"])
def all_user(db: Session = Depends(get_db)):
    user = db.query(models.User).all()
    return user
