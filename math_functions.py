from fastapi import FastAPI
from typing import Union

app = FastAPI()

@app.get("/add")
def add(a: Union[int, float], b: Union[int, float]):
    return {"result": a + b}
