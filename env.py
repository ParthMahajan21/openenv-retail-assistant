class RetailAssistantEnv:
    def __init__(self):
        self.task = None

    def reset(self):
        return {}

    def step(self, action):
        task = action.get("task", "").lower()

        if task == "easy":
            return {
                "observation": "This is a refund request",
                "reward": 1.0,
                "done": True
            }

        elif task == "medium":
            return {
                "observation": "Sorry for the delay, we will help you",
                "reward": 1.0,
                "done": True
            }

        elif task == "hard":
            return {
                "observation": "Clean data and provide analysis insight",
                "reward": 1.0,
                "done": True
            }

        return {
            "observation": "Invalid task",
            "reward": 0.0,
            "done": True
        }
