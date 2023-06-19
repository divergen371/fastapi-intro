from typing import Optional
from datetime import datetime, timedelta
from jose import jwt
from jose.exceptions import JWTError
from .schema import TokenData
from sqlalchemy.orm import Session
from .fanctions.user import show

SECRET_KEY = "86cbacac5b899ec6071f8ded298fdaf805f92d24699b6fc77c7757fe6d6e9b2b"
ALGORITHM = "HS256"
ACCESS_TOKE_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = expires_delta + datetime.utcnow()
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=ACCESS_TOKE_EXPIRE_MINUTES
        )
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt


def verify_token(token: str, credentials_exception, db: Session):
    try:
        payload = jwt.decode(
            token=token, key=SECRET_KEY, algorithms=[ALGORITHM]
        )
        email: str = payload.get("sub")
        user_id: int = payload.get("id")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception

    user = show(user_id, db)
    return user
