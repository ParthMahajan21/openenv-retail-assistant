from fastapi import FastAPI

app = FastAPI()

@app.post("/reset")
def reset():
    return {}

@app.post("/step")
def step(input: dict):
    task = input.get("task", "").lower()

    if task == "easy":
        return {"output": "This is a refund request", "score": 1.0}
    elif task == "medium":
        return {"output": "Sorry for the delay, we will help you", "score": 1.0}
    elif task == "hard":
        return {"output": "Clean data and provide analysis insight", "score": 1.0}

    return {"output": "Invalid task", "score": 0.0}
