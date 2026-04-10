import random
import json
import os
import discord

def CurrentRules(I):
    with open('Information Files\\Rules.txt', 'r') as file:
        I.Return_Message = file.read()

def ViewPoints(I):
    server_name = I.message.guild.name
    filename = f'{server_name}.json'

    if os.path.exists(filename):
        with open(filename, 'r') as f:
            leaderboard = json.load(f)
    else:
        leaderboard = {}
    
    embed = discord.Embed(
        title=f'Leaderboard for {server_name}',
        description='Users Point Vaules'
    )

    embed.set_thumbnail(url=I.message.guild.icon)

    if not leaderboard:
        I.Return_Message = 'No one in this server has points yet :pensive:'
        return

    for i, (user_id, data) in enumerate(leaderboard.items()):
        embed.add_field(
            name=f"{i+1}. {data['name']}",
            value=f"has {data['points']} points",
            inline=False
        )

    I.Return_Message = embed
    
def AddRules():
    return

def Join_The_Game(I):
    with open('Information Files\\Game_Members.txt', 'r') as file:
        player_list = [line.strip() for line in file.readlines()]
        file.close
    
    if str(I.message.user) not in player_list:
        with open('Information Files\\Game_Members.txt', 'a') as file:
            file.write(f'{I.message.user}\n')
            file.close
        I.Return_Message = 'was added to the Game'
    else:
        I.Return_Message = "you can't join twice"
        