from pyrogram import Client, filters
import random
from config import SUDO_USERS

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["chance"], ["."]))
async def chance(client, message):
    text = message.text.split(hl + "chance ", maxsplit=1)[1]
    await message.edit(f"{text}\n\nᴄʜᴀɴᴄᴇ » {random.randint(1, 100)}%")
