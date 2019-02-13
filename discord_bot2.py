import discord
import asyncio
from PIL import Image



client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('*hello'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Hello!')
        print('worked')
    

client.run('NTQ1MDc2NDkyOTgwMTkxMjUy.D0UZlQ.BaWOinzliIX_O1p9rLeGGkmsxDQ')