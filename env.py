class RetailEnv:
    def __init__(self):
        self.tasks = ["easy", "medium", "hard"]
        self.current_task = None

    def reset(self):
        self.current_task = "easy"
        return {"task": self.current_task}

    def step(self, action):
        correct_answers = {
            "easy": "refund",
            "medium": "delay",
            "hard": "analysis"
        }

        task = action.get("task")
        response = action.get("response", "").lower()

        if correct_answers[task] in response:
            reward = 1.0
        else:
            reward = 0.0

        done = True
        next_state = {"task": task}

        return next_state, reward, done, {}
