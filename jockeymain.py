import discord
import ffmpeg
from discord.ext import commands
import pyaudio

intents = discord.Intents.default()
bot = commands.Bot(command_prefix=",", intents=intents)
input_stream = ffmpeg.input('congo cut cut.mp3')

play = pyaudio.PyAudio()


@bot.event
async def on_ready():
    print("Test1")

@bot.command()
async def ping(ctx):
    print("Test2")
