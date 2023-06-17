# Third Party Library
from fastapi import FastAPI

myapp = FastAPI()


@myapp.get(path="/")
def index() -> dict[str, dict[str, str]]:
    return {"data": {"name": "Test"}}


@myapp.get(path="/about")
def about() -> dict[str, set[str]]:
    return {"data": {"About page"}}
