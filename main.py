#Pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI

app= FastAPI()

# Models

class User(BaseModel):
    pass

class Tweet(BaseModel):
    pass


@app.get(path="/")
def home():
    return {"Twitter API" : "Working!"}