import discord
from discord.ext import commands

import json
import os

from functions.master_import import *
from commands.master_cogs import *

with open("config.json") as jsfile:
    rawdata = json.load(jsfile)

# print(type(rawdata),rawdata)
from functions.startup_anim import startup_anim
from functions.console_logs import log_msg
os.system("clear")
startup_anim()

allintents = discord.Intents().all()
client = commands.Bot(intents=allintents, command_prefix="g>")


@client.event
async def on_ready():
    func_name = "on_ready"
    log_msg(func_name, "ReGonta is now connected !")
    log_msg(func_name, "Display name : " + client.user.display_name)
    log_msg(func_name, "ID : " + str(client.user.id))
    log_msg(func_name, "Num. of servers connected to : " +
            str(len(client.guilds)))
    guilds_str = ""
    for k in client.guilds:
        guilds_str += k.name
        if (k != client.guilds[-1]):
            guilds_str += " - "

    log_msg(func_name, "Servers connected to : " + guilds_str)
    await import_cogs(client)
    nb_sync = await client.tree.sync()
    log_msg(func_name, str(len(nb_sync)) + " commands has been synced")


client.run(rawdata["TOKEN"])
