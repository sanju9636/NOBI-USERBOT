from pyrogram import Client, filters
import random

@Client.on_message(filters.user(OWNER_ID) & filters.command(["chance"], ["."]))
async def chance(client, message):
    text = message.text.split(hl + "chance ", maxsplit=1)[1]
    await message.edit(f"{text}\n\nᴄʜᴀɴᴄᴇ » {random.randint(1, 100)}%")
