# Third Party Library
from typing import Any, Generator
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

# Local Library
from . import models
from .database import engine, session_local
from .models import Base
from .schema import Blog

app = FastAPI()

Base.metadata.create_all(engine)


def get_db() -> Generator[Session, Any, None]:
    db: Session = session_local()
    try:
        yield db
    finally:
        db.close()


@app.post(path="/blog")
def create(blog: Blog, db: Session = Depends(dependency=get_db)):
    new_blog = models.Blog(title=blog.title, body=blog.body)
    db.add(instance=new_blog)
    db.commit()
    db.refresh(instance=new_blog)
    return new_blog
