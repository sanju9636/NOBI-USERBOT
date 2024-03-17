import random
from pyrogram import Client, filters
from config import SUDO_USERS

hl = "."

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["luck"], [hl]))
async def luck(client, message):
    if hl + "luck " in message.text:
        text = message.text.split(hl + "luck ", maxsplit=1)[1]
        score = ["1", "2", "-1", "-5", "-10", "100", "-99", "-100", "-10000", "-50"]
        luck_score = random.choice(score)
        emojis = ["💩", "💩", "💩", "💩", "💩", "🍀", "💩", "💩", "💩", "💩"]
        emoji = random.choice(emojis)
        await message.reply(f"**{text}**\n\n**ʟᴜᴄᴋ ꜱᴄᴏʀᴇ**: **{luck_score}** %\n**ʏᴏᴜʀ ʟᴜᴄᴋ**: {emoji}")
    else:
        await message.reply("ɪɴᴠᴀʟɪᴅ ᴄᴏᴍᴍᴀɴᴅ ꜰᴏʀᴍᴀᴛ. ᴘʟᴇᴀꜱᴇ ᴜꜱᴇ `.luck` <ʏᴏᴜʀ ɴᴀᴍᴇ>")
