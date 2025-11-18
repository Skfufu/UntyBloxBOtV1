from dotenv import load_dotenv
from discord.ext import commands
from testdiscordbot.commands.ban import Bancommand
from testdiscordbot.commands.clear import ClearCommand
from testdiscordbot.commands.kick import kickcommande
from testdiscordbot.Message.BlackList import blacklist
from testdiscordbot.Message.jeux_scp import jeuxscp
from testdiscordbot.Message.cmds_infos import infoscommands
from testdiscordbot.Message.infosxeroze import xeroze
from testdiscordbot.Message.mapper import mapper
from testdiscordbot.Message.dev import dev
from testdiscordbot.Message.lepoteaufeu import lepoteaufeu
from testdiscordbot.commands.deban import deBancommand
from testdiscordbot.alive import alive
from testdiscordbot.commands.muet import MuetCommand
import discord
import os


load_dotenv()
token = os.getenv("DISCORD_BOT_TOKEN")
prefix = os.getenv("DISCOR_COMMANDS_PREFIX")

class Mybot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(command_prefix=prefix, intents=intents)
    
    async def setup_hook(self):
        await self.add_cog(ClearCommand)
        await bot.add_cog(Bancommand)
        await bot.add_cog(kickcommande)
        await self.add_cog(blacklist)
        await self.add_cog(jeuxscp)
        await self.add_cog(infoscommands)
        await self.add_cog(xeroze)
        await self.add_cog(mapper)
        await self.add_cog(dev)
        await self.add_cog(lepoteaufeu)
        await self.add_cog(deBancommand)
        await self.add_cog(MuetCommand)
        await self.tree.sync()

    
    async def on_ready(self):
        print(f'Bot connecté sur {self.user} (ID: {self.user.id})')
        print('------')


alive()

bot = Mybot()

bot.run(token)