import discord
from discord.ext import commands
import giphy_client
from giphy_client.rest import ApiException
import random
import requests
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

    @commands.command(pass_context = True , aliases=['ravatar'])
    async def nekosimg(self, ctx, endpoint):
        valid = False
        endpointlist= ["tickle", "slap", "poke", "pat", "neko", "meow", "kiss", "hug", "fox_girl", "feed", "cuddle", "ngif", "smug", "kemonomimi", "baka", "woof", "wallpaper", "goose", "waifu", "avatar"]
        for i in range(len(endpointlist)):
            if endpoint == endpointlist[i]:
                valid = True

        if valid == True :
            requete = requests.get(f"https://nekos.life/api/v2/img/{endpoint}")
            soup = str(requete.content)
            soup = soup[10:-5]

            sendembed = discord.Embed(color=0xcc3399)
            sendembed.set_author(name=f"Voici ton image générée aléatoirement !")
            sendembed.set_image(url=soup)
            await ctx.send(embed=sendembed)
        else:
            listembed = discord.Embed(color=0xcc3399)
            listembed.set_author(name=f"Mauvaise argument, voici la liste des arguments corrects !")
            listembed.add_field(name="Voici tous les arguments corrects", value=f"** **")
            listembed.add_field(name="** **", value=f"** **", inline= False)
            listembed.add_field(name="** **", value=f"tickle\nslap\npoke\npat\nneko")
            listembed.add_field(name="** **", value=f"meow\nhug\nfox_girl\nfeed\ncuddle")
            listembed.add_field(name="** **", value=f"ngif\nsmug\nkemonomimi\nbaka\nwoof")
            listembed.add_field(name="** **", value=f"kiss\nwallpaper\ngoose\nwaifu\navatar")
            await ctx.send(embed=listembed)

def setup(client):
    client.add_cog(Image(client))