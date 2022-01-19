import discord
from discord.ext import commands
prefixint = "n!"

class Basics(commands.Cog):
    
    def __init__(self, client):
        self.client = client 
    
    @commands.command(pass_context = True)
    async def ping(self, ctx):
        await ctx.send(f"My latency is: {round(self.client.latency,3)}ms")    
        
    @commands.command(pass_context = True)
    async def invite(self, ctx):
        invite = discord.Embed(color=0xe4a3f3)
        invite.add_field(name=f"**Lien pour inviter le bot.**",value = f"[Cliquez ici pour inviter le bot](https://discord.com/oauth2/authorize?client_id=758282592025575445&scope=bot&permissions=8)", inline=False)

        await ctx.send(embed=invite)    


    @commands.command(pass_context = True)
    @commands.has_permissions(manage_messages=True)
    async def say(self, ctx, *, message=None):

        await ctx.message.delete()

        embed = discord.Embed(
            color=0xe4a3f3)
        embed.set_author(name="Annonce !")
        embed.add_field(name=f"Envoyé par {ctx.message.author}", value=str(message))
        embed.set_thumbnail(url=ctx.author.avatar)
        if message == None:
            ctx.send("Please write something to say !")
        else:
            await ctx.send(embed=embed)
        
    @commands.command(pass_context = True)
    async def bypasslink(self,ctx,*, message = None):
        
        link = str(message)
        if "http" not in link:
            ctx.send("Please insert an url !")
        else:
            url = "https://bypass.bot.nu/bypass2?url=" + link
            ctx.send(url)
        
def setup(client):
    client.add_cog(Basics(client))