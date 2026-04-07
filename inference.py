from fastapi import FastAPI
from env import RetailEnv

app = FastAPI()
env = RetailEnv()

# ✅ RESET
@app.post("/reset")
def reset():
    state = env.reset()
    return {
        "observation": state,
        "info": {}
    }

# ✅ STEP
@app.post("/step")
def step(action: dict):
    state, reward, done, info = env.step(action)

    return {
        "observation": state,
        "reward": reward,
        "done": done,
        "info": info
    }
