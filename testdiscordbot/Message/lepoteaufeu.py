from discord import Message, app_commands, user
from discord.ext import commands
import discord

message_scp = ("!lepoteaufeu", "legoatlepoteaufeu")

class lepoteaufeu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author == self.bot.user:
            return
        
        contenu = message.content.lower()

        if contenu in message_scp:
            await message.channel.send("Aaaa lepoteaufeu, mon cofondateur (enfin plutôt mon fondateur originale) sans lui je n'aurais j'amais pue exister, sais lui qui a apris à xeroze a dev")
