import discord
from discord.ext import commands
from discord import app_commands
import time

import Ratio
import Information
import I_hardly_know_her
import Culling_Game
import Andrea_Fish

#Establish bot Id so bot doesnt respond to itself
#Change Bot Id to own bot
BotId = 177504009748217856
Last_IHKH = time.time()
IHKR_Cooldown = 600
GUILD_ID = discord.Object(id=1008443588344025089)

class Client(commands.Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        try:
            guild = discord.Object(id=1008443588344025089)
            synced = await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} commands to guild {guild.id}')
        except Exception as e:
            print(f'Error syncing commands: {e}')

#Establish the Client for the Discord Bot
intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="!", intents=intents)

@client.tree.command(name='points', description="View the point standings", guild=GUILD_ID)
async def leaderboard(interaction: discord.Interaction):
    I = Information.information(interaction,client)
    Culling_Game.ViewPoints(I)
    await interaction.response.send_message(embed=I.Return_Message)

@client.tree.command(name='leaderboard', description="View the ratio Leaderboard", guild=GUILD_ID)
async def leaderboard(interaction: discord.Interaction):
    I = Information.information(interaction,client)
    Ratio.leaderboard(I)
    await interaction.response.send_message(embed=I.Return_Message)

@client.tree.command(name='rules', description="View the Culling Game Rules", guild=GUILD_ID)
async def rules(interaction: discord.Interaction):
    I = Information.information(interaction,client)
    Culling_Game.CurrentRules(I)
    await interaction.response.send_message(I.Return_Message)

@client.tree.command(name='join', description="Join the Culling Game Rules", guild=GUILD_ID)
async def rules(interaction: discord.Interaction):
    I = Information.information(interaction,client)
    Culling_Game.Join_The_Game(I)
    message = str(interaction.user).capitalize()
    await interaction.response.send_message(f'{message[:-2]} {I.Return_Message}')

#Ratio Code
@client.event
#Checks at a sent message
async def on_message(message):
    if message.author == client.user:
        return
    
    I = Information.information(message, client=client, BotId=BotId)
    Ratio.ratio(I)
    if I.Return_Message != '':
        await message.channel.send(f"{I.Return_Message}")

    Andrea_Fish.Fish(I)
    if I.Return_Message == 'Fish Found':
        await message.channel.send('https://tenor.com/view/fish-spin-sha-gif-26863370')
    
    global Last_IHKH 
    if (time.time() - Last_IHKH) > IHKR_Cooldown:
        I_hardly_know_her.I_hardly_know_her(I)
        Last_IHKH = time.time()
        if I.CF:
            await message.add_reaction('<:feetChan:1047798934594146335>')
        if I.Last_IHKH!= -1:
            await message.channel.send(f"{message.author.mention} {I.Return_Message}")

client.run('MTA1MTc3NTYyNTg0MjY3MTcwNg.GBbrwb.KZdVoCzAEZdLKYcEkrFjqy1LMEbuTBYhqTe59k')
# ^ Security token