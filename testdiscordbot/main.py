import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

# Charger les variables d'environnement depuis le .env
load_dotenv()
token = os.getenv("tokendiscord")
if token is None:
    raise ValueError("tokendiscord n'est pas défini dans les variables d'environnement !")

# Définir les extensions à charger
COMMAND_EXTENSIONS = ['Bancommand', 'ClearCommand', 'kickcommande', 'deBancommand', 'MuetCommand']
MESSAGE_EXTENSIONS = ['infoscommands', 'xeroze', 'mapper', 'dev', 'lepoteaufeu', 'alive']

# Création du bot
class MonBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        # Charger les extensions du dossier commands
        for ext in COMMAND_EXTENSIONS:
            await self.load_extension(f'testdiscordbot.commands.{ext}')

        # Charger les extensions du dossier Message
        for ext in MESSAGE_EXTENSIONS:
            await self.load_extension(f'testdiscordbot.Message.{ext}')

# Instancier le bot
bot = MonBot()

# Lancer le bot
bot.run(token)







