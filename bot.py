import discord
from discord.ext import commands
import random
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

RESPONSES = [
    "Praaaaowww!!!",
    "prrr...",
    "MREEEOWW!!",
    "Prrrw??"
]

@bot.event
async def on_ready():
    print(f'Logged in successfully as {bot.user.name}!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if bot.user.mentioned_in(message):
        random_reply = random.choice(RESPONSES)
        await message.reply(random_reply)

bot.run(os.environ.get('DISCORD_TOKEN'))
