import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ.get("API_KEY")

model = "gpt-3.5-turbo"

messages = [ {"role": "system", "content":
			"You are a intelligent assistant."} ]

def generate_response(messages, model):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
    )
    message = response.choices[0].message.content
    return message

def main():
    while True:
        message = input("You : ")
        if message == "exit":
            break
        messages.append(
            {"role": "user", "content": message},
        )
        reply = generate_response(messages, model)
        print(f"ChatGPT: {reply}")
        messages.append({"role": "assistant", "content": reply})

if __name__=='__main__':
    main()
