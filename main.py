import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

# Load environment variables from .env file
load_dotenv()

# Retrieve the bot token from an environment variable
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Initialize the bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

# Your bot commands here




# Run the bot
bot.run(TOKEN)
