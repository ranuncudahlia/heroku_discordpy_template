# Instructions
A template for loading a bot made in DiscordPy to Heroku. This also includes the instructions for how to set up your Heroku bot with basic deployment, no add-ons etc.

## 0. Table of Contents
1. Repository Directory
2. About Heroku
3. Deployment
4. Detailed File Exaplanaitions (Procfile, requirements.txt, runtime.txt)
5. Additional Information (Postgres, Console access & logging, misc. tips)
6. Credits

## 1. Repository Directory
* bot (folder): the folder for the python files. the Procfile designates this folder and reads "bot.py" so if you rename this folder or elect not to use it, ensure you update the Procfile as well
  * bot.py (python file): the file for our python bot. it includes some important notes that I recommend reviewing; however, they are also included further in these instructions. if you rename this file, make sure to update the Procfile accordingly.
* Procfile (file with **no extension**): the process file Heroku refers to when knowing what commands to run to start your bot. for our bot, we're using a worker dyno that runs the bot.py file in order to keep the bot online 24/7. if you change the bot file's name/directory, this needs to be updated. The Procfile does NOT have an extension, and will not run properly if one is included.
* README.md (markdown file): the readme, which is what you're reading right now. Feel free to delete or replace within your template. You can always refer back to [the template repository](https://github.com/ranuncudahlia/heroku_discordpy_template) for the instructions as you need them.
* requirements.txt (plain-text file): lists the package requirements for our bot (things such as pip and postgres are automatically included and do not need specification). Heroku looks at this to look at what to install, but it also looks at your bot file. It *also* is extremely important that this file is included, even if it is empty, because Heroku when deploying identifies your app requires Python if this file exists in your root directory.
* runtime.txt (plain-text file): lists the buildpack requirements for our bot. The example in this template uses python-3.6.12. If you need a different version, list it here. You can check which buildpack your app is using once it's deployed by going to the app page and viewing the Settings tab.

