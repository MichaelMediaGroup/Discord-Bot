import discord
from discord import client
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("we have powered on, I an alive.")

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

@client.command()
async def hello(ctx):
    await ctx.send('Hi')



client.run('TOKEN')
