# Third Party Library
from fastapi import FastAPI

# Local Library
from .database import engine
from .models import Base
from .routes import auth, blog, user

app = FastAPI()
app.include_router(router=blog.router)
app.include_router(router=user.router)
app.include_router(router=auth.router)

Base.metadata.create_all(engine)
