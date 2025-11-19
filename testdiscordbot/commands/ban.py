import discord
from discord.ext import commands
from discord import app_commands

class Bancommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ban", description="Ban une personne")
    async def ban(
        self, interaction: discord.Interaction, user: discord.Member, raison: str = "aucune raison"):
        await interaction.response.defer(ephemeral=True)

        # Vérifier les permissions
        if not interaction.user.guild_permissions.ban_members:
            await interaction.followup.send("Vous n'avez pas la permission de bannir.", ephemeral=True)
            return

        # Tenter de bannir
        try:
            await user.ban(reason=raison)
            await interaction.followup.send(f"{user} a été banni pour : {raison}", ephemeral=True)

        except Exception as e:
            await interaction.followup.send(f"Impossible de bannir {user} : {e}", ephemeral=True)



