import discord
from discord.ext import commands
prefixint = "n!"
import requests

class Game(commands.Cog):
    
    def __init__(self, client):
        self.client = client 
        
        
    @commands.command(pass_context = True)
    async def apex(self,ctx, arg1=None, arg2=None):
        response = requests.get(f'https://api.mozambiquehe.re/bridge?version=5&platform={arg1}&player={arg2}&auth=d3wDsHJB0oXacomXIRHO', headers= {'content-type': 'application/json'})
        global2 = response.json()["global"]
        categoryrang = global2["rank"]
        legende = response.json()["legends"]
        legendselect = legende["selected"]
        legendimage = legendselect["ImgAssets"]
        rankname = categoryrang["rankName"]
        rankdiv = categoryrang["rankDiv"]
        elo = categoryrang["rankScore"]
        level = global2["level"]
        legendrecent = legendimage["banner"]
        rangimg = categoryrang["rankImg"]
        embed = discord.Embed(title=f"**{arg2}'s Stats**",description=f'**__Information :__**\n\n**Plateforme :** `{arg1}`\n**Level :** `{level}`\n**Rang :** `{rankname}`\n**Division :**`{rankdiv}`\n**Elo :** `{elo}`',color=discord.Color.green())
        embed.set_image(url=f"{legendrecent}")
        embed.set_thumbnail(url=f'{rangimg}')
        await ctx.send(embed=embed)
        
def setup(client):
    client.add_cog(Game(client))