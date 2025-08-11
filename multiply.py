from fastapi import FastAPI
from pydantic import BaseModel,field_validator
from typing import Any

app = FastAPI()

class multiplyRequest(BaseModel):

    a: Any
    b: Any

    @field_validator("a","b")
    def checkIntegers(cls,value):
        if not isinstance(value,int):
            raise ValueError("value must be an integer")
        return value
    

@app.post("/multiply")
def multiplyNumbers(data:multiplyRequest):
    result = data.a * data.b
    return {"a": data.a, "b":data.b, "result":result}


### windows curl command for command prompt - curl -X POST "http://127.0.0.1:8000/multiply" ^ -H "Content-Type: application/json" ^ -d "{\"a\": 7, \"b\": 4}"