import discord
from discord.ext import commands
prefixint = "n!"
import pyfiglet
from discord.ext.commands import BadArgument, CommandNotFound, MissingPermissions, MissingRequiredArgument
from cogwatch import watch


class Events(commands.Cog):
    def __init__(self, client):
        self.client = client   


    @commands.Cog.listener()
    @watch(path='cogs')
    async def on_ready(self):
        result = pyfiglet.figlet_format("- NENDO -") 
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"n!help - {len(self.client.guilds)} guilds"))

        print('------')
        print(result)
        print('Logged in as')
        print("- ", self.client.user)
        print("- ", self.client.user.id)
        print("- ", len(self.client.guilds), "Guilds")
        print("Your bot is up !")
        print('------')

        self.client.load_extension('dismusic')


    @commands.Cog.listener()
    async def on_guild_join(self):
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"n!help - {len(self.client.guilds)} guilds"))

    @commands.Cog.listener()
    async def on_guild_remove(self):
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"n!help - {len(self.client.guilds)} guilds"))


    @commands.Cog.listener()
    async def on_command_error(self, ctx, exc):
        if isinstance(exc, MissingPermissions):
            await ctx.send("⚠ **Vous n'êtes pas autorisé à utiliser cette commande.**")
            return
        elif isinstance(exc, CommandNotFound):
            await ctx.send("⚠ **Cette commande n'existe pas.**")
            return
        elif isinstance(exc, MissingRequiredArgument): 
            await ctx.send("⚠ **Merci de rajouter un argument après la commande.**")
            return
        elif isinstance(exc, BadArgument): 
            await ctx.send("⚠ **Mauvais argument.**")
            return
        else:
            print(exc)


def setup(client):
    client.add_cog(Events(client))