from discord import Message, app_commands, user
from discord.ext import commands
import discord

message_scp = ("!xeroz", "!xeroze", "!infoxeroze")

class xeroze(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author == self.bot.user:
            return
        
        contenu = message.content.lower()

        if contenu in message_scp:
            await message.channel.send("xeroze est mon créateur si vous voulez le contacter pour un bot discorde ou autre vous pouvez lui envoyer un mp sur son compte fufuz ou xeroze. mais xeroze n'est pas mon seul créateur il y a aussi lepoteaufeu!!")
