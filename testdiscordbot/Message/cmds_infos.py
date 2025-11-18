from discord import Message, app_commands, user
from discord.ext import commands
import discord

message_scp = ("!cmds", "!command", "!commande", "!cmd", "!tout les commande")

class infoscommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author == self.bot.user:
            return
        
        contenu = message.content.lower()

        if contenu in message_scp:
            await message.channel.send("**!cmds = donne les commande, !jeux_scp ou !jeuxscp ou !jeux.scp = donne la description et le lienx du jeux nom du jeux complé")
