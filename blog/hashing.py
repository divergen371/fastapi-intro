# Third Party Library
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:
    def crypt(password: str):
        return pwd_context.hash(password)

    def verify(user_password, request_password):
        return pwd_context.verify(request_password, user_password)
