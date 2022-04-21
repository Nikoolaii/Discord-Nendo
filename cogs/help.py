import discord
from discord.ext import commands
from discord_slash import cog_ext
prefixint = "n!"

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client   
            
    @cog_ext.cog_slash(name="help", description="📚 Afficher la liste de toutes les commandes du bot.")
    async def help(self,ctx):
        page1 = discord.Embed(
            title = f"Panneau d'aide • Prefix : `{prefixint}`",
            description = "Voici toutes les catégories de commandes.",
            color=0xe4a3f3
        )
        page1.set_image(url="https://i.imgur.com/6CkbQkt.gif")
        page1.add_field(name="Commandes principales", value=f":gear:",inline=True)
        page1.add_field(name="Commandes d'images", value=f":frame_photo:",inline=True)
        page1.add_field(name="Commandes drôles", value=f":clown:",inline=True)
        page1.add_field(name="Commandes de staff", value=f"⚠️",inline=True)
        page1.set_footer(text=f"Support: n!invite")

        page2 = discord.Embed (
                title = f"Panneau d'aide • Prefix : `{prefixint}`",
                description = "Les commandes principales.",
                color=0xe4a3f3)
        page2.set_image(url="https://i.imgur.com/6CkbQkt.gif")
        page2.add_field(name=f"{prefixint}say",value="Pour faire parler le bot.")
        page2.add_field(name=f"{prefixint}ping",value="Pour savoir le ping du bot.")
        page2.add_field(name=f"{prefixint}invite",value="Spécialement pour invité le bot sur ton serveur.")
        page2.add_field(name=f"** **",value="** **",inline=False)
        page2.add_field(name=f"{prefixint}serverinfo",value="Pour obtenir des informations sur le serveur")
        page2.add_field(name=f"{prefixint}userinfo",value="Pour obtenir des informations sur toi.")
        page2.add_field(name=f"{prefixint}botinfo",value="Pour obtenir des informations sur le bot.")
        page2.add_field(name=f"{prefixint}bypasslink",value="Pour bypass un lien adfly ou linkvertise par exemple.")
        #page2.add_field(name=f"{prefixint}suggest",value="To send a suggestion to the bot maker.",inline=False)
        page2.add_field(name=f"** **",value="** **",inline=False)
        page2.add_field(name=f"{prefixint}setmsg",value=f"Commande pour définir un message qui pourras être utilisé avec la commande interne au serveur")
        page2.add_field(name=f"{prefixint}sendmsg",value="Commande pour envoyer le message définie par l'administrateur")

        page3 = discord.Embed (
            title = f"Panneau d'aide • Prefix : `{prefixint}`",
            description = "Les commandes d'images.",
            color=0xe4a3f3)
        page3.set_image(url="https://i.imgur.com/6CkbQkt.gif")
        page3.add_field(name=f"{prefixint}pp",value="Pour obtenir ta pdp ou celle d'une personne mentionée.")
        page3.add_field(name=f"{prefixint}servericon",value="Pour récuperer la photo de profil du serveur.")
        page3.add_field(name=f"{prefixint}gif",value="Pour envoyer un gif.")
        page3.add_field(name=f"{prefixint}nekosimg",value="Pour envoyer une image aléatoire grâce à l'api Nekos Life.")

        page4 = discord.Embed (
            title = f"Panneau d'aide • Prefix : `{prefixint}`",
            description = "Les commandes droles.",
            color=0xe4a3f3)
        page4.set_image(url="https://i.imgur.com/6CkbQkt.gif")
        #page4.add_field(name=f"{prefixint}osu",value="Pour avoir tes stats osu!.",inline=False)
        page4.add_field(name=f"{prefixint}fight",value="Pour te battre avec la personne mentionée.")
        page4.add_field(name=f"{prefixint}pof",value=f"Pour faire un pile ou face, un super moyen de décider.")

        page5 = discord.Embed (
            title = f"Panneau d'aide • Prefix : `{prefixint}`",
            description = "Les commandes de staff.",
            color=0xe4a3f3)
        page5.set_image(url="https://i.imgur.com/6CkbQkt.gif")
        page5.add_field(name=f"{prefixint}ban",value="Pour pouvoir ban les méchants de ton serveur")
        page5.add_field(name=f"{prefixint}kick",value="Pour pouvoir kick les méchants de ton serveur")
        page5.add_field(name=f"{prefixint}purge",value="Pour pouvoir supprimer les messages des channels en masse")

        
        pages = [page1, page2, page3, page4, page5]

        message = await ctx.send(embed = page1)
        await message.add_reaction('⬅️')
        await message.add_reaction('⚙️')
        await message.add_reaction('🖼️')
        await message.add_reaction('🤡')
        await message.add_reaction('⚠️')

        def check(reaction, user):
            return user == ctx.author

        i = 0
        reaction = None

        while True:
            if str(reaction) == '⚙️':
                i = 1
                await message.edit(embed = pages[i])
            elif str(reaction) == '🖼️':
                i = 2
                await message.edit(embed = pages[i])
            elif str(reaction) == '🤡':
                i = 3 
                await message.edit(embed = pages[i])
            elif str(reaction) == '⬅️':
                i = 0
                await message.edit(embed = pages[i])
            elif str(reaction) == '⚠️':
                i = 4
                await message.edit(embed = pages[i])
            
            try:
                reaction, user = await self.client.wait_for('reaction_add', timeout = 30.0, check = check)
                await message.remove_reaction(reaction, user)
            except:
                break

        await message.clear_reactions()
    

def setup(client):
    client.add_cog(Help(client))
