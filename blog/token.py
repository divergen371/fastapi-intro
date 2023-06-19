from typing import Optional
from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "86cbacac5b899ec6071f8ded298fdaf805f92d24699b6fc77c7757fe6d6e9b2b"
ALGORITHM = "HS256"
ACCESS_TOKE_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """ """
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
