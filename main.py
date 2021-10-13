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

	if message.content == 'p!oghelp':
		await message.channel.send('U ain\'t gettin any help from me ;)')
	if message.content == 'p!dorto':
		await message.channel.send('https://cdn.discordapp.com/emojis/870388745554231306.png?v=1')
	if message.content == 'p!test':
		await message.channel.send('No u')
	if message.content == 'p!help':
		await message.channel.send('No u') #gotta figure out how embeds work first
	if message.content == 'p!':
		await message.channel.send('Yes, thats my prefix')


client.run('your Bot token')
#I totally didnt accidently put my token here
