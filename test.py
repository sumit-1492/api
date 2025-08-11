from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/sumit")
def add(a:int,b:int):
    return a+b

# class substractclass(BaseModel):
#     a:int
#     b:int

# def sub(a:int,b:int):
#     return a-b

# @app.post("/sub")
# def sub_num(model:substractclass):
#     return sub(model.a,model.b)

# print(add(1,2))

class subtractmodel(BaseModel):
    a: int
    b: int


def subtract(a:int,b:int):
    return a-b

@app.post("/kumar")
def subtract_numbers(model: subtractmodel):
    return subtract(model.a, model.b)

print(add(3,4))
