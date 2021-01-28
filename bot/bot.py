### Bot file goes here. You can either upload your own or simply replace this file.
### If you upload your own file or rename the .py, make sure to change the directory location in our Procfile.

# For Heroku, make sure your .py includes the following.
import os # import the OS details, including our hidden bot token
token = os.environ.get('DISCORD_BOT_TOKEN') # fetch the token from Heroku's "OS" running the bot. make sure the name matches the one you've used on Heroku

# Include this at the end of your code. Instead of bot, you may have "discord.Client()" "commands.Bot()" etc, or whatever you have defined these.
bot.run(token) # make sure your token variable matches the token defined above
