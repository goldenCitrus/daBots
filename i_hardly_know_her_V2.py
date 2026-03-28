import discord
from discord.ext import commands
import random
import string
import json
import os

client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
    print(f'{client.user} is now ready')

@client.event
async def on_message(message):
    if message.author == client.user or message.author == 765235854623899700:
        return

    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)
    message_str = str(message.content)
    no_punct = message_str.translate(str.maketrans('', '', string.punctuation))
    no_punct = no_punct.lower()
    split_message = no_punct.split()
    split_message_punct = message_str.split()
    
    server_name = message.guild.name
    filename = f'{server_name}_idker_cooldown.json'
    active_filename = f'{server_name}_idker_active.json'
    if os.path.exists(filename):
        with open(active_filename, 'w') as f:
            try:
                cooldown = json.load(f)
            except:
                cooldown = 0
    else:
        cooldown = 0
        
    # rnd = random.randint(10,30)
    if message.author.id == 186239130596933632:
            await message.add_reaction('<:feetChan:1047798934594146335>')
            
    elif split_message_punct[0] == '!cooldown':
        cooldown = int(split_message[1])
        with open(filename, 'w') as f:
            json.dump(cooldown, f)
        with open(active_filename, 'w') as f2:
            json.dump(cooldown, f2)
        await message.channel.send(f"idkerV2 cooldown for {message.guild.name} has been set to {cooldown}")
     
    else:
        # I hardly know her command v v
        if len(message_str) < 100:
            banned_words = ["boomer", "chandler", "bluhoser", "carter"]
            er_words = []
            for i in split_message:
                try:
                    if i[-2:] == 'er' and i not in banned_words and len(i) > 3:
                        er_words.append(i)
                except IndexError:
                    continue
                # 
                if cooldown == 0:
                    send_message = True
                    # Open with 'r' to read, and use .read() to get the content
                    with open(filename, 'r') as f:
                        f_str = f.read().strip() # .strip() removes hidden spaces/newlines
                        if f_str: # This checks if the string is NOT empty
                            temp_var = int(f_str)
                        else:
                            temp_var = 0  # Default to 0 if the file is empty

                    with open(active_filename, 'w') as f2:
                        json.dump(temp_var, f2)
                else:
                     send_message = False
            cooldown -= 1
            if bool(er_words) == True and send_message == True:
                if len(er_words) == 1:
                    await message.channel.send(f"{message.author.mention} {er_words.pop().capitalize()}? I hardly know her!")
                else:
                    len_er_words = len(er_words)
                    the_chosen_num = random.randint(1,len_er_words)
                    the_chosen_str = er_words[the_chosen_num-1]
                    await message.channel.send(f"{message.author.mention} {the_chosen_str.capitalize()}? I hardly know her!")
            with open(active_filename, 'w') as f:
                json.dump(cooldown, f)
        # I hardly know her command ^ ^
        
        
    
            
    # if message.author == client.user and message_str == "Well, well, well, someone sure wants some pokespawns!":
        # await message.delete()

# @client.event
# async def on_message(message):
#     if message.author.bot and message.content == "Well, well, well, someone sure wants some pokespawns!":
#         # time.sleep(5)
#         message.delete()


client.run('MTA1MTc2NjEzMDgwMjQzNDA5OA.GaSVyN.LgYVaoTqWZf2Lf9zdpnQ8FDfcq-KoVw1FExBlw')
# ^ security token