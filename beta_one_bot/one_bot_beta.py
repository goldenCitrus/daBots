import discord
from discord.ext import commands
import time

import ratio
import information
import I_hardly_know_her

#Establish bot Id so bot doesnt respond to itself
#Change Bot Id to own bot
BotId = 177504009748217856

#gets Guild ID
const guild = client.guilds.cache.get(guildID)

Last_IHKH = time.time()
IHKR_Cooldown = 0

#Establish the Client for the Discord Bot
client = discord.Client(intents=discord.Intents.all())
# bot = commands.Bot(command_prefix='!', intents=discord.Intents.default())
    
@client.event
async def on_ready():
    print(f'{client.user} is now ready')

function setupSlashCommands(client, guildId) {
    const commands = [
    {
        name: 'leaderboard',
        description: 'leaderboard for who has been ratiod',
        options: [
            {
                type: 'EMBED',
                required: true,
                maxLength: 2000
            }
                ]
    }
]
};


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


#@client.command()
#async def ratio(ctx):
#    I = information.information(ctx)
#    ratio.leaderboard(I)
#    await ctx.send(f"{I.Return_Message}")

client.run('MTA1MTc3NTYyNTg0MjY3MTcwNg.GBbrwb.KZdVoCzAEZdLKYcEkrFjqy1LMEbuTBYhqTe59k')
# ^ Security token
