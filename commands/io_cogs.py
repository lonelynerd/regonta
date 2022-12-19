import json

from discord.ext import commands
from discord import app_commands
import discord

from functions.embed_logs import *
from functions.console_logs import *

with open("./config.json") as jsfile:
    rawdata = json.load(jsfile)


@app_commands.guild_only()
class InputOutput(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.log_ch = bot.get_channel(int(rawdata["LOG_GUILD"]["CHANNEL_ID"]))

    @app_commands.command(name="sidejack", description="Take control of the bot !")
    async def sidejack(self, ctx: discord.Interaction):
        func_name = "sidejack"
        await cmd_log(ctx.user, ctx.guild.name, func_name, "start", self.log_ch)
        await ctx.response.send_message("Starting the sidejack... Go back to your terminal !", ephemeral=True)
        log_msg(func_name, "Starting the sidejack in " +
                ctx.guild.name + "'s server...")
        while True:
            senttext = input("> ")
            if senttext == ":q":
                await cmd_log(ctx.user, ctx.guild.name, func_name, "end", self.log_ch)
                log_msg(func_name, "Ending the sidejack in " +
                        ctx.guild.name + "'s server...")
                return 0
            await ctx.channel.send(senttext)

    @app_commands.command(name="say", description="Let the bot say things.")
    async def say(self, ctx: discord.Interaction, arg: str):
        func_name = "say"
        await cmd_log(ctx.user, ctx.guild.name, func_name, arg, self.log_ch)
        await ctx.response.send_message("Sent !", ephemeral=True)
        log_msg(func_name, ctx.user.display_name +
                " announced something in " + ctx.guild.name + "'s server...")
        await ctx.channel.send(arg)

    @app_commands.command(name="listen", description="Fetch the last n messages.")
    async def listen(self, ctx: discord.Interaction, arg: int):
        func_name = "listen"
        messages = [message async for message in ctx.channel.history(limit=int(arg))]
        await cmd_log(ctx.user, ctx.guild.name, func_name, str(arg), self.log_ch)
        await ctx.response.send_message("Starting to listen to the "+str(arg)+" last messages... Go back to your terminal !", ephemeral=True)
        log_msg(func_name, "Starting to listen in " +
                ctx.guild.name + "'s server...")
        for k in range(len(messages) - 1, 0, -1):
            print(messages[k].author.name + " : \t\t"+messages[k].content)
        log_msg(func_name, "Ending to listen in " +
                ctx.guild.name + "'s server...")
