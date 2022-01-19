from os import name
import discord
from discord.ext import commands
prefixint = "n!"
from random import *
import time

class Fun(commands.Cog):
    
    def __init__(self, client):
        self.client = client 
        
    @commands.command(pass_context = True, aliases=['pof'])
    async def pileouface(self,ctx):
        n = random()
        if  n < 0.5:
            variable = 'pile'
        else :
            variable = 'face'
        
        if variable == 'pile':
            await ctx.send("Pile")
        else:
            await ctx.send("Face")
            
            
    @commands.command(pass_context = True)
    async def fight(self,ctx, member: discord.Member):
        
        n = random()
        if  n < 0.5:
            win = ctx.author.mention
            loose= member.mention
        else :
            win = member.mention
            loose = ctx.author.mention
        
        fight = discord.Embed(
            color=0xcc3399,
            title = f"Le combat fait rage.")
        fight.add_field(name="Pourtant, le vainqueur est:",value=f"{win}, dommage pour {loose}, peut être qu'il gagnera la prochaine fois !",inline=False)
        fight.set_image(url="https://thumbs.gfycat.com/BlackElegantAngelfish-size_restricted.gif")
        
        
        await ctx.message.delete()
        await ctx.send(f"Oh mais que vois-je ? {ctx.author.mention} viens de proposer un duel à {member.mention}")
        time.sleep(2)
        await ctx.send(embed=fight)
        
        
def setup(client):
    client.add_cog(Fun(client))