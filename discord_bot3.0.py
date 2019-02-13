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
        tmp = await client.send_message(message.channel, 'Use * and keywords "hello, earth, cat, hacked, deleteme and How are you?')
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
    elif message.content.startswith('*deleteme'):
        msg = await client.send_message(message.channel, 'I will delete myself now...')
        await client.delete_message(msg)
    elif message.content.startswith('*cat'):
        counter = 0
        x = 0
        while x < 16:
            tmp = await client.send_message(message.channel, "https://images.pexels.com/photos/730896/pexels-photo-730896.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940")
            print(f'worked {x}')
            x += 1
            if x >= 16:
                print(f'Finished. Printed {x} times.')
                break
    elif message.content.startswith('*history'):
        counter = 0
        tmp = await client.send_message(message.channel, "oof discord bot 2.0 got hacked so i was born... lets hope my creator learned his lesson smh")
        print('worked')
    
    

client.run('')