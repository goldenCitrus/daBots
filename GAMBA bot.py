import random
from discord.ext import commands
import json
import discord
import string
import os


client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'{client.user} is now ready')
    
    
@client.event
async def on_message(message):
    
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)
    message_str = str(message.content)
    # no_punct = message_str.translate(str.maketrans('', '', string.punctuation))
    no_punct = message_str.lower()
    split_message = no_punct.split()
    
    # v Money/Banking System v
    server_id = message.guild.id
    filename = f'{server_id}_banking.json'
    
    if os.path.exists(filename):
            with open(filename, 'r') as f:
                banking = json.load(f)
    else:
        banking = {}
    # ^ Money/Banking System ^
    
    # v Coinflip Command v
    if split_message[0] == '!coinflip':
        x = random.randint(0,1)
        guess = split_message[2]
        bet = int(split_message[1])
        if guess == 'heads':
            guess = 1
        elif guess == 'tails':
            guess = 0
        if guess == x:
            await message.channel.send("Congrats you win " + str(bet * 2))
        else:
            await message.channel.send(f"You suck L + ratio you lost your stupid {bet} coins")
    #  ^ Coinflip Command ^
    
    #  v Help Command v
    elif split_message[0] == '!help':
        embed = discord.Embed(title=f'Help Menu', description='a list of commands you can use with this bot')
        embed.add_field(name=f'how to use !coinflip:', value=f'!coinflip [bet ammount] [heads/tails]', inline=False)
        await message.channel.send(embed=embed)
    #  ^ Help Comand ^



client.run('MTA3MDg4MjU2MzA5NjMzNDQ3MQ.GgRnTl.sDDtvy-FIj7V0KnJWjJwEw0k-dHP0caLofB8O0')
# ^ security token