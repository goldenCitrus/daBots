import os
import json
import random
import discord

Non_Ratio_Channel = {"vent-advice-channel"}

def ratio(I):
    filename = f'{I.message.guild.name}.json'

    # Load leaderboard
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            leaderboard = json.load(f)
    else:
        leaderboard = {}

    if I.message.author == I.client.user:
        return

    user_id = str(I.message.author.id)
    user_name = I.message.author.name.capitalize()

    # Ratio trigger
    if random.randint(0,75) == 1 and user_id != str(I.botID) and I.message.channel.name not in Non_Ratio_Channel:
        I.Return_Message = f"{I.message.author.mention} Ratio"

        if user_id in leaderboard:
            leaderboard[user_id]["ratio"] += 1
            leaderboard[user_id]["points"] += 1
        else:
            leaderboard[user_id] = {
                "name": user_name,
                "ratio": 1,
                "points": 1
            }

        # Sort leaderboard
        leaderboard = dict(sorted(
            leaderboard.items(),
            key=lambda x: x[1]["ratio"],
            reverse=True
        ))

        with open(filename, 'w') as f:
            json.dump(leaderboard, f, indent=4)

        return

    elif random.randint(0,4080) == 4000 and user_id != str(I.botID) and I.message.channel.name not in Non_Ratio_Channel:
        I.Return_Message = f"{I.message.author.mention} I actually kinda like this one"

def leaderboard(I):
    server_name = I.message.guild.name
    filename = f'{server_name}.json'

    if os.path.exists(filename):
        with open(filename, 'r') as f:
            leaderboard = json.load(f)
    else:
        leaderboard = {}

    embed = discord.Embed(
        title=f'Leaderboard for {server_name}',
        description='Top 10 most ratioed users'
    )

    embed.set_thumbnail(url=I.message.guild.icon)

    if not leaderboard:
        I.Return_Message = 'No one in this server has been ratioed yet :pensive:'
        return

    for i, (user_id, data) in enumerate(leaderboard.items()):
        if i >= 10:
            break

        embed.add_field(
            name=f"{i+1}. {data['name']}",
            value=f"Ratioed {data['ratio']} times",
            inline=False
        )

    I.Return_Message = embed