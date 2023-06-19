from fastapi import APIRouter, Depends, status, HTTPException
from .. import models
from ..schema import Login
from ..database import get_db
from ..hashing import Hash
from sqlalchemy.orm import Session

router = APIRouter(tags=["Auth"])


@router.post(path="/login")
def login(request: Login, db: Session = Depends(get_db)):
    user = (
        db.query(models.User)
        .filter(models.User.email == request.email)
        .first()
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials"
        )
    if not Hash.verify(user.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password"
        )
    return user