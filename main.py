# Standard Library
from typing import Any

# Third Party Library
from fastapi import FastAPI

app = FastAPI()


@app.get(path="/")
def index() -> dict[str, dict[str, str]]:
    return {"data": {"name": "Test"}}


@app.get(path="/about")
def about() -> dict[str, set[str]]:
    return {"data": {"About page"}}


@app.get(path="/blog/{id}")
def show(id: int) -> dict[str, Any]:
    """
    docstring
    """
    return {"data": id}
