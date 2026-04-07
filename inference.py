from fastapi import FastAPI
from pydantic import BaseModel
from env import RetailEnv

app = FastAPI()
env = RetailEnv()

class Action(BaseModel):
    task: str
    response: str = ""

@app.post("/reset")
def reset():
    state = env.reset()
    return {"state": state}

@app.post("/step")
def step(action: Action):
    state, reward, done, info = env.step(action.dict())
    return {
        "next_state": state,
        "reward": reward,
        "done": done,
        "info": info
    }
