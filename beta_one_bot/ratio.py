import os
import json
import random
import string
import discord

Non_Ratio_Channel = {"vent-advice-channel"}

def ratio(I):
    
    #retrives previous leaderboard info
    filename = f'{I.message.guild.name}.json'

    if os.path.exists(filename):
            with open(filename, 'r') as f:
                leaderboard = json.load(f)
    else:
        leaderboard = {}
            
    if I.message.author == I.client.user:
        return

    # Checks message for Ratio base on 
    # 1.Random odds for Ratio
    # 2.If the author is not the Bot
    # 3.If the message is in the non allowed Channels
    #
    # If all pass the bot will Ratio
    if random.randint(0,75) == 1 and I.message.author.id != I.botID and not(I.message.channel in Non_Ratio_Channel):
        # await message.channel.send(f"{message.author.mention} Ratio")
        I.Return_Message = f"{I.message.author.mention} Ratio"

        if bool(leaderboard.get(f'<@{I.message.author.id}>')) is True:
            leaderboard[f'<@{I.message.author.id}>'] += 1
        else:
            leaderboard[f'<@{I.message.author.id}>'] = 1
        temp = sorted(leaderboard.items(), key=lambda x:x[1], reverse=True)
        leaderboard = dict(temp)

        with open(filename, 'w') as f:
            json.dump(leaderboard, f)

        return
    
    elif random.randint(0,4080) == 4000 and I.message.author.id != I.BotId and not(I.message.channel in Non_Ratio_Channel):
        I.Return_Message = f"{I.message.author.mention} I actually kinda like this one"

def leaderboard(I):
    server_name = I.message.guild.name
    filename = f'{server_name}.json'

    if os.path.exists(filename):
            with open(filename, 'r') as f:
                leaderboard = json.load(f)
    else:
        leaderboard = {}
            
    num = 0
    embed = discord.Embed(title=f'Leaderboard for {server_name}', description='the top 10 yuh')
    embed.set_thumbnail(url=I.message.guild.icon)
    for key, value in leaderboard.items():
        user_id = key.translate(str.maketrans('', '', string.punctuation))
        user = I.client.user
        # If not in cache, try to fetch from Discord API
        if user is None:
            try:
                user = I.client.fetch_user(int(user_id))
            except:
                user_name = "Unknown User"
            else:
                user_name = user.name
        else:
            user_name = user.name
    
        if num <= 10:
            embed.add_field(name=f'{user_name} has been ratioed:', value=f'{value} times', inline=False)
            num += 1
            I.Return_Message = embed
        else:
            I.Return_Message = 'No one in this server has been ratioed yet :pensive:'