from env import RetailEnv
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

env = RetailEnv()

def run_task(task):
    prompt = f"Handle this retail task: {task}"

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    output = response.choices[0].message.content

    result = env.step({
        "task": task,
        "response": output
    })

    return output, result["reward"]


if __name__ == "__main__":
    tasks = ["easy", "medium", "hard"]

    for t in tasks:
        output, score = run_task(t)
        print(f"TASK: {t}")
        print(f"AI OUTPUT: {output}")
        print(f"SCORE: {score}")
        print("-----------")
