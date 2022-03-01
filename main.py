from discord import Intents
import os
from dotenv import load_dotenv
from discord.ext import commands
from cogwatch import watch
from discord_slash import SlashCommand

prefixint = "n!"

client = commands.Bot(command_prefix= prefixint, self_bot = True, intents = Intents.default())
client.remove_command('help')

slash = SlashCommand(client, sync_commands = True)

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
