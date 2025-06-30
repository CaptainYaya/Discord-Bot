import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parent / ".env"
print(f"Looking for .env at: {env_path}")

load_dotenv(dotenv_path=env_path)

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

print("DISCORD_TOKEN =", DISCORD_TOKEN)
print("OPENAI_API_KEY =", OPENAI_API_KEY)

