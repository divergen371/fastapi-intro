# Third Party Library
from fastapi import FastAPI

app = FastAPI()


@app.get(path="/")
def index() -> dict[str, dict[str, str]]:
    return {'data': {'name': 'Test'}}
