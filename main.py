import nextcord
from nextcord.ext.commands import Bot
from variablesfile import *

intents = nextcord.Intents.all()
intents.members = True




bot = Bot()

bot.load_extension("cogs.ping") #the file is in the cogs folder

bot.run(BotToken)