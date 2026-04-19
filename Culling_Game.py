"""Contains the functiontaly for the Culling Games"""
import json
import os

import discord

def current_rules(info):
    """Displays the current rules"""
    with open('Information Files\\Rules.txt', encoding="utf-8") as file:
        return_string = ''
        for num, txt in enumerate(file.readlines()):
            return_string += f'{num}. {txt}'
        info.return_message = return_string

def view_points(info):
    """View the points"""
    server_name = info.message.guild.name
    filename = f'Information Files\\{server_name}.json'

    with open('Information Files\\Game_Members.txt', encoding="utf-8") as f:
        game_members = [line.strip('#0\n').capitalize() for line in f.readlines()]

    print(game_members)
    if os.path.exists(filename):
        with open(filename, encoding="utf-8") as f:
            board = json.load(f)
    else:
        board = {}
    embed = discord.Embed(
        title=f'Leaderboard for {server_name}',
        description='Users Point Vaules'
    )

    embed.set_thumbnail(url=info.message.guild.icon)

    if not board:
        info.return_message = 'No one in this server has points yet :pensive:'
        return

    board = dict(sorted(
            board.items(),
            key=lambda x: x[1]["points"],
            reverse=True
        ))
    counter = 0
    for _, (_, data) in enumerate(board.items()):
        print(data['name'])
        if data['name'] in game_members:
            counter += 1
            embed.add_field(
                name=f"{counter}. {data['name']}",
                value=f"has {data['points']} points",
                inline=False
            )

    info.return_message = embed
    
def add_rules(info, rule):
    """Add a rule to the culling games"""
    server_name = info.message.guild.name
    filename = f'Information Files\\{server_name}.json'

    if os.path.exists(filename):
        with open(filename, encoding="utf-8") as f:
            user_info = json.load(f)
    else:
        user_info = {}

    if user_info[str(info.message.user.id)]["points"] >= 5:
        embed = discord.Embed(
        title='Rule was added to the Game',
        description=f'{rule}'
    )
        user_info[str(info.message.user.id)]["points"] -= 5
        embed.set_thumbnail(url=info.message.guild.icon)

        with open('Information Files\\Rules.txt', encoding="utf-8") as file:
            file.write(f'{rule}\n')

        info.return_message = embed

        with open(filename, encoding="utf-8") as f:
            json.dump(user_info, f, indent=4)
    else:
        embed = discord.Embed(
        title='Rule was not added to the Game',
        description='You dont have the points needed'
        )

        info.return_message = embed
    return

def join_the_game(info):
    """Allows users to join the game"""
    with open('Information Files\\Game_Members.txt', encoding="utf-8") as file:
        player_list = [line.strip() for line in file.readlines()]
    if str(info.message.user) not in player_list:
        with open('Information Files\\Game_Members.txt', encoding="utf-8") as file:
            file.write(f'{info.message.user}\n')
        info.return_message = 'was added to the Game'
    else:
        info.return_message = "you can't join twice"
