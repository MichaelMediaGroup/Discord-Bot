import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("I am alive.")

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)} ms ping time")

@client.command(aliases=["8ball", "eightball"])
async def Eightball(ctx, *, question):
    responses = ['magic eight ball maintains Signs point to yes.',
                 'magicball affirms My reply is no.',
                 'magic ball answers Signs point to yes.',
                 'magicball affirms Yes definitely.',
                 'magicball affirms Yes.',
                 '8 ball magic said Most likely.',
                 'magic ball answers Very doubtful.',
                 'magic 8 ball answers Without a doubt.',
                 'mystic eight ball said Most likely.',
                 "magic ball answers Don't count on it.",
                 'Magic ball says 100% No',
                 'Magic ball does not know have you tryed google?',
                 "Its not looking so good"]
    await ctx.send(f"Quection: {question}\nAnswer: {random.choice(responses)}")



@client.command(aliases=["Hello", "hi", "Hi"])
async def hello(ctx):
    await ctx.send('Hi')
client.run('TOKEN')
