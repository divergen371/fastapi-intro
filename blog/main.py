# Third Party Library
from fastapi import FastAPI

# Local Library
from .database import engine
from .models import Base
from .schema import Blog

app = FastAPI()

Base.metadata.create_all(engine)


@app.post(path="/blog")
def create(blog: Blog) -> dict[str, Blog]:
    return {"data": blog}
