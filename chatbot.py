import os
from openai import OpenAI

API_KEY = os.getenv("API_KEY")

client = OpenAI(
    base_url="https://api.aimlapi.com/v1",
    api_key=API_KEY
)

context = """
You are an AI assistant named AIO.
You answer in Persian.
Be short and helpful.
"""

while True:
    user_input = input("User: ")

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": user_input}
        ],
        stream=True
    )

    for chunk in response:
        if chunk.choices and chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="")
    print()
