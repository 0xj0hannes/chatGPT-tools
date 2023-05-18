import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ.get("API_KEY")

def generate_response(prompt, model):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = response.choices[0].text.strip()
    return message

def main():
    model = "text-davinci-002"
    while True:
        prompt = input(">>> ")
        if prompt == 'exit':
            break
        response = generate_response(prompt, model)
        print(response)

if __name__=='__main__':
    main()
