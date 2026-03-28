import discord
from discord.ext import commands
import random
import json
import os
import string

client = discord.Client(intents=discord.Intents.all())
# bot = commands.Bot(command_prefix='!', intents=discord.Intents.default())
    
@client.event
async def on_ready():
    print(f'{client.user} is now ready')

@client.event
async def on_message(message):
    
    server_name = message.guild.name
    filename = f'{server_name}.json'

    if os.path.exists(filename):
            with open(filename, 'r') as f:
                leaderboard = json.load(f)
    else:
        leaderboard = {}
            
    if message.author == client.user:
        return

    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    send_message = False
    shiny_message = False

    rnd = random.randint(0,75)
    rndShiny = random.randint(0,4080)
    

    if rndShiny == 4000:
        shiny_message = True

    if shiny_message == True:
        await message.channel.send(f"{message.author.mention} I actually kinda like this one")

    if rnd == 10:
        send_message = True

    if message.author.id != 177504009748217856 and send_message == True:
        await message.channel.send(f"{message.author.mention} Ratio")
        
        if bool(leaderboard.get(f'<@{message.author.id}>')) is True:
            leaderboard[f'<@{message.author.id}>'] += 1
        else:
            leaderboard[f'<@{message.author.id}>'] = 1
        temp = sorted(leaderboard.items(), key=lambda x:x[1], reverse=True)
        leaderboard = dict(temp)

        with open(filename, 'w') as f:
            json.dump(leaderboard, f)
    
    if str(message.content) == '!ratio':
        if bool(leaderboard) == True:
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
        else:
            await message.channel.send('No one in this server has been ratioed yet :pensive:')
            

            
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