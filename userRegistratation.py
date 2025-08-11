from fastapi import FastAPI, HTTPException
from pydantic import BaseModel,EmailStr,StringConstraints,field_validator
from typing import Annotated,List

app = FastAPI(title= "User Registration API")

userDb = []

class userRequest(BaseModel):
    username: str
    email: EmailStr
    #password: Annotated[str,StringConstraints(min_length=8)]
    password: Annotated[str,str]

    @field_validator("password")
    def checkPasswordLength(cls,value):
        if len(value) < 8:
            raise ValueError("Password should be atleast 8 characters")  
        return value

@app.post("/register")
def registeredUser(data: userRequest):

    if any(user['email'] == data.email for user in userDb):
        raise HTTPException(status_code=400, detail="Email already registered")
    
    userDb.append(data.model_dump())
    return {"message":"user registered succesfully" , "user":data.username}

@app.get("/users",response_model=List[userRequest]) ## response_model will check wheather all fields are available or not 
def getUsers():
    return userDb


## curl command in cmd for post : curl -X POST "http://127.0.0.1:8000/register" ^ -H "Content-Type: application/json" ^ -d "{\"username\": \"sumit\", \"email\": \"sumit@example.com\", \"password\": \"mypassword123\"}"
## curl command in cmd to get registered users : curl -X GET "http://127.0.0.1:8000/users"