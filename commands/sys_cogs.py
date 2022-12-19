from discord.ext import commands
from discord import app_commands

import json

from functions.embed_logs import *
from functions.console_logs import *

with open("./config.json") as jsfile:
    rawdata = json.load(jsfile)


class System(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.log_ch = bot.get_channel(int(rawdata["LOG_GUILD"]["CHANNEL_ID"]))

    @app_commands.command(name="exit", description="Shut down the bot.")
    async def exit(self, ctx: discord.Interaction):
        func_name = "exit"
        await cmd_log(ctx.user, ctx.guild.name, func_name, None, self.log_ch)
        log_msg(func_name, "The bot is shutting down...")
        await ctx.response.send_message("The bot is shutting down...", ephemeral=True)
        exit(0)

    @app_commands.command(name="info", description="Show some infos about the bot.")
    async def info(self, ctx: discord.Interaction):
        func_name = "info"
        await cmd_log(ctx.user, ctx.guild.name, func_name, None, self.log_ch)
        log_msg(func_name, "Gathering info...")
        embed = discord.Embed(title="ReGonta's status", url="https://github.com/lonelynerd/gonta-bot",
                              description="ReGonta is the successor of Gonta, a bot that went through a chaotic development... But that time is no more !", color=0x1c71d8)
        embed.set_author(name="ReGonta -> "+ctx.user.display_name,
                         icon_url=ctx.user.display_avatar)
        embed.add_field(name="Display name",
                        value=self.bot.user.display_name, inline=False)
        embed.add_field(name="ID", value=self.bot.user.id, inline=False)
        embed.add_field(name="Num. of guilds", value=str(
            len(self.bot.guilds)), inline=False)
        embed.add_field(name="Num. of commands", value=str(
            rawdata["NB_COMMS"]), inline=False)
        embed.add_field(name="Version", value=str(len(self.bot.commands)), inline=False)
        embed.set_thumbnail(url=self.bot.user.display_avatar)
        await ctx.response.send_message(embed=embed)
