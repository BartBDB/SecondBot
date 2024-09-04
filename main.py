import nextcord
from nextcord import Interaction
from nextcord.utils import get
from nextcord.ext import commands, tasks
from nextcord.ext import application_checks
from apikey import *

intents = nextcord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix='&', intents=nextcord.Intents.all())

@client.event
async def on_ready():
    print("Bot is ready to do useful shit!\n")

client.run(BOTTOKEN)