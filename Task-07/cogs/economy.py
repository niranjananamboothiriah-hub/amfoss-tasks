import discord
from discord.ext import commands
from datetime import datetime, timedelta

import database


class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def balance(self, ctx):
        """Show your current Berry balance."""
        user_id = str(ctx.author.id)
        username = str(ctx.author)

        balance = database.get_balance(user_id, username)

        await ctx.send(
            f"🍓 {ctx.author.mention}, your Berry balance is **{balance}**!"
        )

    @commands.command()
    async def daily(self, ctx):
        """Claim 100 Berry once every 24 hours."""
        user_id = str(ctx.author.id)
        username = str(ctx.author)

        last_daily = database.get_last_daily(user_id, username)

        if last_daily:
            last_time = datetime.fromisoformat(last_daily)
            next_claim = last_time + timedelta(hours=24)
            remaining = next_claim - datetime.now()

            if remaining.total_seconds() > 0:
                hours = int(remaining.total_seconds() // 3600)
                minutes = int((remaining.total_seconds() % 3600) // 60)

                await ctx.send(
                    f"⏳ You already claimed your daily Berry!\n"
                    f"Try again in **{hours}h {minutes}m**."
                )
                return

        database.change_balance(user_id, username, 100)
        database.set_last_daily(user_id, username)

        balance = database.get_balance(user_id, username)

        await ctx.send(
            f"🍓 You received **100 Berry**!\n"
            f"Your new balance is **{balance} Berry**."
        )

    @commands.command()
    async def leaderboard(self, ctx):
        """Show the richest users."""
        users = database.get_top_users(10)

        if not users:
            await ctx.send("🍓 No users are on the leaderboard yet!")
            return

        message = "🏆 **Berry Leaderboard** 🏆\n\n"

        for position, (username, balance) in enumerate(users, start=1):
            message += (
                f"**{position}.** {username} — 🍓 **{balance}**\n"
            )

        await ctx.send(message)

    @commands.command()
    async def rob(self, ctx, member: discord.Member):
        """Try to steal Berry from another user."""
        if member.bot:
            await ctx.send("❌ You cannot rob a bot!")
            return

        if member.id == ctx.author.id:
            await ctx.send("❌ You cannot rob yourself!")
            return

        robber_id = str(ctx.author.id)
        robber_name = str(ctx.author)

        target_id = str(member.id)
        target_name = str(member)

        last_rob = database.get_last_rob(robber_id, robber_name)

        if last_rob:
            last_time = datetime.fromisoformat(last_rob)
            next_rob = last_time + timedelta(hours=1)
            remaining = next_rob - datetime.now()

            if remaining.total_seconds() > 0:
                minutes = int(remaining.total_seconds() // 60)

                await ctx.send(
                    f"⏳ You need to wait **{minutes} minutes** before "
                    f"robbing someone again."
                )
                return

        target_balance = database.get_balance(target_id, target_name)

        if target_balance <= 0:
            await ctx.send(
                f"❌ {member.mention} has no Berry to rob!"
            )
            return

        import random

        amount = random.randint(10, min(50, target_balance))

        database.change_balance(target_id, target_name, -amount)
        database.change_balance(robber_id, robber_name, amount)
        database.set_last_rob(robber_id, robber_name)

        new_balance = database.get_balance(robber_id, robber_name)

        await ctx.send(
            f"🏴‍☠️ {ctx.author.mention} robbed **{amount} Berry** "
            f"from {member.mention}!\n"
            f"🍓 Your new balance is **{new_balance} Berry**."
        )


async def setup(bot):
    await bot.add_cog(Economy(bot))