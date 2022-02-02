import discord
from discord.ext import commands
import giphy_client
from giphy_client.rest import ApiException
import random
import nekos
prefixint = "n!"

class Image(commands.Cog):

    def __init__(self, client):
        self.client = client 

    @commands.command(pass_context = True , aliases=['giphy'])
    async def gif(self, ctx, *,q="random"):
        
        api_key="K1vpDUM7MJYSHNZzaoX56F6ulroVYNqs"
        api_instance = giphy_client.DefaultApi()

        try: 
        # Search Endpoint
        
            api_response = api_instance.gifs_search_get(api_key, q, limit=5, rating='g')
            lst = list(api_response.data)
            giff = random.choice(lst)

            emb = discord.Embed(title=f"Gif with keyword __{q}__",
                color=0xe4a3f3, 
                )
            emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')

            await ctx.channel.send(embed=emb)
        except ApiException as e:
            print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

    @commands.command(pass_context = True)
    async def servericon(self, ctx):

        embed = discord.Embed(
            color=0xe4a3f3)
        embed.set_author(name=f"Icon demandé par: **{ctx.message.author}**")
        embed.set_image(url=ctx.guild.icon_url)
        embed.set_thumbnail(url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @commands.command(pass_context = True , aliases=['pdp'])
    async def pp(self, ctx , member: discord.Member=None):

        if not member:
            member = ctx.author

        userAvatar = member.avatar_url

        embed = discord.Embed(color=0xcc3399)
        embed.set_author(name=f"Photo de profil demandée par: {ctx.message.author}")
        embed.set_image(url=userAvatar)

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Image(client))