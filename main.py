import os
from dotenv import load_dotenv
import discord
from interactions import slash_command, SlashContext
import zipfile
import asyncio

# Load environment variables from .env file
load_dotenv()

# Retrieve the bot token from an environment variable
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Initialize the bot
intents = discord.Intents.default()
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@slash_command(name="archive", description="Archive the last 100 messages in the current text channel.")
async def archive(ctx: SlashContext, channel: discord.TextChannel = None):
    if channel is None:
        channel = ctx.channel

    # Create a temporary text file to store messages
    with open(f"{channel.name}.txt", "w", encoding="utf-8") as f:
        async for message in channel.history(limit=100):
            f.write(f"{message.author}: {message.content}\n")

    # Create a ZIP file
    zip_path = f"{channel.name}.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(f"{channel.name}.txt")

    # Send ZIP file
    await ctx.send("Here is the archive:", file=discord.File(zip_path))

    # Clean up temporary files
    os.remove(f"{channel.name}.txt")
    os.remove(zip_path)

# Run the bot
bot.run(TOKEN)
