from discord.ext import commands
from discord import app_commands, Interaction
import discord 


class ClearCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="clear", description="Supprime le nombre de messages spécifié")
    async def clear(self, interaction: discord.Interaction, number: int):
        await interaction.response.defer(ephemeral=True)
        
        has_permission = interaction.user.guild_permissions.manage_messages
        if not has_permission:
            await interaction.followup.send("Vous n'avez pas la permission de gérer les messages.", ephemeral=True)
            return

        if number <= 0 or number > 100:
            await interaction.followup.send("Le nombre de messages à supprimer doit être entre 1 et 100.", ephemeral=True)
            return
        
        deleted = await interaction.channel.purge(limit=number)
        await interaction.followup.send(f"{len(deleted)} messages supprimés", ephemeral=True)





