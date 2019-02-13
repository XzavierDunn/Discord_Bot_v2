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
    if message.content.startswith('*commands'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Use * and keywords "hello, earth, and How are you?')
        print('worked')
    elif message.content.startswith('*hello'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Hello!')
        print('worked')
    elif message.content.startswith('*earth'):
        counter = 0
        tmp = await client.send_message(message.channel, 'https://images.pexels.com/photos/2422/sky-earth-galaxy-universe.jpg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940')
        print('worked')
    elif message.content.startswith('*How are you?'):
        counter = 0
        tmp = await client.send_message(message.channel, "It literally doesn't matter! I am a bot!")
        print('worked')
    
    

