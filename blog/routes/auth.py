# Third Party Library
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

# Local Library
from .. import models, token
from ..database import get_db
from ..hashing import Hash

router = APIRouter(tags=["Auth"])


@router.post(path="/login")
def login(
    request: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = (
        db.query(models.User)
        .filter(models.User.email == request.username)
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
    access_token = token.create_access_token(
        data={"sub": user.email, "id": user.user_id}
    )
    return {"access_token": access_token, "token_type": "bearer"}
