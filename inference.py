from fastapi import FastAPI
from pydantic import BaseModel
from env import RetailEnv

app = FastAPI()
env = RetailEnv()

# Dummy model (step endpoint)
class Action(BaseModel):
    task: str = "easy"
    response: str = ""

# ✅ RESET (must accept empty body)
@app.post("/reset")
def reset():
    state = env.reset()
    return {
        "state": state
    }

# ✅ STEP
@app.post("/step")
def step(action: Action):
    state, reward, done, info = env.step({
        "task": action.task,
        "response": action.response
    })

    return {
        "state": state,   # ⚠️ changed from next_state
        "reward": reward,
        "done": done,
        "info": info
    }
