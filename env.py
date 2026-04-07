class RetailEnv:
    def __init__(self):
        self.tasks = ["easy", "medium", "hard"]

    def reset(self):
        return {"task": "easy"}

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

        return {
            "reward": reward,
            "done": True,
            "info": {}
        }
