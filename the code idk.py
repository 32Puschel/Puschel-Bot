import discord
from discord.ext import commands 

client = commands.Bot(command_prefix = '-')
#Prefixes dont work so far but the code breaks when I remove it. 

@client.event
async def on_ready():
    print('It works!')    

@client.event
async def on_member_join(member):
    print(f'{member} has joined a Server.')
    
@client.event
async def on_member_remove(member):
    print(f'{member} has left a Server.')
    
@client.event
async def on_message(message):

	if message.content == '.test':
		await message.channel.send('No u')
       
@client.event
async def on_message(message):

	if message.content == '.help':
		await message.channel.send('U aint getting any help from me.')

@client.event
async def on_message(message):

	if message.content == '.dorto':
		await message.channel.send('https://cdn.discordapp.com/emojis/870388745554231306.png?v=1')

@client.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.bot.logout()
    client.run('your Bot token')
