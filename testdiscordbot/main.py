from dotenv import load_dotenv
from discord.ext import commands
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
        await self.tree.sync()

    
    async def on_ready(self):
        print(f'Bot connecté sur {self.user} (ID: {self.user.id})')
        print('------')


alive()

bot = Mybot()


bot.run(token)

