import discord
import ffmpeg
from discord.ext import commands


intents = discord.intents.default()
intents.message.content = True
bot = commands.Bot(command_prefix=",", intents=intents)

@bot.event
async def on_ready():
    print("Test1")

@bot.command()
async def ping(ctx):
    print("Test2")
