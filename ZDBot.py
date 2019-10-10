# ZDBot.py
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} is now online!\n')
    for guild in client.guilds:
        print(
            f'{client.user.name} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})\n'
        )

# !roll command
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    roll = random.randint(1,21)
    if message.content == '!roll':
        response = f'*{message.author.name} has rolled a(n) {roll}. {message.author.mention}*'
        await message.channel.send(response)

client.run(TOKEN)
