### Bot file goes here. You can either upload your own or simply replace this file.
### If you upload your own file or rename the .py, make sure to change the directory location in our Procfile.

# For Heroku, make sure your .py includes the following.
import os # import the OS details, including our hidden bot token
token = os.environ.get('DISCORD_BOT_TOKEN') # fetch the token from Heroku's "OS" running the bot. make sure the name matches the one you've used on Heroku
