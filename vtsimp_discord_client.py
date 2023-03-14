import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following server:\n'
        f' - Server name: {guild.name}\n'
        f' - Server ID  : {guild.id}\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Server Members:\n - {members}')

client.run(TOKEN)