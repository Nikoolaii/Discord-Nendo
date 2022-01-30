import discord
import os
from discord.ext import commands
from cogwatch import watch


client = commands.Bot(command_prefix= "n!")
client.remove_command('help')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.lava_nodes = [
    {
        'host' : 'lava.link',
        'port' : 80,
        'rest_uri': f'http://lava.link:80',
        'identifier': 'MAIN',
        'password': 'anything',
        'region': 'we',
        'secure': 'true'
    }
]

prefixint = "n!"

client.run("NzU4MjgyNTkyMDI1NTc1NDQ1.X2srsg.ZTBkEGRgS7CjY4jNsw2YF8ggyg0")
