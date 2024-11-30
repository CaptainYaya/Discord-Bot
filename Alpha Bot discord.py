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
    
    if message.content.startswith("Salut"):
        await message.channel.send("Salut, comment vas-tu ?")
    
    if message.content.startswith("Ca va ?"):
        await message.channel.send("Je vais bien et toi ?")

@client.command()
async def hello(ctx):
    await ctx.send("Salut je suis Alpha, le Fox Bot")



client.run("Bot Token :)")
