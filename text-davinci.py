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
        try:
            response = generate_response(prompt, model)
            print(response)
        except openai.error.APIError as e:
            #Handle API error here, e.g. retry or log
            print(f"OpenAI API returned an API Error: {e}")
            pass
        except openai.error.APIConnectionError as e:
            #Handle connection error here
            print(f"Failed to connect to OpenAI API: {e}")
            pass
        except openai.error.RateLimitError as e:
            #Handle rate limit error (we recommend using exponential backoff)
            print(f"OpenAI API request exceeded rate limit: {e}")
            pass

if __name__=='__main__':
    main()
