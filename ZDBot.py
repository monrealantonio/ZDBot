# ZDBot.py
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
BOT_PREFIX = ("!")

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} is now online!\n')
    for guild in client.guilds:
        print(
            f'{client.user.name} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})\n'
        )

@client.event
async def on_message(message):
    if message.author.bot:
        return
    elif message.content[0] == BOT_PREFIX:
        if message.content == '!roll':
            await on_roll(message)
        elif message.content.split(" ")[0] == '!secret':
            await message.delete()
            print(f'Message from {message.author.name} removed for... secret reasons.\n')
            await on_secret(message)


# !roll - Event for users wanting to roll
@client.event
async def on_roll(message):
    roll = random.randint(1,20)
    response = f'*{message.author.mention} has rolled a {roll}.*\n'
    await message.channel.send(response)
    print(f'{message.author.name} has rolled a {roll}.\n')

# !secret commands that update roles.
async def on_secret(message):
    id = client.get_guild(468206684834365441)
    secretRole = message.content.split(" ")[1]
    if secretRole == 'cheese-banana':
        role = discord.utils.get(id.roles, id=628819307853512705)
        await message.author.add_roles(role)
        print(f'{message.author.name} has become a Harlot!\n')
    elif secretRole == 'movietime':
        role = discord.utils.get(id.roles, id=631995695561441280)
        await message.author.add_roles(role)
        print(f'{message.author.name} is watching Movies!\n')

client.run(TOKEN)
