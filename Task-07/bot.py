import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print("Bot is ready!")


async def load_extensions():
    await bot.load_extension("cogs.fun")
    await bot.load_extension("cogs.games")
    await bot.load_extension("cogs.economy")


async def main():
    async with bot:
        await load_extensions()

        # PUT YOUR BOT TOKEN INSIDE THE QUOTES
        await bot.start("MTU0Mjc5MjU5NDI1MjEwMzc2MA.Gn5eLp.6sELRpvGE-FsegTh9Kfcaxsefh4C29mDuS9REo")


import asyncio

asyncio.run(main())
