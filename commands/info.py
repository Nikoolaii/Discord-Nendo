
import discord
from discord.ext import commands
prefixint = "n!"

class Info(commands.Cog):
    
    def __init__(self, client):
        self.client = client 
    
    @commands.command(pass_context = True)
    async def serverinfo(self,ctx, user: discord.Member = None):
        user = user or ctx.author    
        role_count = len(ctx.guild.roles)
        list_of_bots = [bot.mention for bot in ctx.guild.members if bot.bot]
        embed2 = discord.Embed(title = "**__Server Information__ 📜**",color=0xe4a3f3)
        embed2.add_field(name='**Server Nom :**', value=f"{ctx.guild.name}", inline=False)
        embed2.add_field(name='**Fondateur :**', value=f"{ctx.guild.owner}", inline=False)
        embed2.add_field(name='**Level de vérification :**', value=str(ctx.guild.verification_level), inline=False)
        embed2.add_field(name='**Role élevé :**', value=ctx.guild.roles[-2], inline=False)
        embed2.add_field(name='**Contributeur :**', value="None")
        embed2.add_field(name='**Nombre de Roles :**', value=str(role_count), inline=False)
        embed2.add_field(name='**Nombre de Membre :**', value=ctx.guild.member_count, inline=False)
        embed2.add_field(name='**Bots :**', value=(', '.join(list_of_bots)))
        embed2.add_field(name='**Crée le :**', value=ctx.guild.created_at.__format__("Le **%d/%m/%Y** à **%H:%M:%S**"), inline=False)
        embed2.set_thumbnail(url=ctx.guild.icon)
        embed2.set_author(name=ctx.author.name, icon_url=ctx.author.avatar)
        await ctx.send(embed=embed2)

    @commands.command(pass_context = True)
    async def userinfo(self,ctx, user: discord.Member = None):
        user = user or ctx.author
        embed = discord.Embed(title = "**__Membre Information__ 📜**",color=0xe4a3f3)
        embed.add_field(name='**Nom :**', value = f"{user.name}", inline = False)
        embed.add_field(name='**Tag :**', value = f"#{user.discriminator}", inline = False)
        embed.add_field(name='**Surnom :**', value = f"{user.display_name}", inline = False)
        embed.add_field(name='**Mention :**', value = f"{user.mention}", inline = False)
        embed.add_field(name='**ID :**', value = f"{user.id}", inline = False)
        embed.add_field(name='**Compte crée :**', value = f'{user.created_at.strftime("Le **%d/%m/%Y** à **%H:%M:%S**")}',inline = False)
        embed.add_field(name='**Date d\'arrivée :**', value = f'{user.joined_at.strftime("Le **%d/%m/%Y** à **%H:%M:%S**")}',inline = False)
        embed.add_field(name = "**Status :**",value = f"{str(user.status).title()}")
        embed.add_field(name = "**Activité :**",value = f"{str(user.activity.type).split('.')[-1].title() if user.activity else 'N/A'} {user.activity.name if user.activity else ''}")
        embed.set_thumbnail(url=user.avatar)
        await ctx.send(embed = embed)

    @commands.command(pass_context = True)
    async def botinfo(self,ctx):
        embed = discord.Embed(title="**__Information du bot__**", description= f"Voici les informations de Nendo !",color=0xe4a3f3)
        embed.add_field(name='**Développeur**',value=f'**┕**<@226657385211494401>',inline=True)
        embed.add_field(name='**Paramètre**',value= f'**┕**``{round(self.client.latency * 1000)} ms``\n**┕**``V2.0.0``\n**┕**``{prefixint}help``\n**┕**``discord.gg/PeRjhJa``\n**┕**``Bot sur {len(self.client.guilds)} serveurs``',inline=True)
        embed.set_thumbnail(url=ctx.guild.icon)
        await ctx.send(embed=embed)    
        
        
def setup(client):
    client.add_cog(Info(client))