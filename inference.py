from fastapi import FastAPI
from pydantic import BaseModel
from env import RetailEnv
from openai import OpenAI
import os

app = FastAPI()
env = RetailEnv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class Action(BaseModel):
    task: str
    response: str = ""

@app.post("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: Action):
    state, reward, done, info = env.step(action.dict())
    return {
        "state": state,
        "reward": reward,
        "done": done,
        "info": info
    }
