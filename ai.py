import openai
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")


def proompt(user_input, enemy, chat_history):
    built_up_messages = [{"role": "system", "content": enemy}]
    built_up_messages += chat_history
    built_up_messages.append({"role": "user", "content": user_input})  

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=built_up_messages,
        max_tokens=75,
    )
    return completion.choices[0].message