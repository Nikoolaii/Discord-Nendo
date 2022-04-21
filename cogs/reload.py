import discord
from discord.ext import commands
from discord_slash import cog_ext

class owner(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    @commands.is_owner()
    @cog_ext.cog_slash(name="load", description="✨ Permet de charger un cog.")
    async def load(self, ctx, extension):
        self.client.load_extension(f'cogs.{extension}')
        await ctx.send(f":white_check_mark: Le cog à était chargé avec succès `{extension}`")

    @commands.command()
    @commands.is_owner()
    @cog_ext.cog_slash(name="unload", description="✨ Permet de décharger un cog.")
    async def unload(self, ctx, extension):
        self.client.unload_extension(f'cogs.{extension}')
        await ctx.send(f":white_check_mark: Le cog à était déchargé avec succès `{extension}`")

    @commands.command()
    @commands.is_owner()
    @cog_ext.cog_slash(name="reload", description="✨ Permet de recharger un cog.")
    async def reload(self, ctx, extension):
        self.client.unload_extension(f'cogs.{extension}')
        self.client.load_extension(f'cogs.{extension}')
        await ctx.send(f":white_check_mark: Le cog à était rechargé avec succès `{extension}`")
    
def setup(client):
    client.add_cog(owner(client))
