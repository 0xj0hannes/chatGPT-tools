import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ.get("API_KEY")

def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    return image_url

def main():
    while True:
        message = input(">>> ")
        if message == "exit":
            break
        try:
            url = generate_image(message)
            print(f"URL: {url}")
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
