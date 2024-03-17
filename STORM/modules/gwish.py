import random
from pyrogram import Client, filters
from config import SUDO_USERS

hl = "."

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["gm"], [hl]))
async def chance(client, message):
    text = message.text.split(hl + "gm ", maxsplit=1)[1]
    GUD_MORNING = ["╭━━━┳━━━┳━━━┳━━━╮\n┃╭━╮┃╭━╮┃╭━╮┣╮╭╮┃\n┃┃╱╰┫┃╱┃┃┃╱┃┃┃┃┃┃\n┃┃╭━┫┃╱┃┃┃╱┃┃┃┃┃┃\n┃╰┻━┃╰━╯┃╰━╯┣╯╰╯┃\n╰━━━┻━━━┻━━━┻━━━╯.\n\n╱╱╱╱╱╱╱╱╱╱╭╮\n╭━━┳━┳┳┳━┳╋╋━┳┳━╮\n┃┃┃┃╋┃╭┫┃┃┃┃┃┃┃╋┃\n╰┻┻┻━┻╯╰┻━┻┻┻━╋╮┃\n╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━╯"]
    await message.reply(f"**{text}**\n\n{GUD_MORNING}")
 
@Client.on_message(filters.user(SUDO_USERS) & filters.command(["ga"], [hl]))
async def chance(client, message):
    text = message.text.split(hl + "ga ", maxsplit=1)[1]
    GUD_AFTERNOON = ["╭━━━┳━━━┳━━━┳━━━╮\n┃╭━╮┃╭━╮┃╭━╮┣╮╭╮┃\n┃┃╱╰┫┃╱┃┃┃╱┃┃┃┃┃┃\n┃┃╭━┫┃╱┃┃┃╱┃┃┃┃┃┃\n┃╰┻━┃╰━╯┃╰━╯┣╯╰╯┃\n╰━━━┻━━━┻━━━┻━━━╯\n╭━━━╮\n┃╭━╮┃\n┃┃╱┃┃\n┃╰━╯┃\n┃╭━╮┃\n╰╯╱╰╯\n╭━━━╮\n┃╭━━╯\n┃╰━━╮\n┃╭━━╯\n┃┃\n╰╯\n╭━━━━╮\n┃╭╮╭╮┃\n╰╯┃┃╰╯\n╱╱┃┃\n╱╱┃┃\n╱╱╰╯\n╭━━━╮\n┃╭━━╯\n┃╰━━╮\n┃╭━━╯\n┃╰━━╮\n╰━━━╯\n╭━━━╮\n┃╭━╮┃\n┃╰━╯┃\n┃╭╮╭╯\n┃┃┃╰╮\n╰╯╰━╯\n╭━╮╱╭╮\n┃┃╰╮┃┃\n┃╭╮╰╯┃\n┃┃╰╮┃┃\n┃┃╱┃┃┃\n╰╯╱╰━╯\n╭━━━╮\n┃╭━╮┃\n┃┃╱┃┃\n┃┃╱┃┃\n┃╰━╯┃\n╰━━━╯\n╭━━━╮\n┃╭━╮┃\n┃┃╱┃┃\n┃┃╱┃┃\n┃╰━╯┃\n╰━━━╯\n╭━╮╱╭╮\n┃┃╰╮┃┃\n┃╭╮╰╯┃\n┃┃╰╮┃┃\n┃┃╱┃┃┃\n╰╯╱╰━╯"]
    await message.reply(f"**{text}**\n\n{GUD_AFTERNOON}")

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["gn"], [hl]))
async def chance(client, message):
    text = message.text.split(hl + "gn ", maxsplit=1)[1]
    GUD_NIGHT = ["╭━━━╮╱╱╱╱╱╱╱╭╮\n┃╭━╮┃╱╱╱╱╱╱╱┃┃\n┃┃╱╰╋━━┳━━┳━╯┃\n┃┃╭━┫╭╮┃╭╮┃╭╮┃\n┃╰┻━┃╰╯┃╰╯┃╰╯┃\n╰━━━┻━━┻━━┻━━╯\n╭━╮╱╭╮╱╱╱╭╮╱╭╮\n┃┃╰╮┃┃╱╱╱┃┃╭╯╰╮\n┃╭╮╰╯┣┳━━┫╰┻╮╭╯\n┃┃╰╮┃┣┫╭╮┃╭╮┃┃\n┃┃╱┃┃┃┃╰╯┃┃┃┃╰╮\n╰╯╱╰━┻┻━╮┣╯╰┻━╯\n╱╱╱╱╱╱╭━╯┃\n╱╱╱╱╱╱╰━━╯"]
    await message.reply(f"**{text}**\n\n{GUD_NIGHT}")
