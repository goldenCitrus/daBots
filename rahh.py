import io
import random
import requests
import discord
from discord.ext import commands
from PIL import Image
import string

# Create a new Discord bot
client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'{client.user} is now ready')

# This is the list of image URLs that the bot will choose from
image_urls = ['https://i.pinimg.com/originals/2d/52/f5/2d52f554654c2eecc439332cf6040629.jpg', 'https://static.wikia.nocookie.net/tiktok/images/6/6b/Vinnie_Hacker_appearance.PNG/revision/latest?cb=20220413210124', 'https://filmdaily.co/wp-content/uploads/2021/07/VH-cancelled-lede--1300x731.jpg', 'https://media.tenor.com/1w9zAdvc3awAAAAd/pepe-agony.gif']

# This is the list of image files that the bot will use
# These will be created by downloading the images from the URLs
image_files = []

# This function will download the images from the URLs and store them in the image_files list
async def download_images():
    for url in image_urls:
        response = requests.get(url)
        image_data = response.content
        image_file = Image.open(io.BytesIO(image_data))
        image_files.append(image_file)

# This function will be called when the bot receives a message
@client.event
async def on_message(message):

    message_str = str(message.content)

    if message.author == client.user:
        return
  # Check if the message is 'vinnie'
    if message_str == 'vinnie':
        await message.channel.send(f"{message.author.mention} That's me")
  #if message.content == 'vinnie':
    # Choose a random image from the list of files
   # await message.channel.send(f"{message.author.mention} That's me")

# Start the bot
client.run('MTA1MTgwMTkwMzkzMzE3Nzg1Nw.GwXQfo.dPlMRp0C1HRrGUTnIv5zcXIpFkH-p2ajN3Amcg')