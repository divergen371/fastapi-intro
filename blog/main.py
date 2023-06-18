from fastapi import FastAPI

app = FastAPI()


@app.post(path="/blog")
def create():
    return "create"
