# app.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import sys

# Add bots directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), "bots"))

from PersonalizedGenie import run_personalized_genie
from FirstBot import run_first_bot
from SecondBot import run_second_bot

app = FastAPI()

class PersonalizedRequest(BaseModel):
    name: str
    goal: str
    message: str

class SimpleMessageRequest(BaseModel):
    message: str

@app.post("/personalized")
def call_personalized_genie(req: PersonalizedRequest):
    try:
        result = run_personalized_genie(req.name, req.goal, req.message)
        return {"response": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/firstbot")
def call_first_bot(req: SimpleMessageRequest):
    try:
        result = run_first_bot(req.message)
        return {"response": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/secondbot")
def call_second_bot(req: SimpleMessageRequest):
    try:
        result = run_second_bot(req.message)
        return {"response": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))