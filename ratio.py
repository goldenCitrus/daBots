""""""
import os
import json
import random
import discord

NON_RATIO_CHANNEL = {"vent-advice-channel"}

def ratio(info):
    """Random chance to rely with ratio to a message"""
    filename = f'Information Files\\{info.message.guild.name}.json'

    #User Info
    user_id = str(info.message.author.id)
    user_name = info.message.author.name.capitalize()

    #Condtions
    send_ratio = random.randint(0,1) == 1
    shiny_message = random.randint(0,4080) == 4000
    is_user_bot = user_id != str(info.botid)
    valid_channel = info.message.channel.name not in NON_RATIO_CHANNEL

    # Load leaderboard
    if os.path.exists(filename):
        with open(filename, encoding="utf-8") as f:
            board = json.load(f)
    else:
        board = {}

    if info.message.author == info.client.user:
        return

    # Ratio trigger
    if send_ratio and is_user_bot and valid_channel:
        info.return_message = f"{info.message.author.mention} Ratio"

        if user_id in board:
            board[user_id]["ratio"] += 1
        else:
            board[user_id] = {
                "name": user_name,
                "ratio": 1,
                "points": 0,
                "penalty": 0,
                "player": 0
            }

        with open('Information Files\\Game_Members.txt', encoding="utf-8") as f:
            game_members = [line.strip('\n') for line in f.readlines()]

        print(user_name)
        print(game_members)
        if user_name.strip() in game_members:
            board[user_id]["points"] += 1

        # Sort leaderboard
        board = dict(sorted(
            board.items(),
            key=lambda x: x[1]["ratio"],
            reverse=True
        ))

        with open(filename, mode="w", encoding="utf-8") as f:
            json.dump(board, f, indent=4)

        return

    elif shiny_message and is_user_bot and valid_channel:
        info.return_message = f"{info.message.author.mention} I actually kinda like this one"

def leaderboard(info):
    """Display's a leaderboard of ratioed users"""
    server_name = info.message.guild.name
    filename = f'Information Files\\{server_name}.json'

    if os.path.exists(filename):
        with open(filename, encoding="utf-8") as f:
            board = json.load(f)
    else:
        board = {}

    embed = discord.Embed(
        title=f'Leaderboard for {server_name}',
        description='Top 10 most ratioed users'
    )

    embed.set_thumbnail(url=info.message.guild.icon)

    if not board:
        info.return_message = 'No one in this server has been ratioed yet :pensive:'
        return
    for i, (_, data) in enumerate(board.items()):
        if i >= 10:
            break

        embed.add_field(
            name=f"{i+1}. {data['name']}",
            value=f"Ratioed {data['ratio']} times",
            inline=False
        )

    info.return_message = embed
