import os
import discord
from discord import user
from discord.ext import commands
import random
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path(r"\LuckyCatBot\.env")
load_dotenv = (dotenv_path == dotenv_path)
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
@client.event


async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
   
   if message.author == client.user:
    return
   msg = message.content

   #tosses the coin to get heads or tails 
   if msg.startswith('-toss'):
      rand = random.randint(0,1)
      if(rand == 0):
         await message.channel.send(file=discord.File(r'C:\Users\l\Downloads\Jeanne_Projects\ProgrammingProjects\LuckyCatBot\images\headscat.png'))
         await message.channel.send("You got heads!")
      else:
         await message.channel.send(file=discord.File(r'C:\Users\l\Downloads\Jeanne_Projects\ProgrammingProjects\LuckyCatBot\images\tailscat.png'))
         await message.channel.send("You got tails!")   
   #show the pics as choices
   elif msg.startswith('-choices'):
      await message.channel.send(file=discord.File(r'C:\Users\l\Downloads\Jeanne_Projects\ProgrammingProjects\LuckyCatBot\images\headscat.png'))
      await message.channel.send(file=discord.File(r'C:\Users\l\Downloads\Jeanne_Projects\ProgrammingProjects\LuckyCatBot\images\tailscat.png'))





client.run(TOKEN) 
