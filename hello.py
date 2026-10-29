"""Premier test : une question envoyée à l'API DeepSeek."""
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # charge le fichier .env (la clé n'est jamais écrite dans le code)

client = OpenAI(
    api_key=os.environ["DEEPSEEK_API_KEY"],
    base_url="https://api.deepseek.com",
)

reponse = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "user", "content": "Explique ce qu'est un conteneur Docker en 3 phrases."}
    ],
)
print(reponse.choices[0].message.content)
