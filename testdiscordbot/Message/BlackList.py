import discord
from discord.ext import commands



mots_interdie = ("hitler", "hitl", "hitle", "Ben La Den", "BenLaDen", "ftp", "fils de pute", "enculer", "fuck you" ,"bitch","salop")

@commands.Cog.listener()

async def blacklist(self, message):
 if message.authore == self.bot.user:
  return

 contenu = message.mots_interdie.lower


 for mot in mots_interdie:
  if mot in contenu:
   await message.delete()
   await message.channel.send(f"** un message a étais --SUPRIMER-- car contient un mots bannie !! **")

 await self.bot.process_commands(message)

        
