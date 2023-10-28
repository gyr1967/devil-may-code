import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "hello UwU."},
    {"role": "user", "content": "you are a spooky ghost, say something."}
  ]
)

print(completion.choices[0].message)