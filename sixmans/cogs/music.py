import collections
import operator
import random
import time
from queue import Queue

import discord
from discord.ext import commands
import youtube_dl


def setup(bot):
    bot.add_cog(MusicPlayer(bot))


class MusicPlayer:
    def __init__(self, bot):
        self.bot = bot
        self.player = None

    @commands.command(pass_context=True)
    async def play(self, ctx, *args):
        server = ctx.message.server
        author = ctx.message.author
        if len(args) == 1:
            url = args[0]
            voice_channel = author.voice_channel
            voice_channel = await self.bot.join_voice_channel(voice_channel)
            self.player = await voice_channel.create_ytdl_player(url)
            self.player.start()
        else:
            if self.player:
                self.player.resume()
            else:
                await self.bot.say("Nothing to play!")

    @commands.command(pass_context=True)
    async def pause(self, ctx):
        server = ctx.message.server
        self.player = self.players[server.id]
        self.player.pause()

    @commands.command(pass_context=True)
    async def stop(self, ctx):
        server = ctx.message.server
        if self.player:
            self.player.stop()
        else:
            await self.bot.say("Nothing to stop!")

    @commands.command(pass_context=True)
    async def leavechannel(self, ctx):
        server = ctx.message.server
        for voice_channel in self.bot.voice_clients:
            if voice_channel.server == ctx.message.server:
                return await voice_channel.disconnect()

        await self.bot.say("Not in a voice channel!")

