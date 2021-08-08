import discord
from discord.ext import commands 

client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():
    print('Bot is ready!')     

client.run('Your Token, I totally didnt forget to remove my own token')
