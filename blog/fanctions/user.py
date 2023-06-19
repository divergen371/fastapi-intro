from fastapi import status, HTTPException
from .. import models
from ..schema import User
from sqlalchemy.orm import Session
from ..hashing import Hash


def create(request: User, db: Session):
    new_user = models.User(
        name=request.name,
        email=request.email,
        password=Hash.crypt(request.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def show(user_id: int, db: Session):
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with the id {user_id} is not found.",
        )
    return user


def all_user(db: Session):
    user = db.query(models.User).all()
    return user