## 2. About Heroku
Heroku is a platform for deploying apps. In this case, we are using it to deploy our bot and keep it online, meaning we will not have to run our bot locally. I'm assuming if you're here you already are generally familiar with the concept of Heroku, or at least know why you want to use it. Just in case you want a refresher, or want some more information, here are some links that may be beneficial to have a look at:
* [Heroku's docs for Deploying Python and Django Apps on Heroku](https://devcenter.heroku.com/articles/deploying-python)
* [Heroku's Python Support docs](https://devcenter.heroku.com/categories/python-support)
* [Heroku's article "How Heroku Works"](https://devcenter.heroku.com/articles/how-heroku-works)
* [Heroku's guide for deploying Python apps](https://devcenter.heroku.com/articles/getting-started-with-python) *\*Note: these instructions are for CLI/Console deployment. The instructions I've included in this README use the web dashboard.

## 3. Deployment
We're going to assume you've already setup your bot profile, but if you haven't, here is the bare bones you will need to know in order to proceed:
1. While logged in to Discord on your browser (not the desktop application), go to the [Developer Portal](https://discord.com/developers/applications).
2. Create a new application. The name is not what will be displayed when the bot is connected to Discord.
3. Upload a profile picture if you so choose. Then go to the Bot tab and click create a bot. Accept the confirmation dialog that pops up.
4. Enter the username you would like your bot to have. This will be what will display in servers.
5. Make note of the Token section below the username box. You may want to copy it now to have on hand, or you may wait until later when it is needed.
6. To make it join your server, under OAuth2, select "Bot" as your scope, then select the Bot Permissions your bot will need. Copy the generated link and go to it using your browser, and invite the bot to your server. It will appear offline because we have not deployed it to Heroku yet.

We're going to setup our Heroku account first. Before you do so, make sure you have already cloned this template to your account and have named your repository accordingly. You do not yet need your .py file(s) to be uploaded to the repository; it will build succesfully following all of these steps.

#### 1. Create your account & app
Create your account [here](https://signup.heroku.com/). If you've already created an account, login to it. Note that free accounts can only have 1 active app at any time.

On your dashboard, you will create a new app. Name it whatever you want, so long as you are able to remember it and won't mind possibly writing it out as needed in the future using the console.

It will bring you to the deloy page, but leave this alone for now; we will come back to it later.

#### 2. Configure necessary settings.
While not *required* to deploy your app, I ***strongly encourage*** you to use Heroku's config variables in order to protect your bot's token key by not including it explicitly in your code. The commands you will need to include in your .py file are included in this template under bot/bot.py, with comments to indicate the purpose of each command.

To configure the environment variables, go to the Settings tab, then Reveal Config Vars. You'll add your bot's token key here. Our template uses the name DISCORD_BOT_TOKEN, but you can use whatever, so long as you make sure to use the correct name in your code.

Make note of this page, because this is the same page that will display your bot's buildpack, which you'll need to refer to in order to troubleshoot any buildpack errors *or* if you are using/updating a different version.

#### 3. Link to GitHub & Configure Initial Deployment
Back at the Deploy tab, under Deployment Method select GitHub. Connect your GitHub account to Heroku. If you decide you want to revoke this access, you can do so on GitHub's end in your repository's settings, under Webhooks.

When you have successfully connected to GitHub, you'll be prompted to search your repository name. Note that it will work even if your repository is private.

Once you've selected your repository, you'll configure your deployment settings. You can choose if you would like to automatically deploy updates. If you choose to do so, the bot will be deployed every time the repository has a new commit. If you do not do so, you may either manually push deployments from this page, or deploy manually using Heroku's CLI.

Select your deploy branch under manual deploy. By default, it will be the main branch. If you are following along with this template clean with no edited code, the deployment process will work successfully. To ensure that everything is deployed correctly, check the build log for these lines (*especially* the items bolded):

> **Python app detected**
> 
> **Installing \<*python version here*\>**
> 
> Installing pip 20.1.1, setuptools 47.1.1 and wheel 0.34.2
> 
> Installing SQLite3
> 
> Installing requirements with pip
> 
>    Collecting discord.py
> 
>      **Downloading discord.py-1.6.0-py3-none-any.whl (779 kB)**
> 
>    *\[redacted to save space\]*
> 
>    Installing collected packages: attrs, chardet, multidict, async-timeout, idna, typing-extensions, yarl, idna-ssl, aiohttp, **discord.py**
> 
>    Successfully installed aiohttp-3.7.3 async-timeout-3.0.1 attrs-20.3.0 chardet-3.0.4 **discord.py-1.6.0** idna-3.1 idna-ssl-1.1.0 multidict-5.1.0 typing-extensions-3.7.4.3 yarl-1.6.3
> 
> Discovering process types
> 
>    **Procfile declares types -> worker**
> 
> Compressing...
> 
>    Done: 41.4M
> 
> Launching...
> 
>    Released v3
> 
>    **\<*link to your bot's webapp here*\> deployed to Heroku**

#### 4. Finalize Deployment
Once your build is successful, nagivate to your Resources tab. You should have your worker which states what is in your Procfile. If you are using the template, this will be `worker python bot/bot.py`.

Click the edit/pencil button, then toggle the switch so that our worker is enabled and online. Make sure to click Confirm.

If you view your Discord bot in your server, you should now see that it is online. You may now edit/replace/etc your files as desired in the repository.

## 4. Detailed File Exaplanaitions (Procfile, requirements.txt, runtime.txt)
### **Procfile**
The Procfile defines our dyno, which is what keeps our bot running. Specifically, we are using a worker dyno; there are multiple other types that you can utilize if you are so inclined to do so. You can read more about Heroku's dynos [here](https://www.heroku.com/dynos), as well as pricing and descriptions of other dyno types.

An important note! Worker dynos run 24/7 if there is no Web dyno, which we did not deploy. This means that they are utilizing your account's free dyno hours 24/7. Free accounts by default have 550 hours per month. If you verify your account with a credit/debit card (no charge), this limit is increased to 1000 hours a month. Assuming you are going to want your bot to run at all times, you'll need a max of 744 hours a month (24 hours a day x 31 days in a month). Verifying your account means you will be able to run your bot for free without running out of hours, which is a good option if you are trying to avoid paying for hosting costs. However, be warned: some banks require that verifications use an actual monetary hold of at least $1.00 (USD) to verify your account. This is on a bank per bank basis and is not something Heroku has control over, so be aware that it may occur if you choose to do so. For more information about account verification, [here's Heroku's article about it](https://devcenter.heroku.com/articles/account-verification).

Heroku will also not charge you if you manage to run out of hours; your dynos will simply stop working until the next month begins. *However*, you can elect for higher tier dynos if you so choose. These are charged per second and billed at the end of the month. Heroku has [a neat pricing tool](https://www.heroku.com/pricing) where you can estimate your costs. This is mostly useful only if you are wanting to run multiple bots, as it grants you more hours; for example, $7 will allow you to run a "hobby dyno" alongside your 1000 free dyno hours. If your hobby dyno does not run this entire time, such as intentionally being placed offline or being downgraded, this is where you will be charged per second rather than the full amount.

To view your usage time for any dyno/bot, [go to your account settings under billing](https://dashboard.heroku.com/account/billing). It will list your current usage, as well as your platform credits, if you have purchased any.

One additional note related to our worker dyno: your bot will reboot once every day, usually around 11 PM GMT. This is normal and usually is not noticeable. In American time zones, that is around 3-6 PM.

### requirements.txt & runtime.txt
The requirements.txt file is run using `pip install -r`

Pip and Postgres come preinstalled with your Python deployment, so you do not need to include them here. 

A word of caution: files in your deployment space are refreshed every deployment, as well as once per day. They will not be persistent; this means leave your requirements in the file, even if they've already been installed once.

However, runtime.txt is not necessary. If you really wanted to avoid the process completely, you could manually select a buildpack under your app's settings. This is also how you will update your python version, should you choose to.

By default, as of this writing \[1/28/21\], Heroku uses python-3.6.12 even if there is no runtime.txt file. Importantly, even if new versions of python/pypy are released, your build will keep the version that it was deployed on. Heroku will notify you if it is significantly out of date, such as if they are no longer supporting certain versions. 

For more information about which python versions (including pypy) are supported, you can visit [Heroku's article](https://devcenter.heroku.com/articles/python-support#specifying-a-python-version).

## 5. Additional Information (Postgres, Console access & logging, tips & suggestions)
### Postgres
Heroku offers a free access to postgres by default with all apps deployed using the platform; you just need to enable the add-on and select a tier, which you can do on [the add-on page](https://elements.heroku.com/addons/heroku-postgresql). They have a great deal of information abotu connecting your Python app to the database. Important note: free accounts, including verified ones, are allowed up to 10,000 rows/records, an estimated downtime of 4 hours per month, and 1 GB storage. While they do not limit the number of schemas, they strongly advise against having more than 50 schemas, as it historically on the platform can cause operation problems for the owner's app, [such as disrupting or lagging Heroku's data backup mechanism](https://devcenter.heroku.com/articles/heroku-postgres-backups).

Data can also be accessed online using [the webUI](https://data.heroku.com/), meaning you can manage, configure, etc your databases outside of the Heroku CLI. You are also able to [access databases from outside Heroku/Heroku apps](https://devcenter.heroku.com/articles/connecting-to-heroku-postgres-databases-from-outside-of-heroku), meaning you can utilize Postbird or PGAdmin accordingly.

There is a limit of 20 connections at once; a [frequent mistake by Discord bot creators using Heroku & Postgres](https://stackoverflow.com/questions/64271688/my-discord-py-bot-always-loses-connection-to-my-mysql-database-on-heroku) is to not take into account that Discordpy uses async, which will utilize more connections than intended. Heroku recommends using PgBouncer to mitigate this; you can read Heroku's guide about it [here](https://devcenter.heroku.com/articles/python-concurrency-and-database-connections). Alternatively, you may only make your connections as needed, defined in each command, and close them as soon as the connection is no longer needed.

For more information in general about Heroku, Python, and Postgres in combination, you can reference the Heroku links below:
* [Postgres Guidelines](https://devcenter.heroku.com/articles/heroku-postgres-plans)
* [PostgreSQL add-on](https://elements.heroku.com/addons/heroku-postgresql)
* [Heroku PostgreSQL](https://devcenter.heroku.com/articles/heroku-postgresql)
  * From the same article as above, [Connecting in Python](https://devcenter.heroku.com/articles/heroku-postgresql#connecting-in-python)
* [Monitoring Heroku Postgres](https://devcenter.heroku.com/articles/monitoring-heroku-postgres)
* [PgBouncer Configuration](https://devcenter.heroku.com/articles/best-practices-pgbouncer-configuration)
* [Postgres Over Plan Capacity](https://devcenter.heroku.com/articles/heroku-postgres-over-plan-capacity)
* [Heroku Postgres Database Tuning](https://devcenter.heroku.com/articles/heroku-postgres-database-tuning)
* [Connection Pooling for Heroku Postgres](https://devcenter.heroku.com/articles/postgres-connection-pooling)
* [Heroku PGBackups](https://devcenter.heroku.com/articles/heroku-postgres-backups)


Not specifically Heroku-related, GitHub user [jegfish](https://github.com/jegfish) has [an example database connection](https://gist.github.com/jegfish/cfc7b22e72426f5ced6f87caa6920fd6) using the rewrite branch of discord.py.

### Console Access & Logging
Heroku's command-line can be accessed using the Heroku CLI, which effectively establishes a connection between your local command line and Heroku's. To utilize it, you need to install the Heroku CLI package from [here](https://devcenter.heroku.com/articles/getting-started-with-python#set-up).

There are a multitude of commands available, but the only one I would recommend which is not readily available from the online dashboard is the logging command line. This will give you insights into any crashes/errors that may occur after deploying your bot (particularly if you aren't testing your updates before deployment). Additionally, it can allow you to see the deployment process during updates, particularly if you are waiting for the bot to become fully online so that you may test or use new features with your update.

Once you've installed your Heroku CLI, open your command line. Enter `heroku login` to connect your Heroku account key to your local command environment. It will prompt you to press any key to open your default browser, where it will check Heroku to see if you are logged in, then grab your credentials. Once you have done so, you are now able to use any heroku command.

The main one you will use is `heroku logs --tail -a (your Heroku bot name here)`

It will effectively display the most recent lines of your bot's logs, loading in real time. Technically, you can access your account's logs via `heroku logs --tail` but by appending `-a (bot name)` you are specifying that you want to see the logs for that specific app.

This is *especially* critical since you are not able to access, create, or store any files with your bot hosting. Therefore, you cannot use the python logging module with your bot on the Heroku end.

### Miscellaneous Tips
This section may be updated in the future. These are additional tips and information I've found useful in the process of developing and deploying multiple bots using Heroku.

#### Using timed status messages
Let's say you want your bot to do that cool thing that you see other bots doing all the time: change its status message every X amount of time. Heroku is a little funky with how it processes this. Very large numbers, such as 15 minutes, will have either long delays or fail to run completely. (*On the free/hobby plans, at least. I have not tested this on higher tiers and don't plan to.*)

You'll want to make sure to limit your rotations to a smaller number, such as 1-5 minutes. I recommend setting your timer by using the asyncio package.

```python
## your status message code here
await asyncio.sleep(n) ## n = the length of time to wait in seconds
```
#### Alerting you/a specific channel when online
Maybe you want to be notified whenever the daily refresh occurs. Maybe you want to know when the bot comes online after a deployment. Maybe you're monitoring how long deployments take. Maybe you don't test your code before deploying and want to know when it's online so you can test it.

The hard way, but also the way built in to Heroku, is to use the Heroku CLI to monitor the logs of your bot. The easier way would be to program your bot on_ready to message a specific channel, such as a channel in your testing or support server. You'll need the target channel's ID, and if you are pinging someone (such as yourself), the user ID as well. It's up to you if you'd like to utilize a Heroku environment variable or not; I've had issues with it working in the past, and I don't find it particularly unsecure, since in order to post to a channel & ping a user, the bot/script in question would need to already have access to that channel and user anyway. You'll want to exercise a little more caution if this is in a support channel that anyone can join; I find that the best use case scenario is simply in a private channel which only you/your staff/etc have access to, or in a private server for development purposes.

To access the channel ID, make sure developer mode is turned on in Discord. Right-click your target channel and select "Copy ID."

To retrieve your user ID, right-click your name in the server members list and select "Copy ID." *Note: your user ID is the same across all of Discord, so you may or may not decide to store your ID visibly. You may instead want to utilize a command that retrieves Guild.owner if utilizing a server you own.*

```python
import discord
from discord.ext import commands # make sure you have the commands extension

bot = commands.Bot() # this is what I have the bot shorthanded as

@bot.event # make sure this is an event, not a command; if you already have on_ready currently, make sure to append the new code onto it, not create a new one
async def on_ready():
    channel = bot.get_channel(channel_ID_here) # the channel to post in; replace channel_ID_here with your desired channel
    await channel.send("<@user_ID_here> Bot is now online.") # send a message in the specified channel that pings the specified userID with the message
    # replace user_ID_here with your id. you MUST leave @ at the front and wrap it in <>
```

#### GitHub Student Developer Pack partnership with Heroku
If you are a student currently attending college/any other degree giving program, you can sign up for the [GitHub Student Developer Pack](https://education.github.com/pack), which includes one free hobby dyno up to two years. While the two years comes in the form of enough hobby dyno credits ($168) to last you that span of time, the amount of hobby dyno ($7) is deducted each month, whether or not you've used it. You also are still limited to only 1 hobby dyno. Therefore, before activating this offer, make sure you definitely want to utilize your two years at this point of time, particularly if you are still testing out bots and deciding what you want to do.

You can read more about Heroku's side of the partnership [here](https://www.heroku.com/github-students).

*(The GitHub student pack is also worth looking into just in general if you meet the eligibility, as it comes with a significant amount of development & coding resources in all flavors.)*

### 6. Credits
[Discord.py](https://discordpy.readthedocs.io/en/latest/index.html) created by [Rapptz](https://github.com/Rapptz)

Instructions & template, as well as any code within created by [Kendall Churchil](https://github.com/ranuncudahlia)
