import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
client = commands.Bot(command_prefix= "/")

@client.event
async def on_ready():
    print(f'{client.user} se connecte sans problème !')

@client.event
async def on_message(message):
    if message.content.startswith("/test"):
       return
    
    if message.content.startswith("Salam aleykum"):
        await message.channel.send("Wa aleykum salam wa rahmatullahi wa barakatuh")
    
    if message.content.startswith("Cv ?"):
        await message.channel.send("Je vais bien hamdulillah et toi ?")

@client.command()
async def hello(ctx):
    await ctx.send("Salam aleykum je suis Alpha, le Fox Bot")



client.run("Bot Token :)")