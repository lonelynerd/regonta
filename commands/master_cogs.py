from commands.io_cogs import *
from commands.sys_cogs import *
from commands.meme_cogs import *


async def import_cogs(bot):
    await bot.add_cog(InputOutput(bot))
    await bot.add_cog(System(bot))
    await bot.add_cog(Memes(bot))
