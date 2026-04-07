from fastapi import FastAPI
from env import RetailEnv

app = FastAPI()
env = RetailEnv()

@app.post("/reset")
def reset():
    state = env.reset()
    return {"state": state}

@app.post("/step")
def step(action: dict):
    state, reward, done, info = env.step(action)
    return {
        "state": state,
        "reward": reward,
        "done": done,
        "info": info
    }
