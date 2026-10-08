import os

from dotenv import load_dotenv
from huggingface_hub import InferenceClient


load_dotenv()


def get_client():

    groq_key = os.getenv("GROQ_API_KEY")

    if not groq_key:
        raise ValueError("GROQ_API_KEY is not set.")

    return InferenceClient(
        api_key=groq_key,
        provider="groq"
    )


def generate_response(prompt, temperature=0.7, max_tokens=500):

    client = get_client()

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=temperature,
        max_tokens=max_tokens
    )

    return response.choices[0].message.content