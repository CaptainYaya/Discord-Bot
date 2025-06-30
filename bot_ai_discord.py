import discord
import openai
import os
from pathlib import Path
from dotenv import load_dotenv

# Obtenir le chemin absolu du fichier `.env` dans le même dossier que ce script
env_path = Path(__file__).resolve().parent / ".env"
print(f"Looking for .env at: {env_path}")

# Charger le fichier .env
load_dotenv(dotenv_path=env_path)

# Lire les variables
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

print("DISCORD_TOKEN =", DISCORD_TOKEN)
print("OPENAI_API_KEY =", OPENAI_API_KEY)

if not DISCORD_TOKEN or not OPENAI_API_KEY:
    raise ValueError("Token Discord ou clé OpenAI manquants.")

openai.api_key = OPENAI_API_KEY

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Connecté en tant que {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("!ask"):
        prompt = message.content[5:]
        await message.channel.typing()
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Tu es un assistant Discord utile."},
                {"role": "user", "content": prompt}
            ]
        )
        reply = response["choices"][0]["message"]["content"]
        await message.channel.send(reply)

client.run(DISCORD_TOKEN)
