from typing import Optional,List
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from passlib.context import CryptContext


class Todo(BaseModel):
    title: str
    due_date: str
    description: str
class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    password: Optional[str] = None

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
app = FastAPI(title = "TODO API")

#CRUD Operations
store_todo = []
@app.get("/")
async def read_root():
    return {"Hello"}

#Create Operation
@app.post("/todo/")
async def create_todo(todo : Todo):
    store_todo.append(todo)
    return todo

#Read Operations
@app.get("/todo/", response_model=List[Todo])
async def get_todos_list():
    return store_todo
    
#Read Operations By id
@app.get('/todo/{id}')
async def get_todo(id:int):
    try:
        return store_todo[id]
    except:
        raise HTTPException(status_code = 404 , detail =" Todo not found")

#Update Operation
@app.put('/todo/{id}')
async def update_todo(id:int , todo : Todo):
    try:
        store_todo[id] = todo
        return store_todo
    except:
        raise HTTPException(status_code = 404 , detail =" Todo not found")

#  Delete Operation
@app.delete('/todo/{id}')
async def delete_todo(id:int):
    try:
        obj = store_todo[id]
        store_todo.pop(id)
        return obj
    except:
        raise HTTPException(status_code = 404 , detail =" Todo not found")

@app.post("/user/")
async def create_todo(user : User):
    hashedpwd = pwd_context.hash(user.password)
    return hashedpwd
       
