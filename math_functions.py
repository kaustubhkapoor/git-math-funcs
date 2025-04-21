from fastapi import FastAPI
from typing import Union

app = FastAPI()

@app.get("/add")
def add(a: Union[int, float], b: Union[int, float]):
    return {"result": a + b}

@app.get("/multiply")
def multiply(a: Union[int, float], b: Union[int, float]):
    return {"result": a * b}

#//division

@app.get("/divide")
def divide(a: Union[int, float], b: Union[int, float]):
    if b == 0:
        return {"error": "Division by zero is not allowed"}
    return {"result": a / b}

@app.get("square_root")
def square_root(a: Union[int, float]):
    return {"result": a**2}

@app.get("/subtraction")
def subtraction(a: Union[int, float], b: Union[int, float]):
    return {"result": a - b}