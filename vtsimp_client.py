# vtsimpclient.py
# A vtsimpclient is an object that represents a connection to Discord
# A vtsimpclient handles events, tracks state, and generally interacts with Discord APIs

import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') # GET bot token data from github environment
GUILD = os.getenv('DISCORD_GUILD') # GET server name from data github environment

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following server:\n' # simple CLI message POST vtsimp as discord user
        f' - Server name: {guild.name}\n' # simple message POST discord server name
        f' - Server ID  : {guild.id}\n' # simple message POST discor server ID
    )

    members = '\n - '.join([member.name for member in guild.members]) # GET all discord member?
    print(f'Server Members:\n - {members}') # POST all member (output belum sesuai harapan])

client.run(TOKEN)