
import asyncio
import discord
from discord.ext import commands

token = ''  # Enter your bot token


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as {0} ({0.id})'.format(client.user))
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('*commands'):
            await message.channel.send('Use * and keywords "hello, How are you?, cat and history')
            print(f'Sent: commands')
        elif message.content.startswith('*hello'):
            await message.channel.send('Hello {0.author.mention}!'.format(message))
            print('Sent: hello')
        elif message.content.startswith('*How are you?'):
            await message.channel.send("It literally doesn't matter! I am a bot!")
            print('Sent: How are you?')
        elif message.content.startswith('*cat'):
            await message.channel.send('https://images.pexels.com/photos/730896/pexels-photo-730896.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940')
            print('Sent: cat')
        elif message.content.startswith('*history'):
            await message.channel.send('oof discord bot 2.0 got hacked so i was born... lets hope my creator learned his lesson smh')
            print('Sent: history')


client = MyClient()
client.run(token)
