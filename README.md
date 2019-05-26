
Discord Bot/Voicebot

I obviously don't fully understand what i'm doing here yet
so i have two files one starts the voicebot and the other starts
the messaging bot. I split it because you can't do 

bot.run(token) and client.run(token) in the same file because only
the first one runs.

If for whatever reason you're here and actually read this you can 
clone this repo and hit that

pip install -r requirements.txt

and I recommend using a virtualenvironment.

Also you will have to run over to 
"https://discordapp.com/developers/applications/"
and start your own application and bot then get the bot's token and use that in each file.

To add the bot to your channels go to 

"https://discordapp.com/oauth2/authorize?client_id=ENTERYOURAPPLICATIONCLIENTID&scope=bot"

This was built using the Discord.py package

Github: "https://github.com/Rapptz/discord.py"
Docs: "https://discordpy.readthedocs.io/en/latest/"