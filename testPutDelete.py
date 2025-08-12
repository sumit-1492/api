from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title = "simple API for put and delete")

userDb = {
    1: {"name": "Sumit",   "age":33},
    2: {"name": "Dibyam", "age": 30},
    3: {"name": "Trupti" , "age":26}
}

class userClass(BaseModel):
    name: str
    age: int

@app.put("/userdb/database/v1/update/{user_id}")
def userUpdate(user_id:int,user:userClass):
    if user_id in userDb:
        userDb[user_id] = user.model_dump()
        print(userDb)
        return {"message" : "User updated succesfully" , "user":userDb[user_id]}
    else:
        return {"message" : "User not found"}
    

@app.delete("/userdb/database/v1/delete/{user_id}")
def userDelete(user_id:int,user:userClass):
    if user_id in userDb:
        del userDb[user_id]
        print(userDb)
        return {"message":"user deleted successfully"}
    else:
        return {"message" : "User not found"}