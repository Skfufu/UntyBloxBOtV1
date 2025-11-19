from discord.ext import commands
from discord import app_commands, Interaction
import discord

class ClearCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="clear", description="Supprime le nombre de messages spécifié")
    async def clear(self, interaction: Interaction, number: int):
        await interaction.response.defer(ephemeral=True)
        
        if not interaction.user.guild_permissions.manage_messages:
            await interaction.followup.send("Vous n'avez pas la permission de gérer les messages.", ephemeral=True)
            return

        if number <= 0 or number > 100:
            await interaction.followup.send("Le nombre de messages à supprimer doit être entre 1 et 100.", ephemeral=True)
            return

        channel = interaction.channel
        if isinstance(channel, discord.TextChannel):
            deleted = await channel.purge(limit=number)
            await interaction.followup.send(f"{len(deleted)} messages supprimés", ephemeral=True)
        else:
            await interaction.followup.send("Impossible de supprimer les messages ici.", ephemeral=True)





