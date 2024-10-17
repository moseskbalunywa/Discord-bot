import discord
from discord.ext import commands

# Define bot prefix
bot = commands.Bot(command_prefix="!")

# Event to check when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Example command
@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

# Run the bot with your token
bot.run('I WONT SHARE MY TOKEN ON THIS PLATFORM')
