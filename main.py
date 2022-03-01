import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from cogwatch import watch

prefixint = "n!"

client = commands.Bot(command_prefix= prefixint)
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


load_dotenv()
token = os.getenv("DISCORD_TOKEN")
client.run(token)
