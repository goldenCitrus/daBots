import discord
from discord.ext import commands
import random
import json
import os
import string

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

    Non_Ratio_Channel = {"vent-advice-channel"}

    #retrives previous leaderboard info
    server_name = message.guild.name
    filename = f'{server_name}.json'

    if os.path.exists(filename):
            with open(filename, 'r') as f:
                leaderboard = json.load(f)
    else:
        leaderboard = {}
            
    if message.author == client.user:
        return

    #Retrives User and Channel info
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    # Checks message for Ratio base on 
    # 1.Random odds for Ratio
    # 2.If the author is not the Bot
    # 3.If the message is in the non allowed Channels
    #
    # If all pass the bot will Ratio
    if random.randint(0,5) == 1 and message.author.id != BotId and not(channel in Non_Ratio_Channel):
        await message.channel.send(f"{message.author.mention} Ratio")
        
        if bool(leaderboard.get(f'<@{message.author.id}>')) is True:
            leaderboard[f'<@{message.author.id}>'] += 1
        else:
            leaderboard[f'<@{message.author.id}>'] = 1
        temp = sorted(leaderboard.items(), key=lambda x:x[1], reverse=True)
        leaderboard = dict(temp)

        with open(filename, 'w') as f:
            json.dump(leaderboard, f)

    elif random.randint(0,4080) == 4000 and message.author.id != BotId and not(channel in Non_Ratio_Channel):
        await message.channel.send(f"{message.author.mention} I actually kinda like this one")
    
    # Code for viewing the leaderboard
    if str(message.content) == '!ratio':
        num = 0
        embed = discord.Embed(title=f'Leaderboard for {message.guild.name}', description='the top 10 yuh')
        embed.set_thumbnail(url=message.guild.icon)
        for key, value in leaderboard.items():
            user_id = key.translate(str.maketrans('', '', string.punctuation))
            user = client.get_user(int(user_id))

            # If not in cache, try to fetch from Discord API
            if user is None:
                try:
                    user = await client.fetch_user(int(user_id))
                except:
                    user_name = "Unknown User"
                else:
                    user_name = user.name
            else:
                user_name = user.name
        
            if num <= 10:
                embed.add_field(name=f'{user_name} has been ratioed:', value=f'{value} times', inline=False)
                num += 1
        await message.channel.send(embed=embed)
# @bot.command(name='lb')
# async def lb(ctx, arg):
#     server_name = ctx.guild
#     filename = f'{server_name}.json'
    
#     if os.path.exists(filename):
#             with open(filename, 'r') as f:
#                 leaderboard = json.load(f)
#     else:
#         leaderboard = {}
#     try:
#         leaderboard[ctx.message.author] += 1
#     except KeyError:
#         leaderboard[ctx.message.author] = 1

client.run('MTA1MTc3NTYyNTg0MjY3MTcwNg.GBbrwb.KZdVoCzAEZdLKYcEkrFjqy1LMEbuTBYhqTe59k')
# ^ Security token