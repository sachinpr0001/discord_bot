import discord
from discord.ext import commands, tasks
import youtube_dl

from random import choice

client = commands.Bot(command_prefix='-')

status = ['Aaj Arpit Ki Maarunga!', 'Are Nahi Yaar!', 'Pel Diye Jaoge!', 'Toby ka bhai hai tu!', 'Aye Bokachoda!']

@client.event
async def on_ready():
	change_status.start()
	print('Bot is Online!')

@client.command(name='ping', help='This command returns the latency')
async def ping(ctx):
	await ctx.send(f'**Pong!** Latency : {round(client.latency * 1000)}ms')


@tasks.loop(seconds=10)
async def change_status():
	await client.change_presence(activity=discord.Game(choice(status)))


client.run('ODkwMjc0NjE0NTQ1MTIxMjgw.YUta2A.v2DaOhlcypCe2bU2mhKiQbpt-BY')

