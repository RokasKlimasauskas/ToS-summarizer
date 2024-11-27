import openai
from dotenv import load_dotenv
import os

# Loading environment variables from .env file
"""load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')"""

def generate_text(prompt):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
