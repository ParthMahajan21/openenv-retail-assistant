from fastapi import FastAPI
from pydantic import BaseModel
from env import RetailEnv

app = FastAPI()
env = RetailEnv()

# ✅ Request schema
class StepInput(BaseModel):
    task: str
    response: str = ""

# ✅ RESET endpoint (STRICT FORMAT)
@app.post("/reset")
async def reset():
    state = env.reset()
    return {
        "observation": state,   # 🔥 IMPORTANT (NOT "state")
        "info": {}
    }

# ✅ STEP endpoint (STRICT FORMAT)
@app.post("/step")
async def step(input: StepInput):
    state, reward, done, info = env.step({
        "task": input.task,
        "response": input.response
    })

    return {
        "observation": state,   # 🔥 IMPORTANT
        "reward": reward,
        "done": done,
        "info": info
    }
