from nextcord import *
from nextcord.ext import commands
import logging
import os
import time

import cbext.util as u
from cbext.owner import Owner
from cbext.test import Test
from cbext.misc import Misc

bot = commands.Bot(command_prefix="c!", description="CASbot is a test bot created by CAS, aka >>#0001.", owner_ids=u.owners)

logging.basicConfig(level=logging.INFO)

bot.add_cog(Owner(bot))
bot.add_cog(Test(bot))
bot.add_cog(Misc(bot))

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('c!hello'):
        await message.channel.send('Hello!')

TOKEN = os.getenv("CASBOT_TOKEN")

#if os.getlogin() == "casga":
#    with open("C:\\Users\\casga\\Desktop\\bot-token.txt", "r") as f:
#        TOKEN = f.read()

while True:
    bot.run(TOKEN)
    time.sleep(1)