from env import RetailEnv

env = RetailEnv()

def run():
    for task in ["easy", "medium", "hard"]:
        obs = env.reset(task)

        if task == "easy":
            action = {"response": "refund request"}
        elif task == "medium":
            action = {"response": "sorry we will help you"}
        else:
            action = {"response": "clean data and analysis"}

        obs, reward, done, _ = env.step(action)

        print(f"Task: {task}")
        print(f"Score: {reward}")

if __name__ == "__main__":
    run()
