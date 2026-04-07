from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# -------- Request Schema --------
class StepInput(BaseModel):
    task: str

# -------- RESET ENDPOINT --------
@app.post("/reset")
def reset():
    return {}

# -------- STEP ENDPOINT --------
@app.post("/step")
def step(input: StepInput):
    task = input.task.lower()

    if task == "easy":
        return {
            "output": "This is a refund request",
            "score": 1.0
        }

    elif task == "medium":
        return {
            "output": "Sorry for the delay, we will help you",
            "score": 1.0
        }

    elif task == "hard":
        return {
            "output": "Clean data and provide analysis insight",
            "score": 1.0
        }

    else:
        return {
            "output": "Invalid task",
            "score": 0.0
        }
