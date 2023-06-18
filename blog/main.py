from fastapi import FastAPI

app = FastAPI()


class Blog:
    title: str
    body: str


@app.post(path="/blog")
def create(blog: Blog) -> dict[str, Blog]:
    return {"data": blog}
