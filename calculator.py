from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
from typing import Any, Literal

app = FastAPI()

class calculatorRequest(BaseModel):

    a: Any
    b: Any
    operation: Literal["add", "subtract", "multiply", "divide"]

    @field_validator("a","b")
    def checkIntegers(cls, value):
        if not isinstance(value, (int,float)):
            raise ValueError("value must be a number of type interger or float")
        return value
    

@app.post("/calculator")
def calculator(data: calculatorRequest):

    a,b, operation = data.a, data.b, data.operation

    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b == 0:
            raise HTTPException(status_code=400, detail="Divison By Zero Is Not Allowed")
        result = a/b
    else:
        raise HTTPException(status_code=400, detail="Invlid Operation")
    
    return {"a":a, "b":b, "operation": operation, "result":result}


## curl command in cmd : curl -X POST "http://127.0.0.1:8000/calculator" ^ -H "Content-Type: application/json" ^ -d "{\"a\": 7, \"b\": 7, \"operation\": \"divide\"}"



