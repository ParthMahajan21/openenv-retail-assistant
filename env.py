class RetailEnv:
    def __init__(self):
        self.current_task = None

    def reset(self):
        self.current_task = "easy"
        return {"task": self.current_task}

    def step(self, action):
        correct = {
            "easy": "refund",
            "medium": "delay",
            "hard": "analysis"
        }

        task = action.get("task")
        response = action.get("response", "").lower()

        reward = 1.0 if correct.get(task, "") in response else 0.0

        done = True
        return {"task": task}, reward, done, {}
