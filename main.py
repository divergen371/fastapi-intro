# Standard Library
from typing import Any, Optional

# Third Party Library
from fastapi import FastAPI
from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    description: str
    published_at: Optional[bool]


app = FastAPI()


@app.get(path="/")
def index() -> dict[str, dict[str, str]]:
    return {"data": {"name": "Test"}}


@app.get(path="/about")
def about() -> dict[str, set[str]]:
    return {"data": {"About page"}}


@app.get(path="/blog")
def item(limit: int = 10, published: bool = True) -> dict[str, str]:
    if published:
        return {"data": f"{limit}件"}
    else:
        return {"data": "非公開"}


@app.post(path="/blog")
def create_blog(blog: Blog) -> dict[str, Blog]:
    return {"data": blog}


@app.get(path="/blog/category")
def category() -> dict[str, str]:
    return {"data": "all category"}


@app.get(path="/blog/{article_id}")
def show(article_id: int) -> dict[str, Any]:
    """
    docstring
    """
    return {"data": article_id}


@app.get(path="/blog/{article_id}/comments")
def comments(article_id: int, limit: Optional[str] = None) -> dict[str, set]:
    """
    docstring
    """
    return {"data": {article_id, limit, "comments"}}
