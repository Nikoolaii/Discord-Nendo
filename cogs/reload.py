import discord
from discord.ext import commands

class owner(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, extension):
        self.client.load_extension(f'cogs.{extension}')
        await ctx.send(f":white_check_mark: Le cog à était chargé avec succès `{extension}`")

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, extension):
        self.client.unload_extension(f'cogs.{extension}')
        await ctx.send(f":white_check_mark: Le cog à était déchargé avec succès `{extension}`")

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, extension):
        self.client.unload_extension(f'cogs.{extension}')
        self.client.load_extension(f'cogs.{extension}')
        await ctx.send(f":white_check_mark: Le cog à était rechargé avec succès `{extension}`")
    
def setup(client):
    client.add_cog(owner(client))
