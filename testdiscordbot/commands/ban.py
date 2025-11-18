from discord.ext import commands
from discord import User, app_commands
import discord

class Bancommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


@app_commands.command(name="ban", description="ban les personne")
async def ban(self, interaction, user: discord.Member, raison: str = "aucune raisson"): 
    await interaction.response.defer(ephemeral=True)


    has_permission = interaction.user.guild_permissions.ban_members
    if not has_permission:
        await interaction.followup.send("vous n'avais pas les permission")
        return
    

    try:
        await user.ban(reason=raison)
        await interaction.response.send_message(f"{user} a été banni pour {raison}")

    except Exception as e:

        await interaction.response.response.send_message(f"{User} est imposible a bannire : {e}", ephemeral=True)


