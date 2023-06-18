from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Blog(BaseModel):
    title: str
    body: str


@app.post(path="/blog")
def create(blog: Blog) -> dict[str, Blog]:
    return {"data": blog}
