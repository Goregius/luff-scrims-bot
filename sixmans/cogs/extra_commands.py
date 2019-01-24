import collections
import operator
import random
import time
from queue import Queue

import discord
from discord.ext import commands


def setup(bot):
    bot.add_cog(ExtraCommands(bot))


class ExtraCommands:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Says hello", aliases=["hi", "hey", "howdy", "bonjour", "hola", "hallo", "ciao", "namaste", "salaam", "zdras-tvuy-te", "konnichiwa"], pass_context=True)
    async def hello(self, ctx):
        greeting = 'Hello '
        if (ctx.message.author.name == "tdb"):
            greeting = 'Get lost '
        await self.bot.say(greeting + ctx.message.author.mention)
