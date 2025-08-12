from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title = " simple API for put and delete")

userDb = {
    1: {"name": "Sumit",   "age":33},
    2: {"name": "Dibyam", "age": 30},
    3: {"name": "Trupti" , "age":26}
}

