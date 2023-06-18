# Third Party Library
from fastapi import FastAPI

# Local Library
from .schema import Blog

app = FastAPI()


@app.post(path="/blog")
def create(blog: Blog) -> dict[str, Blog]:
    return {"data": blog}
