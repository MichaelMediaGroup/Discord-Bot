import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
await client.change_presence(status=discord.Status.idle, activity=discord.Game(name="Minecraft"))
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


@commands.has_permissions(administrator = True)
@client.command(aliases=['purge'])
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount + 1)
    
@commands.has_permissions(kick_members=True)    
@client.command()
async def kick(ctx, Member : discord.Member, *, reason=None):
    await Member.kick(reason=reason)

@commands.has_permissions(kick_members=True)    
@client.command()
async def ban(ctx, Member : discord.Member, *, reason=None):
    await Member.ban(reason=reason) 
    
#gets user info of user on the discord
@client.command(aliases=["userinfo"] ,help = "Finds info about users on the discord.")
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title=f"{user}'s info", description=f"Here's {user}'s info", color=0x00ff00)
    embed.add_field(name="Username:", value=user.name, inline=True)
    embed.add_field(name="ID:", value=user.id, inline=True)
    embed.add_field(name="Status:", value=user.status, inline=True)
    embed.add_field(name="Highest Role:", value=user.top_role, inline=True)
    embed.add_field(name="Joined:", value=user.joined_at, inline=True)
    embed.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=embed)
    
client.run('TOKEN')
