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


token = "token"

class MonBot(commands.Bot):
    async def setup_hook(self):
        for extension in ['Bancommand', 'ClearCommand', 'kickcommande', 'infoscommands', 'xeroze', 'mapper', 'dev', 'lepoteaufeu', 'deBancommand', 'alive', 'MuetCommand']:
            await self.load_extension(f'cogs.{extension}')

intents = discord.Intents.all()
bot = MonBot(command_prefix="!", intents=intents)

bot.run(token=token)



