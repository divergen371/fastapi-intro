# Third Party Library
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# Local Library
from ..database import get_db
from ..fanctions import user
from ..schema import ShowUser, User

router = APIRouter(prefix="/user", tags=["users"])


@router.post(path="")
def create_user(request: User, db: Session = Depends(get_db)):
    return user.create(request=request, db=db)


@router.delete(path="/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return user.destroy(user_id=user_id, db=db)


@router.get(path="/{user_id}", response_model=ShowUser)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return user.show(user_id=user_id, db=db)


@router.get("", response_model=ShowUser)
def all_user(db: Session = Depends(get_db)):
    return user.all_user(db=db)
