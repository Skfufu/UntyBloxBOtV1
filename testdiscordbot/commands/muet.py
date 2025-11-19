import discord
from discord.ext import commands
from discord import app_commands, Interaction
import asyncio
import datetime

class MuetCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="muet", description="Mute un membre pour une durée donnée (en minutes).")
    async def muet(self, interaction: discord.Interaction, user: discord.Member, duree: int, raison: str = "aucune raison"):
        await interaction.response.defer(ephemeral=True)

        # Vérification des permissions
        if not interaction.user.guild_permissions.mute_members:
            await interaction.followup.send("Vous n'avez pas la permission de mute des membres.", ephemeral=True)
            return

        # Vérification du temps
        if duree <= 0 or duree > 4320:
            await interaction.followup.send(f"La durée {duree} est invalide (doit être entre 1 et 4320 minutes).", ephemeral=True)
            return

        try:
            
            await user.edit(timeout=discord.utils.utcnow() + datetime.timedelta(minutes=duree), reason=raison)
            await interaction.followup.send(f"{user.mention} a été mute pendant {duree} minutes pour : {raison}")

           
            await asyncio.sleep(duree * 60)
            await user.edit(timeout=None, reason="Fin automatique du mute")

        except Exception as e:
            await interaction.followup.send(f"Erreur : impossible de mute {user}. ({e})", ephemeral=True)


    
 

    




