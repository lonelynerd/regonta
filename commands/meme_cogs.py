from discord.ext import commands
from discord import app_commands

import json
import os
import random

from functions.embed_logs import *
from functions.console_logs import *

with open("./config.json") as jsfile:
    rawdata = json.load(jsfile)


class Memes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.log_ch = bot.get_channel(int(rawdata["LOG_GUILD"]["CHANNEL_ID"]))

    @app_commands.command(name="meme", description="Show a random meme.")
    async def meme(self, ctx: discord.Interaction):
        func_name = "meme"
        await cmd_log(ctx.user, ctx.guild.name, func_name, None, self.log_ch)
        log_msg(func_name, ctx.user.display_name + " wants some memes...")
        path = "./memes/"
        files = os.listdir(path)
        if len(files) == 0:
            await ctx.response.send_message(
                "There's no images available... Sorry !", ephemeral=True)
            return 0
        filenrd = random.choice(files)
        with open(path + filenrd, "rb") as fh:
            f = discord.File(fh, filename=filenrd)
            embed = discord.Embed(title="Random meme", color=0xc061cb)
            embed.set_author(name="ReGonta -> "+ctx.user.display_name,
                             icon_url=ctx.user.display_avatar)
            embed.set_image(url="attachment://"+filenrd)
            await ctx.response.send_message(embed=embed, file=f)
