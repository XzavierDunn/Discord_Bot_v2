
import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import find


token = ''  # Enter your bot token


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as {0} ({0.id})'.format(client.user))
        print('------')

client = MyClient()


@client.event
async def on_ready():
    channel = client.get_channel()  # Enter your channel id
    await channel.send('')  # send a message to your chat when this file loads

client.run(token)
