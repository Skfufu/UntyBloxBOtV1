from discord.ext import commands
from discord import app_commands
import discord
import asyncio #note : from discord import Message, app_commands, user
from discord.ext import commands
import discord

class kickcommande(commands.cog):
    def __init__(self, bot):
        self.bot = bot
    
@app_commands.command(name= "kick", description= "kick les personne")
async def kick(self, interactions:, user: discord.Member, time: int, raison: str = "aucune raison"):
        await interactions.response.defter(epherale=True)

        has_permission = interactions.user.guild_permissions.kick_members
        if not has_permission:
            await interactions.followup.send("vous n'avez pas les permission")
            return
        
        if time <= 0 or time > 20160:
            await interactions.followup.send(f"{time} est beaucoup trop grand ou trop petit")    
            return
        
        try:
             await interactions.guild.ban(user, reason=raison, delete_message_days=time)
             await interactions.response.send_message(f"{user} a été exclue pour {raison} pendant {time}")

             await asyncio.sleep(time *60)
             await interactions.guild.unban(user, reason= "fin du temps d'exclusion")
        
        except Exception as e:
             await interactions.response.send_message(f"{user} na pas pue etre exclue {e}")
        

        

