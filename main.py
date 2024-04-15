import discord
from discord.ext import commands
import os
import sys
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    guild = bot.get_guild(739233428683096144)
    channelID = guild.get_channel(1229038944889344081)
    await channelID.send('hello')
    await load()

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'cogs.{filename[:-3]}')
                print('now loaded '+filename)
            except:
                print('failed to load '+filename)

bot.run(os.getenv('token'))
