import discord
from discord.ext import commands


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roast(self, ctx):
        await ctx.send(
            "🏴‍☠️ Even a Sea King has better navigation skills than you!"
        )


async def setup(bot):
    await bot.add_cog(Fun(bot))