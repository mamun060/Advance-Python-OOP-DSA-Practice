from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

users = [] 

class User(BaseModel):
    id: int 
    name: str
    email: str
    age: int

@app.get("/users")
def get_users():
    return users

@app.post("/users", response_model=User)
def create_user(user: User):
    for u in users:
        if u.id == user.id:
            raise HTTPException(status_code=400, detail="User ID already exists")
    users.append(user)
    return user


@app.get('/user/{user_id}', response_model=User)
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.put('/user/{user_id}', response_model=User)
def update_user(user_id: int, update_user: User):
    for index, user in enumerate(users):
        if user.id == user_id:
            users[index] = update_user
            return update_user
    raise HTTPException(status_code=404, detail="User not found")

@app.delete('/user/{user_id}')
def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user.id == user_id:
            del users[index]
            return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")

