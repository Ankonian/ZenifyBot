import discord
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix=',', intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    if message.content.startswith('!zenify'):
      for guild in client.guilds:
            print(str(guild.members))
            async for member in guild.fetch_members():
                if not member.bot and not member.name == 'PimpDaddyMagic':
                    print(member.name + " is not a bot")
                    await member.edit(nick="Zen " + member.name)
                
                
                
            
                    

@client.event
async def on_member_join(member):
    await member.edit(nick="Zen")

client.run('ODAzODExMTA1MDgzODgzNTUx.YBDNbQ.ln5Co3f7OkzsVeV4u9_xe6xeDgM')