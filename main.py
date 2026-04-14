"""Code to run the dicord bot client, references the other files to run the functions"""
import time
import discord
from discord.ext import commands

import culling_game
import fish
import ihkh
import information
import ratio

#Establish bot Id so bot doesnt respond to itself
#Change Bot Id to own bot
BOTID = 177504009748217856
IHKR_COOLDOWN = 500
GUILD_ID = discord.Object(id=1008443588344025089)

def main():
    """Runs file"""
    with open('Information Files\\client.txt', encoding="utf-8") as file:
        token = file.read().strip()
        client.run(f'{token}')

class Client(commands.Bot):
    """Builds client obejct"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.last_ihkh = time.time()

    async def on_ready(self):
        """Runs the syncing to the server"""
        print(f'Logged on as {self.user}!')
        try:
            guild = discord.Object(id=1008443588344025089)
            synced = await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} commands to guild {guild.id}')
        except RuntimeError as e:
            print(f'Error syncing commands(RuntimeError): {e}')
        except TypeError as e:
            print(f'Error syncing commands(TypeError): {e}')
        except NameError as e:
            print(f'Error syncing commands(NameError): {e}')

#Establish the Client for the Discord Bot
intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="!", intents=intents)

@client.tree.command(name='rule_add', description="Add a rule to the game", guild=GUILD_ID,)
async def ruleadd(interaction: discord.Interaction, ctx: str):
    """Culling Game feature, allows for rules to be added"""
    info = information.Information(interaction,client)
    culling_game.add_rules(info,ctx)
    await interaction.response.send_message(embed=info.return_message)

@client.tree.command(name='points', description="View the point standings", guild=GUILD_ID)
async def points_leaderboard(interaction: discord.Interaction):
    """Culling Game feature, prints a leaderboard of points"""
    info = information.Information(interaction,client)
    culling_game.view_points(info)
    await interaction.response.send_message(embed=info.return_message)

@client.tree.command(name='leaderboard', description="View the ratio leaderboard", guild=GUILD_ID)
async def ratio_leaderboard(interaction: discord.Interaction):
    """Ratio Feature, View the ratio leaderboard"""
    info = information.Information(interaction,client)
    ratio.leaderboard(info)
    await interaction.response.send_message(embed=info.return_message)

@client.tree.command(name='rules', description="View the Culling Game Rules", guild=GUILD_ID)
async def rules(interaction: discord.Interaction):
    """Culling Game feature, allows for rules to be viewed"""
    info = information.Information(interaction,client)
    culling_game.current_rules(info)
    await interaction.response.send_message(info.return_message)

@client.tree.command(name='join', description="Join the Culling Game Rules", guild=GUILD_ID)
async def join(interaction: discord.Interaction):
    """Culling Game feature, allows for new members to join"""
    info = information.Information(interaction,client)
    culling_game.join_the_game(info)
    message = str(interaction.user).capitalize()
    await interaction.response.send_message(f'{message[:-2]} {info.return_message}')

@client.event
async def on_message(message):
    """Checks a sent message for Ratio, IHKH and Fish"""
    if message.author == client.user:
        return
    info = information.Information(message, client=client, botid=BOTID)
    ratio.ratio(info)
    if info.return_message != '':
        await message.channel.send(f"{info.return_message}")
    fish.has_fish(info)
    if info.return_message == 'Fish Found':
        await message.channel.send('https://tenor.com/view/fish-spin-sha-gif-26863370')
    if (time.time() - client.last_ihkh) > IHKR_COOLDOWN:
        ihkh.ihkh(info)
        client.last_ihkh = time.time()
        if info.chandler and info.is_ihkh:
            await message.add_reaction('<:feetChan:1047798934594146335>')
        elif info.is_ihkh:
            await message.channel.send(f"{message.author.mention} {info.return_message}")

if __name__ == "__main__":
    main()
