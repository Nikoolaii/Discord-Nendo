import discord
from discord.ext import commands
prefixint = "n!"

class Admin(commands.Cog):
    
    def __init__(self, client):
        self.client = client 
        
    @commands.command(pass_context = True)
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        embed = discord.Embed(title = '**__Membre Bannis__**📜',color = 0xcc3399)
        embed.add_field(name = '**__Auteur :__**',value =ctx.author.mention,inline = False)
        embed.add_field(name='**__Cible :__**',value =member.mention,inline = False)
        embed.add_field(name='**__Raison :__**',value =reason,inline = False)
        embed.add_field(name="**__Date d'arrivé :__**",value =member.joined_at.strftime("Le **%d/%m/%Y** à **%H:%M:%S**"),inline = False)
        embed.set_image(url="https://i.ibb.co/cJQzpsH/template-3.png")
        embed.set_thumbnail(url=member.avatar_url)
        await member.ban(reason=reason)
        await ctx.channel.send(embed = embed)

    @commands.command(pass_context = True)
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        embed = discord.Embed(title = '**__Membre Kick__**📜',color = 0xcc3399)
        embed.add_field(name = '**__Auteur :__**',value =ctx.author.mention,inline = False)
        embed.add_field(name='**__Cible :__**',value =member.mention,inline = False)
        embed.add_field(name='**__Raison :__**',value =reason,inline = False)
        embed.add_field(name="**__Date d'arrivé :__**",value =member.joined_at.strftime("Le **%d/%m/%Y** à **%H:%M:%S**"),inline = False)
        embed.set_image(url="https://i.ibb.co/8KBwfCk/template-4.png")
        await member.kick(reason=reason)
        await ctx.channel.send(embed = embed)
        
    @commands.command(pass_context = True)
    @commands.has_permissions(manage_messages = True)
    async def purge(self, ctx, amount=None):
        amount = int(amount)
        await ctx.channel.purge(limit=amount)
        await ctx.channel.send(f"**♻️ {ctx.author.mention} a nettoyé le salon de `{amount}` message(s) !**")
        
def setup(client):
    client.add_cog(Admin(client))