import random
from pyrogram import Client, filters
from config import SUDO_USERS

hl = "."

# Define the luck command handler
@Client.on_message(filters.user(SUDO_USERS) & filters.command(["luck"], [hl]))
async def luck(client, message):
    # Extract the text following the /luck command
    if hl + "luck " in message.text:
        text = message.text.split(hl + "luck ", maxsplit=1)[1]
        
        # Generate a random luck score between 1 and 100
        score = ["1", "2", "-1", "-5", "-10", "100", "-99", "-100", "-10000", "-50"]
        luck_score = random.randint(score)
        
        # Select a random emoji
        emojis = ["💩", "💩", "💩", "💩", "💩", "🍀", "💩", "💩", "💩", "💩"]
        emoji = random.choice(emojis)
        
        # Send the luck score and selected emoji as a reply
        await message.reply(f"{text}\n\n**ʟᴜᴄᴋ ꜱᴄᴏʀᴇ**: {luck_score}%\n**ʏᴏᴜʀ ʟᴜᴄᴋ**: {emoji}")
    else:
        # Handle incorrect command format
        await message.reply("ɪɴᴠᴀʟɪᴅ ᴄᴏᴍᴍᴀɴᴅ ꜰᴏʀᴍᴀᴛ. ᴘʟᴇᴀꜱᴇ ᴜꜱᴇ {hl}ʟᴜᴄᴋ <ʏᴏᴜʀ ɴᴀᴍᴇ>")
