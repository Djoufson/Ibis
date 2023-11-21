from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def generate_openai_advertisement(prompt:str, max_tokens=100) -> str:
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],

        model="gpt-3.5-turbo",
        max_tokens=max_tokens
    ).choices[0].message.content

    return response
