from core.exceptions import *
from sqlalchemy import text
from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.templating import Jinja2Templates
import requests
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from faker import Faker
import random
from app.services.session_manage import session_manager

fake = Faker()

# Generate a dataset of random sentences
dataset_size = 1000
dataset = [fake.sentence() for _ in range(dataset_size)]


templates = Jinja2Templates(directory="templates")

users = {
    "admin": {
        "password": "@hjdhs5756U7YG"
    }
}

security = HTTPBasic()
def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
    user = users.get(credentials.username)
    if not user or user["password"] != credentials.password:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return user

# Dictionary to store chat history for each session
chat_history = {}


class Chat:
    def __init__(self):
        self.session_history = {}
        ...
    
    async def unhelpful_chatbot(self, user_input: str, session_id: str):
        user = session_manager.get_user(session_id)
        if not user:
            raise HTTPException(status_code=401, detail="Invalid session ID")

        if session_id not in self.session_history:
            self.session_history[session_id] = []

        response = random.choice(dataset)

        self.session_history[session_id].append({"input": user_input, "response": response})
        return {"input": user_input, "response": response, "chat_history": self.session_history[session_id]}

    async def get_history(self, session_id: str):
        user = session_manager.get_user(session_id)
        if not user:
            raise HTTPException(status_code=401, detail="Invalid session ID")
        if session_id not in self.session_history:
            self.session_history[session_id] = []
        return {"chat_history": self.session_history[session_id]}
    


    