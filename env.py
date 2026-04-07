from pydantic import BaseModel

class Observation(BaseModel):
    text: str

class Action(BaseModel):
    response: str


class RetailEnv:
    def __init__(self):
        self.current_task = None

    def reset(self, task="easy"):
        self.current_task = task

        if task == "easy":
            return {"text": "Customer wants refund for damaged product"}

        elif task == "medium":
            return {"text": "Customer says: My order is delayed"}

        elif task == "hard":
            return {"text": "Sales Data: 100,200,NA,300,error,500"}

    def step(self, action):
        response = action.get("response", "").lower()

        reward = 0.0

        if self.current_task == "easy":
            if "refund" in response:
                reward = 1.0

        elif self.current_task == "medium":
            if "sorry" in response and ("help" in response or "assist" in response):
                reward = 1.0
            elif "sorry" in response:
                reward = 0.5

        elif self.current_task == "hard":
            if "clean" in response and "analysis" in response:
                reward = 1.0
            elif "clean" in response:
                reward = 0.5

        return {"text": "Task completed"}, reward, True, {}

    def state(self):
        return {"task": self.current_task}
