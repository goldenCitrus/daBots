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
    
def AddRules(I,RuleAdd):
    server_name = I.message.guild.name
    filename = f'{server_name}.json'
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            UserInfo = json.load(f)
    else:
        UserInfo = {}

    if UserInfo[str(I.message.user.id)]["points"] >= 5:
        embed = discord.Embed(
        title=f'Rule was added to the Game',
        description=f'{RuleAdd}'
    )
        UserInfo[str(I.message.user.id)]["points"] -= 5
        embed.set_thumbnail(url=I.message.guild.icon)

        with open('Information Files\\Rules.txt', 'a') as file:
            file.write(f'{RuleAdd}\n')

        I.Return_Message = embed

        with open(filename, 'w') as f:
                json.dump(UserInfo, f, indent=4)
    else:
        embed = discord.Embed(
        title=f'Rule was not added to the Game',
        description=f'You dont have the points needed'
        )
        I.Return_Message = embed

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
        