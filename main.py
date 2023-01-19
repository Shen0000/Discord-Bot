import discord
from discord.ext import commands
import os
import itertools as it
import logging
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents().all()
# client = discord.Client(intents=intents)
client = commands.Bot(command_prefix="$", intents=intents)

def alias_creator(s): # this makes it so that you can use any combination of uppercase and lowercase to call a command
    lu_sequence = ((c.lower(), c.upper()) for c in s)
    product = [''.join(x) for x in it.product(*lu_sequence)]
    for word in product:
        if word == str(s):
            product.remove(word)
    return product

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,activity=discord.Activity(name="Serving the Wayland CS Club!", type=5))
    print('We have logged in as {0.user}'.format(client))
    # logging.info(f"User: {client.user} (ID: {client.user.id})")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    await client.process_commands(message)

@client.command(
    name = "hello",
    description = "Says hello to you!",
    aliases = alias_creator("hello")
    )
async def hello(message): # $hello will return "Hello + your username"
    await message.channel.send("Hello " + message.author.display_name + "!")

@client.command(
    name = "ping",
    description = "Returns the ping of the bot",
    aliases = alias_creator("ping")
    )
async def ping(ctx):
    # print("Pinged!")
    await ctx.send("Pong! {}ms".format(round(client.latency*1000)))

@client.command(
    name = "server",
    description = "Returns information about the server",
    aliases = alias_creator("server")
    )
async def server(ctx):
    name = str(ctx.guild.name)
    desc = str(ctx.guild.description)
    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name + " Server Information",
        Description=desc,
        color=discord.Color.blue()    
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)

    await ctx.send(embed=embed)


client.run(os.getenv('TOKEN'))