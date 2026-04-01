import discord
from discord.ext import commands
import random
import json
import os
import string

import ratio
import message

#Establish bot Id so bot doesnt respond to itself
#Change Bot Id to own bot
BotId = 177504009748217856

#Establish the Client for the Discord Bot
client = discord.Client(intents=discord.Intents.all())
# bot = commands.Bot(command_prefix='!', intents=discord.Intents.default())
    
@client.event
async def on_ready():
    print(f'{client.user} is now ready')

#Ratio Code
@client.event
#Checks at a sent message
async def on_message(message):
    if message.author == client.user:
        return

    M = message(message, client, BotId)
    ratio(M)
    await message.channel.send(f"{M.Return_Message}")

    #retrives previous leaderboard info
    
    # Code for viewing the leaderboard
    if str(message.content) == '!ratio':
        leaderboard(M)
        await message.channel.send(f"{M.Return_Message}")
        

client.run('MTA1MTc3NTYyNTg0MjY3MTcwNg.GBbrwb.KZdVoCzAEZdLKYcEkrFjqy1LMEbuTBYhqTe59k')
# ^ Security token