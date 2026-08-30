import discord
from discord.ext import commands
import random


class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def coinflip(self, ctx):
        result = random.choice(["Heads", "Tails"])
        await ctx.send(f"🪙 {result}!")

    @commands.command()
    async def roll(self, ctx):
        number = random.randint(1, 6)
        await ctx.send(f"🎲 You rolled a {number}!")


async def setup(bot):
    await bot.add_cog(Games(bot))