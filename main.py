from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello"}


print("Hello World")
