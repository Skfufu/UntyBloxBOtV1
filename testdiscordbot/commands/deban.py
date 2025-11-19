from discord.ext import commands
from discord import User, app_commands, Interaction
import discord

class deBancommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @app_commands.command(name="dban", description="dban les personne")
    async def ban(self, interaction: discord.Interaction, user: discord.Member, raison: str = "aucune raisson"): 
        await interaction.response.defer(ephemeral=True)


        has_permission = interaction.user.guild_permissions.ban_members
        if not has_permission:
           await interaction.followup.send("vous n'avais pas les permission")
        
        try:
            
            await interaction.guild.unban(user, raison)
            await interaction.response.send_message(f"{user} a été debanni pour {raison}")

        except Exception as e:

            await interaction.response.response.send_message(f"{User} est imposible a bannire : {e}", ephemeral=True)





