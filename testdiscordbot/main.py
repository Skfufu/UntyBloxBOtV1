from dotenv import load_dotenv
from discord.ext import commands
from .commands.ban import Bancommand
from .commands.clear import ClearCommand
from .commands.kick import kickcommande
from .Message.BlackList import blacklist
from .Message.jeux_scp import jeuxscp
from .Message.cmds_infos import infoscommands
from .Message.infosxeroze import xeroze
from .Message.mapper import mapper
from .Message.dev import dev
from .Message.lepoteaufeu import lepoteaufeu
from .commands.deban import deBancommand
from .alive import alive
from .commands.muet import MuetCommand
import discord
import os


token = os.getenv("tokendiscord")
if token is None:
    raise ValueError("DISCORD_TOKEN n'est pas défini dans les variables d'environnement !")

class MonBot(commands.Bot):
    async def setup_hook(self):
        for extension in ['Bancommand', 'ClearCommand', 'kickcommande', 'infoscommands', 'xeroze', 'mapper', 'dev', 'lepoteaufeu', 'deBancommand', 'alive', 'MuetCommand']:
            await self.load_extension(f'commands.{extension}')
            await self.load_extension(f'Message.{extension}')


intents = discord.Intents.all()
bot = MonBot(command_prefix="!", intents=intents)

bot.run(token=token)









