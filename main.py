import discord
import os

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

# client.run(os.getenv('TOKEN'))
client.run("MTA2NTM5MDIzMzY3NzQ3OTk4Nw.G6wtQ2.L6kcMQLDd8asAEcyZ-_OTUt_iLOMkvVmghBd6M")