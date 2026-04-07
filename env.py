from pydantic import BaseModel
from graders import grade_easy, grade_medium, grade_hard

class Observation(BaseModel):
    text: str

class Action(BaseModel):
    response: str

class RetailEnv:
    def __init__(self):
        self.task = None

    def reset(self, task="easy"):
        self.task = task

        if task == "easy":
            return Observation(text="Customer wants refund for damaged product")

        elif task == "medium":
            return Observation(text="Customer says: My order is delayed")

        elif task == "hard":
            return Observation(text="Sales Data: 100,200,NA,300, error, 500")

    def step(self, action: Action):
        if self.task == "easy":
            reward = grade_easy(action.response)

        elif self.task == "medium":
            reward = grade_medium(action.response)

        elif self.task == "hard":
            reward = grade_hard(action.response)

        done = True
        return Observation(text="Task completed"), reward, done, {}

    def state(self):
        return self.task