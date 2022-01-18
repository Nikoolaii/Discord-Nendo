import discord
import os
from discord.ext import commands
from cogwatch import watch

client = commands.Bot(command_prefix= "n!")
client.remove_command('help')

for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
        client.load_extension(f'commands.{filename[:-3]}')

prefixint = "n!"

client.run("")
