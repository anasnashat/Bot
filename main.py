import os, asyncio, time
from dotenv import load_dotenv

import time
import discord
from discord.ext import commands

load_dotenv()

bot = commands.Bot(command_prefix='!', case_insensitive=True, self_bot=True)

msg = '''
Crossfire Epic new server for Everyone EG,NA,BR servers , Download it now and get 150k ZP 
Website: 
https://cfepic.com/
Download:
https://www.mediafire.com/file/oohjr4em6n6irtf/CF_EPIC_
Discord:
https://discord.gg/cfepic
'''


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == bot.user:
        return

    if message.content.startswith('!epic'):
        # dm all members of the guild
        for member in message.guild.members:
            try:
                await member.send(msg)
                print(f"Sent message to {member}")
                time.sleep(25)
            except:
                pass

    else:
        await bot.process_commands(message)


Token = 'MTA0NDA5NTE5MDgwNzM1MTM3Ng.GdTbqe.jO1VgRHUaGA9cFiKb8g9Rm_JqmAbaJg01LtQwU'
bot.run(Token)

# important run bot from shell not from run to work
