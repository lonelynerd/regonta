import discord
import datetime

async def cmd_log(user,serv,cmd,args,ctx):
    embed=discord.Embed(title="LOG - "+cmd, description="User "+ user.display_name +" used a command !", color=0xff197a)
    file = discord.File("cases/"+cmd+".png", filename=cmd+".png")
    embed.set_author(name="ReGonta -> "+user.display_name,icon_url=user.display_avatar)
    #print("attachment://./cases/"+cmd+".png"
    embed.add_field(name="User", value=user.display_name, inline=True)
    embed.add_field(name="User's ID", value=user.id, inline=True)
    embed.add_field(name="Server", value=serv, inline=False)
    embed.add_field(name="Command", value=cmd, inline=True)
    embed.set_thumbnail(url="attachment://"+cmd+".png")
    if args != None:
        embed.add_field(name="Arguments", value=args, inline=True)
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed,file=file)