import discord
from discord.ext import commands
from discord import app_commands
import time

import ratio
import information
import I_hardly_know_her

#Establish bot Id so bot doesnt respond to itself
#Change Bot Id to own bot
BotId = 177504009748217856
Last_IHKH = time.time()
IHKR_Cooldown = 60
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

@client.tree.command(name='leaderboard', description="View the ratio Leaderboard", guild=GUILD_ID)
async def leaderboard(interaction: discord.Interaction):
    I = information.information(interaction,client)
    ratio.leaderboard(I)
    await interaction.response.send_message(embed=I.Return_Message)

#Ratio Code
@client.event
#Checks at a sent message
async def on_message(message):
    if message.author == client.user:
        return

    I = information.information(message, client=client, BotId=BotId)
    ratio.ratio(I)
    if I.Return_Message != '':
        await message.channel.send(f"{I.Return_Message}")
    if (time.time() - Last_IHKH) > IHKR_Cooldown:
        I_hardly_know_her.I_hardly_know_her(I)
        if I.CF:
            await message.add_reaction('<:feetChan:1047798934594146335>')
        if I.IHKH_vaule:
            await message.channel.send(f"{message.author.mention} {I.Return_Message}")

client.run('MTA1MTc3NTYyNTg0MjY3MTcwNg.GBbrwb.KZdVoCzAEZdLKYcEkrFjqy1LMEbuTBYhqTe59k')
# ^ Security token