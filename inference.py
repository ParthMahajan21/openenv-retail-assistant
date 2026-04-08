from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/reset")
def reset():
    return {}

@app.post("/step")
def step(data: dict):
    task = data.get("task", "").lower()

    if task == "easy":
        return {"observation": "This is a refund request", "reward": 1.0, "done": True}
    elif task == "medium":
        return {"observation": "Sorry for the delay, we will help you", "reward": 1.0, "done": True}
    elif task == "hard":
        return {"observation": "Clean data and provide analysis insight", "reward": 1.0, "done": True}

    return {"observation": "Invalid task", "reward": 0.0, "done": True}
